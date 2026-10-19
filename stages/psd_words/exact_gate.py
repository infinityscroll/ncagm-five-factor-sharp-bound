#!/usr/bin/env python3
"""Prepared solver-free proof-data checker. No discovery-worker imports."""
import sys
if sys.argv[1:] != ["--authorized-worker"]:
    raise SystemExit("Prepared only: later root authorization and supervisor required")
sys.set_int_max_str_digits(1000000)
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import comb
from pathlib import Path
import hashlib
import json
import time
import traceback

ROOT = Path(__file__).resolve().parent
START = time.process_time()
VENV = ROOT.parent / "overnight-ncagm-sharp-root-20261018/.venv"
assert sys.version_info[:2] == (3, 12)
assert Path(sys.prefix).resolve() == VENV.resolve()
import sympy
assert Path(sympy.__file__).resolve().is_relative_to((VENV/"lib/python3.12/site-packages").resolve())


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(name, value):
    with (ROOT/name).open("x") as stream:
        json.dump(value, stream, indent=2, sort_keys=True)
        stream.write("\n")


def progress(stage, **items):
    value = {"stage":stage, "worker_cpu_seconds":time.process_time()-START, **items}
    with (ROOT/"case-progress.jsonl").open("a") as stream:
        stream.write(json.dumps(value, sort_keys=True)+"\n")
    print(json.dumps(value, sort_keys=True), flush=True)


def rational_sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0


def quadratic_sign(x, y):
    """Sign of x+y sqrt(5), using an exact norm comparison."""
    sx, sy = rational_sign(x), rational_sign(y)
    if sx == 0:
        return sy
    if sy == 0 or sx == sy:
        return sx
    norm = x*x-5*y*y
    assert norm != 0
    return sx*rational_sign(norm)


class Radical:
    """Four rational coefficients, radical-index convolution multiplication."""
    __slots__ = ("c",)

    def __init__(self, coordinates):
        self.c = tuple(Fraction(v) for v in coordinates)
        assert len(self.c) == 4

    @classmethod
    def raw(cls, coordinates):
        value = object.__new__(cls)
        value.c = tuple(coordinates)
        return value

    def __bool__(self):
        return any(self.c)

    def __eq__(self, other):
        return isinstance(other, Radical) and self.c == other.c

    def __add__(self, other):
        return Radical.raw(a+b for a,b in zip(self.c, other.c))

    def __sub__(self, other):
        return Radical.raw(a-b for a,b in zip(self.c, other.c))

    def scale(self, scalar):
        return Radical.raw(a*scalar for a in self.c)

    def __mul__(self, other):
        # bit0 is sqrt(5), bit1 is sqrt(249). Repeated bits square out.
        out = [Fraction(0)]*4
        for i, a in enumerate(self.c):
            if not a:
                continue
            for j, b in enumerate(other.c):
                if b:
                    common = i & j
                    weight = (5 if common & 1 else 1)*(249 if common & 2 else 1)
                    out[i ^ j] += a*b*weight
        return Radical.raw(out)

    def sign(self):
        a,b,c,d = self.c
        sa, sb = quadratic_sign(a,b), quadratic_sign(c,d)
        if sa == 0:
            return sb
        if sb == 0 or sa == sb:
            return sa
        # Norm in Q(sqrt(5)) for A+B sqrt(249).
        x = a*a+5*b*b-249*c*c-1245*d*d
        y = 2*a*b-498*c*d
        sn = quadratic_sign(x,y)
        assert sn != 0
        return sa*sn


ZERO_R = Radical((0,0,0,0))
ONE_R = Radical((1,0,0,0))
LOWER = Radical((Fraction(3,8),Fraction(1,8),0,0))
UPPER = Radical((Fraction(21,48),0,Fraction(1,48),0))
WIDTH = UPPER-LOWER


def scalar(x):
    return Radical((x,0,0,0))


@lru_cache(maxsize=None)
def decoded(coordinates):
    return Radical(coordinates)


def decode_matrix(raw):
    return [[decoded(tuple(entry)) for entry in row] for row in raw]


def verify_factorization(entry, strict):
    """Verify supplied proof data; perform no LDL elimination."""
    matrix = decode_matrix(entry["matrix"])
    lower = decode_matrix(entry["LDL"]["lower_factor"])
    diagonal = [decoded(tuple(q)) for q in entry["LDL"]["pivots"]]
    size = len(matrix)
    assert len(lower) == len(diagonal) == size
    assert all(len(row) == size for row in matrix+lower)
    assert all(matrix[i][j] == matrix[j][i] for i in range(size) for j in range(size))
    for i in range(size):
        assert lower[i][i] == ONE_R
        assert all(not lower[i][j] for j in range(i+1,size))
        sign = diagonal[i].sign()
        assert sign >= 0
        if strict:
            assert sign > 0
    for i in range(size):
        for j in range(i+1):
            total = ZERO_R
            for k in range(j+1):
                total = total+(lower[i][k]*lower[j][k])*diagonal[k]
            assert total == matrix[i][j], ("LDLT_reconstruction",entry["k"],i,j)
    return matrix


u = sympy.Symbol("u")
FIELD = sympy.QQ.frac_field(u)
RING = FIELD.get_ring()
U = FIELD.from_sympy(u)
RF_ZERO, RF_ONE = FIELD.zero, FIELD.one
E = 16*U**2-12*U+1
N = 32*U**2-18*U+1
NVAL = N/E
AVAL = N/(16*U-6)
RVAL = NVAL/(NVAL-1)
FREE = [17,25,61,62,64,65,66,68,69,70,71,72,73,74,76,78,79,80]
DEGREES = [3,3,2,2,2,3,3,3,3,4,4,4,4,4,4,4,4,4]
SCALES = {"G0":[0,1,0,2,1,1,1],"G1":[1,2,2,2],"H0":[0,0,1,0],"H1":[1,2,1,1]}
EXPECTED_Q = {"G0":28,"G1":16,"H0":32,"H1":24}


@lru_cache(maxsize=None)
def parse(text):
    return FIELD.from_sympy(sympy.sympify(text, locals={"u":u}))


def polynomial(value):
    assert value.denom.degree() == 0
    return RING.from_sympy(FIELD.to_sympy(value))


def coefficients(poly):
    values = [Fraction(0)]*(max(0,int(poly.degree()))+1) if poly else [Fraction(0)]
    for monomial, value in poly.to_dict().items():
        values[monomial[0]] = Fraction(int(value.numerator), int(value.denominator))
    return tuple(values)


def evaluate(values, point):
    answer = ZERO_R
    for value in reversed(values):
        answer = answer*point+scalar(value)
    return answer


def anchor_equal(function, expected):
    denominator = evaluate(coefficients(function.denom), UPPER)
    assert denominator
    assert evaluate(coefficients(function.numer), UPPER) == expected*denominator


@lru_cache(maxsize=None)
def shifted_power_coefficients(values):
    """Horner expansion P(lower+width*t); independent of Bernstein formulas."""
    out = [ZERO_R]
    for value in reversed(values):
        new = [ZERO_R]*(len(out)+1)
        for j, coefficient in enumerate(out):
            new[j] = new[j]+coefficient*LOWER
            new[j+1] = new[j+1]+coefficient*WIDTH
        new[0] = new[0]+scalar(value)
        out = new
    while len(out)>1 and not out[-1]:
        out.pop()
    return tuple(out)


def bernstein_power_coefficients(values):
    """Coefficient of t^j is binomial(q,j) times the jth forward difference."""
    degree = len(values)-1
    differences = list(values)
    answer = []
    for j in range(degree+1):
        answer.append(differences[0].scale(comb(degree,j)))
        differences = [b-a for a,b in zip(differences,differences[1:])]
    return answer


def basis_words(alphabet):
    return [()]+[(i,) for i in range(alphabet)]+list(product(range(alphabet),repeat=2))


def label_word(word):
    labels = {}
    answer = []
    for item in word:
        if item not in labels:
            labels[item] = len(labels)
        answer.append(labels[item])
    return tuple(answer)


def pair_key(left,right,mark=None):
    answers = []
    for first,second in ((left,right),(right,left)):
        labels = {} if mark is None else {mark:0}
        encoded = []
        for word in (first,second):
            for item in word:
                if item not in labels:
                    labels[item] = len(labels)
                encoded.append(labels[item])
            encoded.append(-1)
        answers.append(tuple(encoded[:-1]))
    return min(answers)


def indices(marked):
    result = {}
    words = basis_words(6)
    for left in words:
        for right in words:
            key = pair_key(left,right,0 if marked else None)
            if key not in result:
                result[key] = len(result)
    return result


def concrete_word_rows():
    """Expand word-pair localizers directly; retain each canonical word once."""
    marked, ordinary = indices(True), indices(False)
    assert len(marked) == 59 and len(ordinary) == 22
    rows = {}
    def add(word,index,constant=0,n_coefficient=0):
        if word != label_word(word):
            return
        row = rows.setdefault(word,{})
        previous = row.get(index,(0,0))
        row[index] = (previous[0]+constant,previous[1]+n_coefficient)
    for left in basis_words(5):
        for right in basis_words(5):
            h = 59+ordinary[pair_key(left,right)]
            add(left[::-1]+right,h,n_coefficient=1)
            for pivot in range(5):
                word = left[::-1]+(pivot,)+right
                g = marked[pair_key(left,right,pivot)]
                add(word,g,constant=1)
                add(word,h,constant=-1)
    assert len(rows) == 76
    return rows


def main():
    assert (ROOT/"RUN-ATTEMPT.json").is_file()
    manifest = json.loads((ROOT/"FROZEN-MANIFEST.json").read_text())
    for filename, expected in manifest["sha256"].items():
        assert digest(ROOT/filename) == expected, filename
    cert = json.loads((ROOT/"INPUT-CERTIFICATE.json").read_text())
    assert digest(ROOT/"INPUT-CERTIFICATE.json") == "f4727ed67e787acb10208ca8fe7ea7a6c787cebfb117faf77df8647022843225"
    affine = json.loads((ROOT/"INPUT-AFFINE.json").read_text())
    raw_blocks = json.loads((ROOT/"INPUT-BLOCKS.json").read_text())
    endpoint = json.loads((ROOT/"INPUT-N5-CERTIFICATE.json").read_text())
    checkpoint = json.loads((ROOT/"INPUT-POLYNOMIAL-CHECKPOINT.json").read_text())
    assert WIDTH.sign()>0 and (LOWER-scalar(Fraction(1,2))).sign()>0 and (ONE_R-UPPER).sign()>0
    assert evaluate(coefficients(polynomial(E)),LOWER) == ZERO_R
    assert evaluate(coefficients(polynomial(24*U**2-21*U+2)),UPPER) == ZERO_R
    assert (LOWER.scale(48)-scalar(21)).sign()>0
    assert NVAL-5 == -2*(24*U**2-21*U+2)/E
    assert N == 2*E+6*U-1
    # E is increasing beyond lower; N>0 there; F5 increases to zero at upper.

    linear_roots = [Fraction(0),Fraction(1),Fraction(1,16),Fraction(1,2),Fraction(1,6),Fraction(1,8),Fraction(3,8)]
    factors = []
    for root in linear_roots:
        assert (LOWER-scalar(root)).sign() == (UPPER-scalar(root)).sign() != 0
        factors.append(polynomial(U-FIELD(root.numerator)/root.denominator))
    for expression in (U**2-15*U/16+FIELD(3)/32,U**2-17*U/16+FIELD(9)/64):
        poly = polynomial(expression)
        # A convex quadratic lies below the endpoint chord, hence is negative.
        assert evaluate(coefficients(poly),LOWER).sign()<0 and evaluate(coefficients(poly),UPPER).sign()<0
        factors.append(poly)
    factors.append(polynomial(E/16))
    seen_nonzero = set()
    def nonzero_on_interval(poly):
        key = coefficients(poly)
        if key in seen_nonzero:
            return
        assert poly
        rest = poly
        for factor in factors:
            while not rest.rem(factor):
                rest = RING.exquo(rest,factor)
        assert rest.degree() == 0 and rest, ("unproved_denominator_factor",key)
        seen_nonzero.add(key)

    slopes = [Fraction(value) for value in cert["rational_slopes"]]
    assert len(slopes) == 18 and all(abs(q)<=100 for q in slopes)
    assert affine["free_orbit_columns"] == endpoint["free_orbit_columns"] == raw_blocks["free_orbit_columns"] == FREE
    seed = [Fraction(value) for value in endpoint["raw_free_coordinates"]]
    assert len(seed) == 18
    free = [NVAL**(4-d)*(FIELD(f.numerator)/f.denominator/5**(4-d)+(1/NVAL-FIELD(1)/5)*FIELD(b.numerator)/b.denominator)
            for f,b,d in zip(seed,slopes,DEGREES)]
    def substitute(row):
        assert len(row) == 19
        return sum((parse(text)*value for text,value in zip(row,free+[RF_ONE]) if text != "0"),RF_ZERO)
    orbit = [parse(text) for text in cert["orbit_functions"]]
    assert len(orbit) == len(affine["solution_matrix_rows"]) == 81
    for i, row in enumerate(affine["solution_matrix_rows"]):
        assert substitute(row) == orbit[i], ("orbit_affine_reconstruction",i)
        nonzero_on_interval(orbit[i].denom)
        c,b = endpoint["orbit_coordinates"][i]
        anchor_equal(orbit[i],Radical((c,0,b,0)))
    assert [orbit[i] for i in FREE] == free, "actual_free_orbits_match_ansatz_coordinates"
    target = -NVAL*(NVAL-1)*(NVAL-2)*(NVAL-3)*(NVAL-4)*(8*(2-RVAL)*AVAL**4-4*RVAL*(3-RVAL)*AVAL**3+RVAL**2*AVAL**2)
    for word, row in concrete_word_rows().items():
        actual = sum(((c+k*NVAL)*orbit[index] for index,(c,k) in row.items() if c or k),RF_ZERO)
        expected = target if not word else RF_ONE if len(word)==5 and len(set(word))==5 else RF_ZERO
        assert actual == expected, ("concrete_word_coefficient",word)
    progress("81_orbits_and_76_direct_word_coefficients_checked")

    blocks = {}
    records = {row["name"]:row for row in raw_blocks["blocks"]}
    assert set(records) == {"G0","G1","G2","G3","H0","H1","H2","H3"}
    for name, record in records.items():
        size = record["size"]
        values = [substitute(row) for row in record["affine_entry_rows"]]
        assert len(values) == size*size
        blocks[name] = [values[i*size:(i+1)*size] for i in range(size)]
        assert all(blocks[name][i][j] == blocks[name][j][i] for i in range(size) for j in range(size))
        for value in values:
            nonzero_on_interval(value.denom)
    ell = NVAL-(NVAL-2)*AVAL
    beta = (NVAL-2)*AVAL/(NVAL-1)
    gamma = AVAL*(2*(NVAL-2)*AVAL-NVAL)/(NVAL-1)
    assert gamma == AVAL*4*NVAL*(1-U)/((16*U-6)*(NVAL-1))
    kernels = {"G0":[[RF_ONE,ell,beta,ell**2,beta*ell,beta*ell,beta*ell,gamma]],
               "G1":[[RF_ONE,AVAL,AVAL,ell,AVAL,RF_ZERO],[RF_ZERO,NVAL-1,-(NVAL-1),RF_ZERO,RF_ZERO,RF_ONE]]}
    kernel_rows = 0
    for name, vectors in kernels.items():
        for vector in vectors:
            for row in blocks[name]:
                assert sum((a*b for a,b in zip(row,vector)),RF_ZERO) == RF_ZERO
                kernel_rows += 1
    assert kernel_rows == 20
    assert records["G0"]["retained_principal_indices"] == list(range(7))
    assert records["G1"]["retained_principal_indices"] == list(range(4))
    # Deleted-kernel projections have determinants gamma and a respectively;
    # both positive since lower<u<upper<1, n>=5, a>0, 16u-6>0.
    for name, expected in (("G2",(-1024*U**2+1088*U-144)/(8*U-3)),("H2",(-1024*U**2+960*U-96)/(8*U-3))):
        assert blocks[name] == [[expected]]
        # Concave numerator is above its positive endpoint chord.
        assert evaluate(coefficients(expected.numer),LOWER).sign()>0
        assert evaluate(coefficients(expected.numer),UPPER).sign()>0
        assert evaluate(coefficients(expected.denom),LOWER).sign()>0
        assert coefficients(expected.numer)[2] < 0
    assert blocks["G3"] == blocks["H3"] == [[RF_ZERO]]
    progress("kernels_scalars_and_denominators_checked",kernel_rows=kernel_rows)

    polynomials = {record["name"]:record for record in checkpoint["blocks"]}
    certificates = {record["name"]:record for record in cert["coefficient_certificates"]}
    assert set(polynomials) == set(certificates) == set(SCALES)
    all_checks = []
    total_matrices = 0
    for name in SCALES:
        record, proposal = polynomials[name],certificates[name]
        h = SCALES[name]
        size = len(h)
        keep = records[name]["retained_principal_indices"]
        assert keep == list(range(size)) == record["retained_indices"]
        assert record["h"] == h and record["removed_common_E_power"] == 0
        assert proposal["bernstein_degree"] == EXPECTED_Q[name] == record["degree"]+4
        q = EXPECTED_Q[name]
        entries = proposal["coefficients"]
        assert len(entries) == q+1 and [item["k"] for item in entries] == list(range(q+1))
        clearing = parse(record["denominator"])
        assert clearing.denom.degree() == 0
        nonzero_on_interval(polynomial(clearing))
        matrices = []
        for k, entry in enumerate(entries):
            assert len(entry["matrix"]) == size
            matrices.append(verify_factorization(entry,strict=(k==q)))
            total_matrices += 1
        for i in range(size):
            for j in range(i+1):
                raw = blocks[name][keep[i]][keep[j]]
                normalized = raw*NVAL**(h[i]+h[j]-4)*clearing**2
                p = polynomial(normalized)
                expected = list(shifted_power_coefficients(coefficients(p)))
                assert len(expected) <= q+1
                expected += [ZERO_R]*(q+1-len(expected))
                actual = bernstein_power_coefficients([matrix[i][j] for matrix in matrices])
                assert actual == expected, ("independent_polynomial_reconstruction",name,i,j)
        all_checks.append({"block":name,"coefficient_matrices":q+1,"size":size,
                           "exact_LDLT_reconstruction":True,"exact_field_signs":True,
                           "independent_Horner_and_forward_difference_polynomial_identity":True})
        progress("block_replayed",block=name,coefficient_matrices=q+1)
    assert total_matrices == 104
    write("RESULT.json",{"status":"COMPLETED_EXACT_GATE","all_checks":"PASS",
          "scientific_verdict":"INDEPENDENT_CERTIFICATE_CHECK_CONDITIONAL_ON_REPRESENTATION_CONTRACTION_BRIDGE",
          "certificate_sha256":digest(ROOT/"INPUT-CERTIFICATE.json"),
          "source_sha256":digest(Path(__file__)),"worker_cpu_seconds":time.process_time()-START,
          "matrices_checked":104,"orbit_functions_checked":81,"concrete_word_patterns_checked":76,
          "kernel_rows_checked":20,"scalar_blocks_checked":4,"blocks":all_checks,
          "zero_free_factor_checks":len(seen_nonzero),
          "independence":{"field_arithmetic_and_signs":"new implementation",
                          "PSD":"supplied factorization independently reconstructed; no elimination rerun",
                          "polynomial":"Horner composition versus Bernstein forward differences",
                          "word_coefficients":"direct word-pair localizer expansion",
                          "shared_engine":"SymPy QQ(u) exact polynomial arithmetic",
                          "representation_block_contractions":"REUSED RAW MAP; SEPARATE BRIDGE REQUIRED"},
          "scope":"integer n>=5 matrix tuples; continuous polynomial interval; no equality-witness replay",
          "solver_calls":0,"new_roundings":0,"discovery_imports":0,"no_human_or_priority_claim":True})


if __name__ == "__main__":
    try:
        main()
    except BaseException as error:
        write("WORKER-FAILURE.json",{"status":"INCOMPLETE_NO_RESULT","error":type(error).__name__+": "+str(error),
              "worker_cpu_seconds":time.process_time()-START,"retry_permitted":False})
        traceback.print_exc()
        raise
