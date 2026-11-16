(announcing-gut-to-soil-tutorial)=
# Learn QIIME 2 with the all-new gut-to-soil tutorial

I'm excited to share the all new [*Gut-to-Soil Microbiome Axis Tutorial*](https://amplicon-docs.qiime2.org/en/stable/tutorials/gut-to-soil/), which went live with the [2026.10 release of QIIME 2](https://forum.qiime2.org/t/qiime-2-2026-10-is-now-available/34362).
This is intended to be the primary entry point for new QIIME 2 users to learn an amplicon analysis workflow, and it allows you to follow along with a full marker gene analysis on real microbiome data from a recent study ([Meilander *et al.* (2025)](https://doi.org/10.1093/ismeco/ycaf089)) to illustrate how you can use QIIME 2 in your own work.

There are a few exciting new features that I'd like to highlight here.

First, as the tutorial works from demultiplexed sequencing data through statistics and visualizations, it tracks a constructed data set through the analysis in 21 figures, **allowing you to visualize the data as it moves through the workflow**.
That is often difficult to achieve because the data we're working with is too large to view directly, but it is hugely helpful for understanding an analysis workflow.
For example, Figure 11 presents three feature tables: an original and two [rarefied](#term-rarefaction) variants of it.
If you ever find yourself wondering something like *What does this `FeatureTable[Frequency]` thing that the QIIME 2 documentation is referring to actually look like?*, this tutorial will help you understand!

```{figure} ./_static/images/gut-to-soil-even-sampling.jpeg
:alt: Figure 11 of the gut-to-soil tutorial, Rarefying feature tables to achieve an even sampling depth across all samples
:align: center
:width: 60%
```

Next, the tutorial provides 17 exercises and solutions that will guide your exploration of the data and help you test your understanding as you go.
These cover topics from sequence quality control to reporting analysis reproducibility.
Some of these will also push you to write new QIIME 2 commands by adapting ones that you've already seen:

```{figure} ./_static/images/gut-to-soil-exercise-15.png
:alt: Exercise 15 of the gut-to-soil tutorial, Perform ANCOM-BC2 on genera, instead of ASVs
:align: center
```

New functionality is introduced throughout the tutorial, including [building a GTDB-based classifier using RESCRIPt](https://amplicon-docs.qiime2.org/en/stable/tutorials/gut-to-soil/#JpK7rHsmxb), [performing rarefaction-based diversity analysis with q2-boots](https://amplicon-docs.qiime2.org/en/stable/tutorials/gut-to-soil/#ds6e3w3hn8), [annotating QIIME 2 results](https://amplicon-docs.qiime2.org/en/stable/tutorials/gut-to-soil/#xMUqJ9Z5sH) (e.g., with a license or information about how to cite it when used), and [generating a QIIME 2 report which integrates multiple .qzv files into a single visualization](https://amplicon-docs.qiime2.org/en/stable/tutorials/gut-to-soil/#nQX4FhPpv6) (super convenient for publication and sharing with collaborators!).

And, when paired with the [QIIME 2 Workshop Docker Container](https://use.qiime2.org/en/stable/how-to-guides/use-the-workshop-container/), this is a great resource for running your own training events.
This container provides convenient functionality built-in, including:
- a JupyterLab server that provides a consistent interface to all workshop participants (regardless of their host operating system); and
- {term}`QIIME 2 View`, so your participants can double click on a `.qzv` file and have it open directly in their web browser.

When your workshop participants go home, they'll have a working installation of QIIME 2 on their computer that they can take with them to continue their learning or jump into their own data analysis.

Finally, this tutorial is currently in review for publication.
In addition to [the website](https://amplicon-docs.qiime2.org/en/stable/tutorials/gut-to-soil/), if you'd like the tutorial in PDF form you can access that through the pre-print: [*Microbiome marker gene analysis with QIIME 2: the "gut-to-soil microbiome axis" tutorial*](https://zenodo.org/records/23238754).
(Generally I recommend the website though as it is easier to copy/paste commands from and will be updated regularly with new versions of QIIME 2.)

Thanks to all of the co-authors on the pre-print for making this happen!
If you have any feedback, please feel free to [let us know](https://forum.qiime2.org/t/learn-qiime-2-with-the-all-new-gut-to-soil-tutorial/34387).

Happy QIIMEing!

💩 → 🌱
