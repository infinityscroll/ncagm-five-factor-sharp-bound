# Independent replay source prepared, not run

The worker is newly written and solver-free. It does not import, execute,
or reuse the discovery worker's field class, sign routine, LDL elimination,
word-coefficient routine, or polynomial transformation routine. It uses
SymPy only for rational polynomial arithmetic over Q(u). Supplied exact
LDL factors are proof data, checked by reconstructing every matrix entry;
the stored pass flags are not accepted as evidence.

The exact Bernstein-to-power formula uses forward differences. Independent
Horner substitution of the reconstructed normalized rational block supplies
the comparison power coefficients. The word coefficient equations are built
by explicit expansion of degree<=2 word-pair localizers, retaining one
canonical word representative per orbit. No point samples are used.

Reused inputs are the affine orbit functions, invariant-block contraction
map, n5 anchor, normalization metadata, and successful final certificate.
The source checks the affine point, all76 generated word equations, the
full equality kernels, zero-free denominators, the scalar blocks, and104
exact Bernstein matrices. It does not regenerate the representation map.
Root owns the independent map-regeneration gate in
`../overnight-ncagm-m5-independent-block-map-20261019`. The replay's result
explicitly remains conditional on that separate bridge and its mathematical
representation-completeness review. It does not independently replay the
known attaining matrix family.

The existing reviewed supervisor is copied byte-identically from the final
margin gate:30 worker CPU seconds,45 wall seconds,1GiB sampled/final RSS,
one use, explicit post-reap measured CPU rejection. No cap adequacy is
claimed without a run. Any incomplete run yields NO_RESULT; no alternate
candidate, retry or relaxed check is authorized here.

Preparation involved only reading, writing, copying/moving, diff/hash work.
No scientific code execution, imports, tests, syntax checking, solver,
package installation or new rounding occurred. Root must statically review
the source/manifest before separately authorizing any launch.

The initial requested directory already contained the preserved n5 replay.
All eight newly created files were moved into this fresh all-n directory;
none of the earlier n5 files was overwritten. See COLLISION-CLEANUP.txt.
