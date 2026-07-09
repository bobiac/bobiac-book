# 07 - <i class="fa-solid fa-ruler-combined"></i> From Images to Data

An image may look like a result, but it is not data. What we actually have is an **array of intensity values**, and what we need to answer a biological question is a **table of measurements**. Measurement and quantification is the process of turning one into the other — going from images, to numbers, to plots.

Whenever we describe an image, we are already measuring it. Saying that one cell is *bigger*, *brighter*, or *more clustered* than another is an informal measurement. The goal of quantification is to make these observations **explicit, standardized, and comparable**, so that our conclusions rest on numbers rather than impressions.

Turning an image into data is not automatic; it is a series of **choices**, and every one of them is driven by your **scientific question**. The first choice is which **objects** to measure. The same image can be described in terms of whole fields of view, cell groups, single cells, nuclei, or subcellular puncta. These objects are nested within one another, and the scale we choose determines what we are able to ask — for example, how many puncta there are per cell, or how many cells there are per cluster. The second choice is which **properties** to measure. Most measurements fall into four broad categories — **count**, **location**, **intensity**, and **shape** — and the quantities we ultimately care about are often *derived* by combining them, such as intensity divided by area to give a mean intensity, or count divided by area to give a density.

The outcome of these choices is a **table**: one row per object, one column per measurement. This table is our data, and everything downstream — plots, statistics, and conclusions — is built on it.

Finally, it is important to treat these numbers with healthy suspicion. Both the segmentation that defines the objects and the measurements taken from them can be wrong, so they should be validated — for instance by checking histograms for implausible outliers and by overlaying measured values back onto the image. The analysis built on the data deserves the same care: cells within a single well are not independent replicates, and treating them as such will artificially inflate statistical significance. It also helps to remember what imaging is and is not good for. It is uniquely powerful for **spatial** and **temporal** questions, but for questions of absolute concentration or molecular identity, methods such as flow cytometry, qPCR, or sequencing are often better suited.

## Slides

<a
    class="custom-button custom-download-button" href="../../pdfs/07_measurement_and_quantification/bobiac26_intro_to_measurements.pdf" download> <i class="fas fa-download"></i> Download the Slides
</a>

<div align="center">
  <iframe class="custom-pdf-frame-169" src="../../pdfs/07_measurement_and_quantification/bobiac26_intro_to_measurements.pdf"> </iframe>
</div>
