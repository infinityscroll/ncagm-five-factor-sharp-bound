# Independent all-n block-map reconstruction

Fixed target: the final margin certificate, SHA256
f4727ed67e787acb10208ca8fe7ea7a6c787cebfb117faf77df8647022843225.
No candidate fitting, rounding, solver, imports of discovery code or new target.

Rebuild the eight complete representation contractions independently using
explicit sparse vectors in the full word basis at n=5,6,7,8,9. For each of the
81 upper-triangular entries and each orbit coordinate, reconstruct its degree
at most four polynomial by exact rational Lagrange interpolation. The degree
bound is analytical: each pair of words has at most four free labels, each
equality pattern contributes a falling factorial of order at most four, and
the representative coefficients depend only on fixed anchors and equality.
All representatives and orbit types exist for n>=5, including the marked
four-label switch. Therefore five values uniquely determine these polynomial
maps for all n>=5. This is not positivity inferred from samples.

Substitute n=(32u²-18u+1)/(16u²-12u+1), multiply the new maps by the final81
orbit rational functions and compare every resulting entry in Q(u) with the
saved affine block evaluated at those same free orbit coordinates. Check the
lower triangular entries too. Do not reverse either word in Gram contraction.
This separately validates the previously reused block-entry arrays for the
actual fixed candidate. It does not regenerate the entire affine solution,
which is unnecessary once the final original word identities pass.

One execution under the previously reviewed single-use wait4 supervisor,
unchanged30 workerCPU/45wall/1GiB sampled-and-final RSS bounds. No external
resources, no paid compute, no publication. Source preparation is not a run;
root and separate static review precede execution. Any incomplete run is not
acceptance evidence. The independently written PSD/word verifier and the
analytical representation/attainment proof remain separate obligations.
