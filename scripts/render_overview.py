"""Render independent mathematical examples; no research files are read.

Run with Python + NumPy + Matplotlib. Assets are written relative to this file.
This script does not benchmark or claim to call the portfolio's libraries.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    output = root / "docs" / "assets"
    output.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({
        "font.family": "Arial", "font.size": 10,
        "axes.labelsize": 10, "xtick.labelsize": 9, "ytick.labelsize": 9,
        "axes.linewidth": .65, "xtick.direction": "in", "ytick.direction": "in",
        "svg.fonttype": "none", "figure.facecolor": "#f8f8f4",
        "axes.facecolor": "#ffffff", "text.color": "#182b40",
        "axes.labelcolor": "#182b40", "xtick.color": "#364a60", "ytick.color": "#364a60",
    })
    fig = plt.figure(figsize=(10.6667, 8), dpi=150)
    grid = fig.add_gridspec(2, 2, left=.09, right=.90, bottom=.16, top=.84,
                          height_ratios=[1.1, 1], hspace=.50, wspace=.32)
    ax_field = fig.add_subplot(grid[0, :])
    ax_branch = fig.add_subplot(grid[1, 0])
    ax_coverage = fig.add_subplot(grid[1, 1])
    fig.text(.09, .943, "PHOTONICS  /  SCIENTIFIC COMPUTING", fontsize=16, weight="bold")
    fig.text(.09, .903, "Optical fields, analytical branches, and inspectable data", fontsize=11)

    x = np.linspace(-3, 3, 361)
    y = np.linspace(-1.25, 1.25, 151)
    xx, yy = np.meshgrid(x, y)
    field = np.exp(-.13 * xx**2 - 1.5 * yy**2) * (np.exp(2.6j * xx) + .65*np.exp(-2.6j*xx + .7j))
    intensity = np.abs(field)**2
    intensity /= intensity.max()
    image = ax_field.imshow(intensity, extent=[x.min(),x.max(),y.min(),y.max()],
                            origin="lower", cmap="magma", vmin=0, vmax=1, aspect="auto")
    ax_field.set(xlabel="x / arbitrary length", ylabel="y / arbitrary length")
    ax_field.set_title("(a) Scalar-wave illustration", loc="left", fontsize=11, pad=8)
    colour = fig.add_axes([.915,.55,.012,.225])
    fig.colorbar(image,cax=colour,label="Normalized intensity")

    k = np.linspace(-1,1,81)
    branch_a = 1.4 + .45*k + .20*k*k
    branch_b = 1.6 - .40*k + .05*k*k
    mask = (k < .12) | (k > .36)
    ax_branch.plot(k,branch_a,color="#0969b1",lw=1.7,label="Analytical branch A")
    ax_branch.plot(k[mask],branch_b[mask],".",color="#da4d31",ms=3.7,label="Sampled branch B")
    # Do not connect across the intentionally absent interval.
    for segment in (k < .12, k > .36):
        ax_branch.plot(k[segment],branch_b[segment],color="#da4d31",lw=1)
    ax_branch.set(xlabel="Parameter k",ylabel="Dimensionless value",xlim=(-1,1))
    ax_branch.set_title("(b) Known branches; explicit missing samples",loc="left",fontsize=10,pad=8)
    ax_branch.legend(loc="upper center",fontsize=8,frameon=False)

    coverage = np.ones((8,12),dtype=int)
    coverage[2:4,5:8] = 0
    coverage[6,2:5] = 2
    from matplotlib.colors import ListedColormap, BoundaryNorm
    cmap = ListedColormap(["#e9edf1","#187eaa","#ec8c46"])
    norm = BoundaryNorm([-.5,.5,1.5,2.5],3)
    ax_coverage.imshow(coverage,origin="lower",cmap=cmap,norm=norm,aspect="auto",
                       extent=[-.5,11.5,-.5,7.5],interpolation="nearest")
    ax_coverage.set(xlabel="Scan coordinate 1",ylabel="Scan coordinate 2",xticks=[0,4,8,11],yticks=[0,3,7])
    ax_coverage.set_title("(c) Synthetic scan coverage",loc="left",fontsize=10,pad=8)
    from matplotlib.patches import Patch
    ax_coverage.legend(handles=[Patch(color=c,label=l) for c,l in zip(cmap.colors,["Missing","Present","Repeated"])],
                       loc="upper center",bbox_to_anchor=(.5,-.25),ncol=3,fontsize=8,frameon=False)
    fig.text(.09,.025,"INDEPENDENT SYNTHETIC EXAMPLES  •  No unpublished research data",fontsize=9,color="#596a7b")
    for suffix in ("png","svg"):
        fig.savefig(output / f"portfolio-overview.{suffix}",dpi=150,facecolor=fig.get_facecolor())
    plt.close(fig)
    assets=[]
    for path in sorted(output.glob("portfolio-overview.*")):
        assets.append({"path":path.relative_to(root).as_posix(),"sha256":hashlib.sha256(path.read_bytes()).hexdigest()})
    manifest={
        "source_kind":"independent synthetic numerical illustration",
        "source":"scripts/render_overview.py","seed":None,
        "read_external_data":False,
        "method":"Analytical scalar field and two polynomial branches; explicitly constructed coverage matrix.",
        "not_a_claim":"Not Maxwell simulation, unpublished research, tracking-algorithm output, or performance benchmark.",
        "versions":{"numpy":np.__version__,"matplotlib":matplotlib.__version__},
        "canvas":{"width_px":1600,"height_px":1200,"aspect":"4:3"},
        "assets":assets,
    }
    (output / "manifest.json").write_text(json.dumps(manifest,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"generated":assets,"missing_samples":int((~mask).sum()),"coverage_missing":int((coverage==0).sum()),"coverage_repeated":int((coverage==2).sum())},indent=2))


if __name__ == "__main__":
    main()
