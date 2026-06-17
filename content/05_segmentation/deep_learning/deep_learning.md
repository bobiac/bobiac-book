# Deep Learning Methods

Deep learning is a branch of machine learning that takes things a step further. Instead of relying on manually selected features (like edges or textures), deep learning models learn to extract **their own features** directly from raw image data. This makes them especially powerful for complex tasks like image segmentation.

<div align="center">
    <img src="../../../_static/images/dl/seg_methods_dl.png" alt="dl" width="700">
</div>

<br>

In a typical deep learning workflow, we feed the entire image into a **neural network**, a multi-layered model inspired by the brain. Through training on many labeled examples, the network learns to recognize patterns, structures, and shapes in the image. Each layer in the network transforms the data a little more, gradually building up an understanding of what’s in the image.

Unlike traditional machine learning, we don’t need to tell the model *what* to look for—it figures that out on its own.

In **image segmentation**, deep learning models assign a class to each pixel (e.g., cell, background, nucleus) and output a full **segmentation mask**. These masks can capture fine details and handle challenging cases like overlapping cells, blurry edges, or varying lighting conditions.

Because deep learning learns directly from data and can model very complex relationships, it often outperforms classical and machine learning methods for robustness, however, this performance comes at a higher cost of training and data requirement.

In the following chapters, we will explore how to perform image segmentation using [**Cellpose**](https://cellpose.readthedocs.io/en/latest/).
