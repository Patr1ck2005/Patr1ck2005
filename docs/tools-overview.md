# From numerical observations to inspectable results

[简体中文](tools-overview.zh-CN.md) · [Project directory](../README.md)

Research software is useful when another person can understand its inputs, reproduce a small result and see where interpretation is still required. This collection focuses on that practical handoff across photonics, scientific computing and visualization.

The four shared libraries have deliberately separate jobs. **campaign-data** checks files and coverage before analysis. **eigenmode-analysis** organizes numerical candidates along paths and parameter graphs, preserving missing observations and assignment diagnostics. **plot-foundation** renders explicit plotting specifications. **plot-workflows** connects analysis outputs to reusable views. The combined example generates its own mathematical data and checks the results it claims.

![A computed synthetic workflow](https://raw.githubusercontent.com/Patr1ck2005/plot-workflows/main/docs/assets/showcase/hero.png)

These curves illustrate a software workflow. They are independently defined synthetic quantities, not measured or simulated evidence for a photonic device. Tracking labels also require physical interpretation: a numerically continuous branch does not establish a unique physical identity.

Separate projects explore scalar optical propagation, parameterized GDS layouts, interactive wave fields and games. Their repository pages distinguish runnable software, prototypes, historical work and attributed upstream forks. The [full directory](../README.md) keeps those differences visible.

For a first try, use [the combined example](https://github.com/Patr1ck2005/plot-workflows#run-the-end-to-end-example) in a fresh environment. Its requirements select the compatible stable releases and Matplotlib 3.10.9. The independent eigenmode 0.3.1 grouping line belongs in a separate environment. Each repository contains its own licensing, source and compatibility information.

Useful feedback starts with three questions: Could you run the example? What real task would you try next? Which missing capability prevents that task? A small shareable input and a clearly specified output are more useful than a broad platform request.

Private research orchestration, compute-fleet operations and current experiment-specific modules remain internal. Public examples demonstrate bounded capabilities without exposing ongoing research. These projects are available for concrete discussion about numerical optics, analysis and research tools; no commercial service or production support commitment is implied.
