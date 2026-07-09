# 08 - <i class="fa-solid fa-circle-nodes"></i> Introduction to Spatial Analysis

Spatial analysis is about questions that can only be answered by knowing **where** things are: whether objects are organized or random, which objects are near which, how crowded a region is, and whether two kinds of object tend to coincide. Our eyes are good at spotting these patterns, but intuition is not a measurement. The goal of spatial analysis is to turn "that looks clustered" into a number we can compare, test, and trust.

The starting point is deceptively bare: all we truly measure is a set of **coordinates**. Everything we care about, such as density, clustering, co-localization, is a *relationship* between objects, and relationships are not explicitly stored in the coordinates themselves. They have to be constructed. This makes spatial analysis a sequence of deliberate decisions, and as always those decisions follow from your scientific question.

Three ideas underpin most spatial analyses.

**Relationships must be defined.** Before we can measure how objects relate, we have to decide what "related" means — the closest object, every object within some distance, objects that share a border, or objects the tissue itself connects. Each definition encodes an assumption about the biology, and different definitions can lead to different conclusions from the same points.

**A pattern is only meaningful against an expectation.** Calling something "clustered" or "colocalized" is incomplete until we answer *compared to what?* The reference is a **null distribution**: a version of the data that keeps the features we want to control for (such as the number of objects and the shape of the region) but scrambles the one we are testing (their arrangement). Comparing the real pattern to many such randomized versions is what separates a genuine signal from something that would happen by chance. Choosing how much to scramble — gently or aggressively — is itself a modelling choice.

**Measurements summarize relationships into numbers.** Once relationships and a null are in place, we can quantify them: how far objects sit from their neighbours, whether they are closer or farther than random, and at which spatial scale any structure appears. These summaries are what ultimately answer the question.

Finally, it is worth being clear about what spatial analysis *cannot* do. It can show that objects are close, but not that they interact; it can reveal that a pattern exists, but not what caused it; and its answers usually depend on the scale you choose to look at. Turning spatial correlation into mechanism is the job of experimental design, not of the analysis alone.

## Slides

<a
    class="custom-button custom-download-button" href="../../pdfs/08_colocalization/bobiac26_spatial_analysis.pdf" download> <i class="fas fa-download"></i> Download the Slides
</a>

<div align="center">
  <iframe class="custom-pdf-frame-169" src="../../pdfs/08_colocalization/bobiac26_spatial_analysis.pdf"> </iframe>
</div>
