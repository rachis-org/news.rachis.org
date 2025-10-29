# Announcing `rachis`, a rebrand of the QIIME 2 Framework (Q2F)

As you may or may not know, the QIIME 2 microbiome data science platform is built on what we call the QIIME 2 Framework (Q2F).
Q2F provides the general purpose functionality that gives QIIME 2 a lot of its power, including data provenance tracking, the Python API, the artifact class system, the parallel computing framework, the artifact cache, and more.[^q2f-code]

QIIME 2's amplicon data analysis functionality, for example, builds on Q2F, providing domain-specific analysis tools in the form of plugins.
Other tools do as well.
Q2F serves as the foundation for [MOSHPIT](https://moshpit.qiime2.org) (for metagenome annotation, assembly, and data analysis; formerly referred to as the QIIME 2 metagenome distribution), as well as pathogen genomics tools in our pathogenome distribution, and in stand-alone tools like [genome-sampler](https://genome-sampler.readthedocs.io).

The distinction between "QIIME 2" and the "QIIME 2 Framework" is often lost however, so potential users of Q2F don't realize that it has generalized functionality that extends beyond microbiome amplicon analysis.
Stemming from Q2F's ability to enhance bioinformatics reproducibility, accessibility, and scalability, we are keen to support biological data science beyond microbiome amplicon analysis.
To facilitate movement in that direction, and to better disambiguate our different tools, we are beginning the process of rebranding Q2F as a distinct entity from QIIME 2.

## Q2F will be rebranded as `rachis`

Today we're announcing a rebrand of Q2F as `rachis`.
The name `rachis` (pronounced ray-kiss) is derived from the ancient Greek ῥάχις [rhákhis], meaning “spine”; in plants, a rachis is the central axis of a compound structure, such as the central stem of a compound leaf, flower, or fruit cluster (e.g., the stem of a grape cluster).
Analogously, the rachis framework will serve as a central axis and platform for diverse biological data science tools to drive scientific advances, including QIIME 2, MOSHPIT, and more.
These tools benefit from the centralized structural features of the rachis framework, provided as software distributions that provide the necessary functionality for a given biological domain.
As a user, you do not directly interact with the rachis framework itself but benefit from the centralized, general features, and enhanced accessibility that it provides (much as when someone eats grapes they do not eat the rachis, but may appreciate how much easier it is to enjoy a cluster of grapes than, say, a pomegranate) [](#f-grapefruit).

```{figure} https://imgs.xkcd.com/comics/fuck_grapefruit.png
:label: f-grapefruit
:alt: XKCD comic plotting ease of use versus tastiness of fruits.
:align: left

Fruits offered on a rachis framework offer superior usability, accessibility, and tastiness. Re-used under CC-BY-NC-2.5 from: https://xkcd.com/388/
```

## So, what is "QIIME 2"?

QIIME 2 will now be used to exclusively refer to what we've previously called the *QIIME 2 amplicon distribution*.
This is what most users already think of QIIME 2 as, so this will allow for more clarity in our documentation and in describing what QIIME 2 and `rachis` each do.

## What changes will users need to make?

None!

For users of the QIIME 2 amplicon distribution, nothing will change.
You'll be able to continue to use QIIME 2 as you always have.
We also don't plan to change the name of the [QIIME 2 Forum](https://forum.qiime2.org), though we may move some categories around to begin providing more support for other tools like MOSHPIT that build on `rachis`.
You may see some changes on other websites, like [QIIME 2 View](https://view.qiime2.org), to reflect the new branding, but you can expect minimal (if any) disturbance to your workflow (e.g., old URLs will redirect as necessary).

## What changes will developers need to make?

None! (Though you can optionally update your `import` statements.)

The [`qiime2`](https://github.com/qiime2/qiime2) Python package will be renamed `rachis`, and import paths will change such that their canonical form will include `rachis` in place of `qiime2`.
For example, a statement like `import qiime2.Artifact` will change to `import rachis.Artifact`.
We'll redirect import statements that include `qiime2`, such that this change will be optional.

## Timeline

We expect to transition the `qiime2` Python package in time for the 2026.1 release (scheduled for January of 2026).
Documentation changes will follow in *Developing with QIIME 2* and *Using QIIME 2* later in 2026, as will changes to websites and any reorganization on the QIIME 2 Forum.
As mentioned above, users and developers should barely notice this change, but our hope is that it improves clarity in our documentation and helps in our development of future funding for the projects.

## `rachis` leadership

The `rachis` project is led by:
- [Greg Caporaso](https://forum.qiime2.org/u/gregcaporaso/summary), the `rachis` Program Manager;
- [Nick Bokulich](https://forum.qiime2.org/u/nicholas_bokulich/summary), the `rachis` Director of Research;
- [Evan Bolyen](https://forum.qiime2.org/u/ebolyen/summary), the `rachis` Director of Engineering;
- and [Liz Gehret](https://forum.qiime2.org/u/lizgehret/summary), the `rachis` Director of Distribution.

Our intention is to expand this leadership board by onboarding new Directors for additional program areas as the rachis ecosystem expands.

## Onward!

Thanks for joining us on this journey, and thanks as always for your interest in QIIME 2!
We expect this change will usher in an exciting new era for the project, and we have lots of exciting features planned including new tools, interfaces, and -omics domains.

See you on the QIIME 2 Forum! 🍇

[^q2f-code]: The Q2F codebase is that found at https://github.com/qiime2/qiime2.
