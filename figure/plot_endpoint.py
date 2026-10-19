#!/usr/bin/env python3
"""Presentation only: plot the accepted sharp five-factor lower formula.

Requires Python 3 and matplotlib. No solver, fitting, sampling experiment,
network access, or old-workspace dependency. Run: python plot_endpoint.py

Normalization: A_i >= 0, sum A_i <= n I, and
  D5(A)/(n)_5 >= -kappa5(n) I, for integers n >= 5.
The CSV evaluates the closed formula with 80-digit Decimal arithmetic;
float conversion is used only for rendering. The CSV is not proof evidence.
"""
from csv import DictWriter
from decimal import Decimal, localcontext
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


def endpoint(n: int) -> Decimal:
    """Return -kappa5(n) from the accepted larger stationary branch."""
    if n < 5:
        raise ValueError("The stated theorem domain is integer n >= 5")
    x = Decimal(n)
    r = x / (x - 1)
    delta = (20 * x * x - 60 * x + 49).sqrt()
    a = x * (6 * x - 9 + delta) / (16 * (x - 1) * (x - 2))
    kappa = a * a * (r * (3 - r) * a - r * r / 2)
    return -kappa


def main() -> None:
    out = Path(__file__).resolve().parent
    ns = list(range(5, 31))
    with localcontext() as context:
        context.prec = 80
        lower = [endpoint(n) for n in ns]
        asymptote = -(Decimal(11) + 5 * Decimal(5).sqrt()) / 64
        rows = [
            {
                "n": n,
                "kappa5_normalized": format(-value, ".50f"),
                "sharp_lower_endpoint": format(value, ".50f"),
                "asymptotic_lower_endpoint": format(asymptote, ".50f"),
                "prior_conjecture_benchmark": "-1",
            }
            for n, value in zip(ns, lower)
        ]
    with (out / "sharp-m5-endpoint.csv").open("w", newline="") as stream:
        writer = DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 10,
        "axes.labelsize": 11,
        "axes.edgecolor": "#7A828B",
        "axes.linewidth": 0.7,
        "xtick.color": "#47515C",
        "ytick.color": "#47515C",
        "svg.fonttype": "none",
        "savefig.facecolor": "white",
    })
    fig, ax = plt.subplots(figsize=(9.2, 5.8))
    fig.subplots_adjust(left=0.11, right=0.97, bottom=0.25, top=0.80)
    fig.suptitle("Sharp five-factor lower endpoint", fontsize=18,
                 fontweight="semibold", x=0.11, ha="left", y=0.96)
    fig.text(0.11, 0.865,
             r"Bound for $D_5(A)/(n)_5$ with $A_i\succeq0$ and "
             r"$\sum_i A_i\preceq nI$; integers $n\geq5$",
             fontsize=11, color="#47515C", ha="left")

    values = [float(value) for value in lower]
    ax.plot(ns, values, color="#A0ABB6", linewidth=1.1,
            linestyle=(0, (2.5, 3.5)), zorder=2)
    points = ax.scatter(ns, values, color="#184D72", s=26, zorder=4,
                        label="Sharp endpoint at integer n")
    limit = ax.axhline(float(asymptote), color="#AF762B", linewidth=1.35,
                      linestyle=(0, (6, 4)), zorder=1,
                      label=r"Asymptote: $-(11+5\sqrt{5})/64$")
    benchmark = ax.axhline(-1, color="#6A7178", linewidth=1.1,
                          linestyle=(0, (4, 2, 1, 2)), zorder=1,
                          label="−1: prior conjecture benchmark")
    ax.set_xlim(4.4, 30.6)
    ax.set_ylim(-1.27, -0.27)
    ax.set_xticks([5, 10, 15, 20, 25, 30])
    ax.xaxis.set_minor_locator(MultipleLocator(1))
    ax.set_yticks([-1.2, -1.0, -0.8, -0.6, -0.4])
    ax.set_xlabel(r"$n$ (number of matrices)", labelpad=9)
    ax.set_ylabel(r"Normalized endpoint $-\kappa_5(n)$", labelpad=9)
    ax.grid(axis="y", color="#E9EDF0", linewidth=0.8, zorder=0)
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(axis="both", which="major", length=4, width=0.7)
    ax.tick_params(axis="x", which="minor", length=2, width=0.5,
                   color="#A7AFB7")
    ax.legend(handles=[points, limit, benchmark], loc="lower right",
              frameon=True, facecolor="white", edgecolor="none", framealpha=1,
              fontsize=10, labelspacing=0.8,
              borderaxespad=1.0, handlelength=2.6)

    fig.text(0.11, 0.13,
             "Points are discrete integer values. The dashed connector is a visual guide only.",
             fontsize=9, color="#58626D", ha="left")
    fig.text(0.11, 0.075,
             "AI-assisted, unrefereed; exact certificate supplied",
             fontsize=9, color="#58626D", ha="left")
    fig.savefig(out / "sharp-m5-endpoint.png", dpi=200)
    fig.savefig(out / "sharp-m5-endpoint.svg")
    plt.close(fig)
    print("Created sharp-m5-endpoint.csv, sharp-m5-endpoint.png, sharp-m5-endpoint.svg")


if __name__ == "__main__":
    main()
