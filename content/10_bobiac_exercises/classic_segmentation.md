# Classic Segmentation

**Context:** You are collaborating with a colleague to study circulating tumor cell nuclei in neuroblastoma patients. They are doing the sample prep and imaging, you are analyzing the images. Your colleague shared images from their first imaging attempt. 

## Exercise 1

**Background:** The first question you both have are how many cells survived the isolation, in vitro culture, and preparation for imaging. 

**Problem:** Write code that calculates the number of cells in each image.  

:::{dropdown} Solution

```python
from pathlib import Path
import numpy as np
import tifffile as tiff
from scipy.ndimage import distance_transform_edt
from skimage.feature import peak_local_max
from skimage.filters import gaussian, threshold_otsu
from skimage.measure import label
from skimage.morphology import binary_closing, remove_small_objects
from skimage.segmentation import watershed

input_dir = Path("../../../_static/images/classic_seg/")

for image_path in input_dir.glob("*.tif"):  # only loop through files ending in .tif
    # load the image
    raw_image = tiff.imread(image_path)

    # filter the image with gaussian filter
    filtered_image = gaussian(raw_image, sigma=1)

    # threshold filtered_image to generate binary mask
    binary_mask = filtered_image > threshold_otsu(filtered_image)

    # Remove small objects
    binary_mask_sized = remove_small_objects(binary_mask, min_size=10)

    # Fill small holes by performing morphological closing
    binary_mask_filled = binary_closing(binary_mask_sized)

    # apply watershed to separate nuclei and label mask
    # compute the distance transform
    distance_transform = distance_transform_edt(binary_mask_filled)

    # find local maxima coordinates in the distance transform
    local_maxima_coords = peak_local_max(
        distance_transform, footprint=np.ones((25, 25)), min_distance=10
    )

    # create image that's the same size and dtype as binary_mask_filled
    local_maxima_image = np.zeros_like(binary_mask_filled, dtype=bool)

    # add the local_maxima_coords to the created local_maxima image
    local_maxima_image[tuple(local_maxima_coords.T)] = True

    # label the local_maxima image to create seeds for the watershed function
    seeds = label(local_maxima_image)

    # apply the watershed algorithm to segment the image and get labels
    labeled_ws_image = watershed(-distance_transform, seeds, mask=binary_mask_filled)

    # calculate the number of cells
    # number of cells = number of nuclei = number of labels
    # print the number of labels
    num_labels = labeled_ws_image.max()
    print(f"{image_path.name}: {num_labels} cells")```

:::

## Exercise 2

**Problem:** Your PI is eager to get an update on how the imaging went. Write code that creates a figure displaying one of the images and its corresponding segmentation.

:::{dropdown} Solution

```python
# specify dependencies
import matplotlib.pyplot as plt
from skimage.color import label2rgb

# define a function to plot images side by side
def double_image_plotter(img_1, img_2):
    """Function that plots 2 images side by side with their variable names as titles

    Parameters
    ----------
    img_1:
    left plotted image

    img_2:
    right plotted image

    Return
    ----------
    plot of the images

    """
    # Create a figure and axis
    fig, axes = plt.subplots(1, 2, figsize=(8, 6), layout="constrained")  # 1 row, 2 columns

    # Plot images
    axes[0].imshow(img_1, cmap="gray", vmin=img_1.min(), vmax=img_1.max())
    axes[0].axis("off")  # Turn off axis
    axes[1].imshow(img_2, cmap="gray", vmin=img_2.min(), vmax=img_2.max())
    axes[1].axis("off")  # Turn off axis

    # Show the plot
    plt.show()

# create overlay of labeled segmentation on image
seg_summary_refined = label2rgb(labeled_ws_image, image=raw_image, bg_label=0)

# plot the images
double_image_plotter(raw_image, seg_summary_refined)
```

:::

## Exercise 3

**Background:** Your PI notices a nucleus in the figure that looks intriguing, and asks what the summed intensity is compared to any other nucleus. You note that the nucleus of interest has a label 3 number in your segmentation, and you decide to compare it to a nucleus with label 5 number. 

**Problem:** Write code that calculates the summed intensity in the region of the nucleus with label 3, then do the same for the nucleus with label 5. 

:::{dropdown} Solution

```python
# labels for each nucleus
interesting_label = 3
comparison_label = 5

# get nuclei segmentations
interesting_nucleus = labeled_ws_image==interesting_label
comparison_nucleus = labeled_ws_image==comparison_label

# get interesting nucleus summed intensity
filtered_interesting_nucleus = interesting_nucleus * raw_image
sum_interesting = filtered_interesting_nucleus.sum()

# get comparison nucleus summed intensity
filtered_comparison_nucleus = comparison_nucleus * raw_image
sum_comparison = filtered_comparison_nucleus.sum()

# print values
print(f"Interesting Nucleus Summed Intensity: {sum_interesting}")
print(f"Comparison Nucleus Summed Intensity: {sum_comparison}")
```

:::