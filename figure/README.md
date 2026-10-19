# Optional private figure: sharp five-factor lower endpoint

Presentation only. This evaluates the already accepted closed formula for
integer n=5,...,30; it is not a new experiment, proof, optimization, or novelty
check. Source and CSV accompany both raster and vector figures.

For PSD A_i with sum A_i<=nI, let D5(A) be the ordered distinct-five-index
product sum and (n)_5=n(n-1)(n-2)(n-3)(n-4). The plotted normalized endpoint is

    D5(A)/(n)_5 >= -kappa5(n) I,
    r=n/(n-1), Delta=sqrt(20n^2-60n+49),
    a=n(6n-9+Delta)/[16(n-1)(n-2)],
    kappa5(n)=a^2[r(3-r)a-r^2/2].

The asymptote is -(11+5sqrt(5))/64. The -1 line is the prior conjecture
benchmark, not an asserted sharp bound. Integer values are shown as dots;
the connector is a visual guide and makes no additional noninteger claim.

The certificate is the independently accepted scientific input, not a
dependency required to reproduce the image:
`../stages/block_map/CERTIFICATE.json`, SHA256
`f4727ed67e787acb10208ca8fe7ea7a6c787cebfb117faf77df8647022843225`.
The parameterization and theorem bridge are documented in
`../reviews/THEOREM-BRIDGE-AUDIT.md`.

Run with Python 3 and matplotlib:

    python plot_endpoint.py

The formula is evaluated at 80-digit Decimal precision; CSV columns retain
50 decimal places. Rendering uses float coordinates. The source uses no
solver, network, credential, paid service, or old workspace import. PNG is
1840x1160 pixels; SVG retains vector paths and editable text. The figure
explicitly labels the work AI-assisted and unrefereed. No publication is
authorized or performed by creating it.
