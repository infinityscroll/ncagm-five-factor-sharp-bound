"""Independent explicit-word reconstruction of the final eight Gram blocks."""
import sys
if sys.argv[1:] != ['--authorized-worker']:
    raise SystemExit('Run only under the separately authorized bounded supervisor')
sys.set_int_max_str_digits(1000000)
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
from pathlib import Path
from collections import defaultdict
from fractions import Fraction
from itertools import product
import json,hashlib,time,traceback
import sympy as sp
from sympy import QQ

BASE=Path(__file__).resolve().parent
START=time.process_time()
def save(name,value):
    with (BASE/name).open('x') as f:
        json.dump(value,f,indent=2,sort_keys=True);f.write('\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def basis(n):return [()]+[(i,) for i in range(n)]+list(product(range(n),repeat=2))

def canonical(a,b,marked):
    # Encode equality patterns of two words, allowing exchange of the words.
    # No reversal of either word: these are Gram entries, not word products.
    def encode(pair):
        seen=[0] if marked else []
        ans=[]
        for w in pair:
            for label in w:
                if label not in seen:seen.append(label)
                ans.append(seen.index(label))
            ans.append(-1)
        return tuple(ans[:-1])
    return min(encode((a,b)),encode((b,a)))

def index(marked):
    keys={}
    for a in basis(6):
        for b in basis(6):
            key=canonical(a,b,marked)
            if key not in keys:keys[key]=len(keys)
    return keys

def vector(terms):
    d=defaultdict(int)
    for w,c in terms:d[w]+=c
    return {w:c for w,c in d.items() if c}

def representatives(n,marked):
    active=list(range(1 if marked else 0,n))
    i,j,k,l=active[:4]
    c={i:1,j:-1}
    wt=lambda x:c.get(x,0)
    one={():1}
    linear={(x,):1 for x in active}
    squares={(x,x):1 for x in active}
    pairs={(x,y):1 for x in active for y in active if x!=y}
    L={(x,):wt(x) for x in active if wt(x)}
    Q={(x,x):wt(x) for x in active if wt(x)}
    P=vector(((x,y),wt(x)+wt(y)) for x in active for y in active if x!=y)
    M=vector(((x,y),wt(x)-wt(y)) for x in active for y in active if x!=y)
    if marked:
        trivial=[one,{(0,):1},linear,{(0,0):1},{(0,x):1 for x in active},
                 {(x,0):1 for x in active},squares,pairs]
        standard=[L,{(0,x):wt(x) for x in active if wt(x)},
                  {(x,0):wt(x) for x in active if wt(x)},Q,P,M]
    else:
        trivial=[one,linear,squares,pairs]
        standard=[L,Q,P,M]
    switch=vector([(w,1) for w in [(i,j),(j,i),(k,l),(l,k)]]+
                  [(w,-1) for w in [(i,k),(k,i),(j,l),(l,j)]])
    skew=vector([(w,1) for w in [(i,j),(j,k),(k,i)]]+
                [(w,-1) for w in [(j,i),(k,j),(i,k)]])
    assert sum(v*v for v in switch.values())==8
    assert sum(v*v for v in skew.values())==6
    return [trivial,standard,[switch],[skew]]

def count_maps(n,marked,ids):
    answer={}
    for block,vs in enumerate(representatives(n,marked)):
        for i,vi in enumerate(vs):
            for j in range(i,len(vs)):
                row=[0]*len(ids)
                for left,ci in vi.items():
                    for right,cj in vs[j].items():
                        row[ids[canonical(left,right,marked)]]+=ci*cj
                answer[block,i,j]=row
    return answer

def product_poly(a,b):
    out=[Fraction(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out

def main():
    assert (BASE/'RUN-ATTEMPT.json').is_file()
    manifest=json.loads((BASE/'FROZEN-MANIFEST.json').read_text())
    for p,h in manifest['sha256'].items():assert sha(BASE/p)==h,p
    cert=json.loads((BASE/'CERTIFICATE.json').read_text())
    blockdata=json.loads((BASE/'INPUT-BLOCKS.json').read_text())
    u=sp.Symbol('u');F=QQ.frac_field(u);U=F.from_sympy(u)
    parse=lambda text:F.from_sympy(sp.sympify(text,locals={'u':u}))
    nr=(32*U**2-18*U+1)/(16*U**2-12*U+1)
    orbits=[parse(x) for x in cert['orbit_functions']]
    assert len(orbits)==81
    free=blockdata['free_orbit_columns']
    assert free==[17,25,61,62,64,65,66,68,69,70,71,72,73,74,76,78,79,80]
    parameters=[orbits[i] for i in free]+[F.one]
    blocks={b['name']:b for b in blockdata['blocks']}
    sample_sizes=list(range(5,10))
    lagrange=[]
    for at in sample_sizes:
        p=[Fraction(1)]
        for other in sample_sizes:
            if other!=at:p=product_poly(p,[Fraction(-other,at-other),Fraction(1,at-other)])
        assert len(p)==5
        for x in sample_sizes:
            assert sum(c*x**k for k,c in enumerate(p))==int(x==at)
        lagrange.append(p)
    powers=[nr**k for k in range(5)]
    maps_out=[];checked=0;scalar_map_count=0
    for marked,prefix,offset in [(True,'G',0),(False,'H',59)]:
        ids=index(marked)
        assert len(ids)==(59 if marked else 22)
        data=[count_maps(n,marked,ids) for n in sample_sizes]
        assert all(set(d)==set(data[0]) for d in data)
        for key in sorted(data[0]):
            block,i,j=key;name=prefix+str(block)
            b=blocks[name];size=b['size'];assert 0<=i<=j<size
            coefficients=[];mapped=F.zero
            for col in range(len(ids)):
                p=[sum(Fraction(d[key][col])*lagrange[s][degree] for s,d in enumerate(data)) for degree in range(5)]
                # Recover each exact integer count at the five interpolation points.
                for s,n in enumerate(sample_sizes):
                    assert sum(v*n**k for k,v in enumerate(p))==data[s][key][col]
                coefficients.append([str(v) for v in p])
                if any(p):
                    f=sum((F(v.numerator)/F(v.denominator)*powers[k] for k,v in enumerate(p)),F.zero)
                    mapped+=f*orbits[offset+col]
                scalar_map_count+=1
            row=b['affine_entry_rows'][i*size+j]
            assert len(row)==19
            expected=sum((parse(v)*parameters[k] for k,v in enumerate(row)),F.zero)
            assert mapped==expected,('generic_block_identity',name,i,j)
            reverse=b['affine_entry_rows'][j*size+i]
            assert sum((parse(v)*parameters[k] for k,v in enumerate(reverse)),F.zero)==mapped
            maps_out.append({'block':name,'i':i,'j':j,'count_polynomials_ascending':coefficients,
                             'identity_exact_Q_u':True})
            checked+=1
        print(json.dumps({'phase':'block_maps_complete','prefix':prefix,'entries':checked,'worker_cpu_seconds':time.process_time()-START}),flush=True)
    assert checked==81
    save('RECONSTRUCTED-MAPS.json',{'sample_sizes':sample_sizes,'polynomial_degree_bound':4,
         'degree_bound_basis':'Each pair of words has at most four free labels; count depends on n through a sum of falling factorials of order at most four. Representatives have fixed anchor weights. Thus interpolation is exact for all integer n>=5, not a sampled PSD test.',
         'maps':maps_out})
    save('RESULT.json',{'status':'COMPLETED_EXACT_GATE','all_checks':'PASS','upper_triangle_identities':checked,
         'scalar_polynomial_maps':scalar_map_count,'field':'Q(u)','independent_explicit_word_counts':True,
         'source_generator_imported':False,'certificate_sha256':sha(BASE/'CERTIFICATE.json'),
         'reconstructed_maps_sha256':sha(BASE/'RECONSTRUCTED-MAPS.json'),
         'source_sha256':sha(Path(__file__)),'worker_cpu_seconds':time.process_time()-START,
         'scope':'Reconstruct all eight complete contracted Gram blocks of this fixed candidate. PSD and original localizer identities are separate obligations. No novelty claim.'})

if __name__=='__main__':
    try:main()
    except BaseException as e:
        save('WORKER-FAILURE.json',{'status':'INCOMPLETE_NO_RESULT','error':type(e).__name__+': '+str(e),
              'worker_cpu_seconds':time.process_time()-START})
        traceback.print_exc();raise
