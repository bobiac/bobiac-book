# 05 - <i class="fa-solid fa-crosshairs"></i> Spot Detection

Many image analysis tasks require detecting small, **spot-like structures** in an image such as fluorescent beads, foci, or any other punctate signal like in fluorescence in situ hybridization (FISH).

There are **different ways to detect spots**, and how well they work depends a lot on the **quality of the data** (signal-to-noise ratio, background, spot density, variability in intensity and size, etc.). Classical approaches are based on simple image-processing operations, for example:

- **Local maxima detection** (e.g. [`peak_local_max`](https://scikit-image.org/docs/stable/api/skimage.feature.html#skimage.feature.peak_local_max) from `scikit-image`), which finds the brightest local peaks in the image, very similar to ImageJ's `Find Maxima`. It is fast and simple, but sensitive to noise and usually requires manual threshold tuning.
- **Laplacian of Gaussian (LoG) blob detection** (e.g. [`blob_log`](https://scikit-image.org/docs/stable/api/skimage.feature.html#skimage.feature.blob_log) from `scikit-image`), which detects blobs across a range of scales and can therefore handle spots of different sizes.

These classical methods work well on **clean, high-contrast data**, but they often struggle when the signal is weak, the background is uneven, or the spots are densely packed, and they typically need careful parameter tuning for each new dataset.

To overcome these limitations, **deep learning-based methods** have been developed that learn to detect spots directly from the data, making them more **robust** and **threshold-agnostic** across different imaging conditions.

In this tutorial, we will use [**Spotiflow**](https://weigertlab.org/spotiflow/index.html), a deep learning-based spot detection tool, to detect spots in 2D and 3D images.
