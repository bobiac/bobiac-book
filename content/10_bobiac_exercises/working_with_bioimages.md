# Working with Bioimages

**Context:** You are working with a colleague to image placental spheroids on a Zeiss point scanning confocal microscope. Your colleague collected a 2 channel z stack of a placental spheroid while you were sick. You are going to use what you have learned about Python to inspect the file and prepare a figure to show your PI.

## Exercise 1

**Background:** When imaging, it is important to be aware of your detector's bit depth, as it specifies the range of possible intensity values in your acquired image. As you learned, the range is defined as 0 to 2^bit depth. Image **saturation** occurs when intensity values reach the maximum value. In practice, it is good to avoid saturation so that you can distinguish relative intensity differences.

**Problem:** You suspect that your colleague may have used settings that led to saturation. Write Python code to determine whether there are any saturated pixels in either channel across all z-slices.

:::{dropdown} Solution

```python
# import dependencies
import bffile
import numpy as np

# read the .czi image file with bffile
image_path = r"../../_static/images/python4bia/final_challenge.czi"
image = bffile.imread(image_path)

# drop T axis since it is 1
image = np.squeeze(image)

# check the dtype of the image to see what the maximum pixel intensity value could be
print(image.dtype) # we see that the dtype is uint16, so the max pixel intensity value is 65535

# check to see what the maximum pixel intensity value is in the image
print(image.max()) # we see that the max pixel intensity value in the image is 65535, so your colleague saturated the image
```

:::

## Exercise 2

**Problem:** Your PI asks to see the maximum intensity projection (MIP) of each channel side by side that your colleague collected. Write code to plot the two MIPs side by side.

:::{dropdown} Solution

```python
# import dependencies
import matplotlib.pyplot as plt
import numpy as np

# get each channel from image
channel_1 = image[0] # channel 1
channel_2 = image[1] # channel 2

# calculate each channel's MIP
mip_channel_1 = np.max(channel_1, axis=0)
mip_channel_2 = np.max(channel_2, axis=0)

# create a figure with 2 subplots, one for each channel's MIP
fig, axes = plt.subplots(1, 2, figsize=(8, 6), layout="constrained") # 1 row, 2 columns, constrained layout

# plot the images
axes[0].imshow(mip_channel_1, cmap="gray", vmin=mip_channel_1.min(), vmax=mip_channel_1.max()) # channel 1 
axes[1].imshow(mip_channel_2, cmap="gray", vmin=mip_channel_2.min(), vmax=mip_channel_2.max()) # channel 2

# turn off axes labels for both subplots
axes[0].axis("off")
axes[1].axis("off")

# show the plot
plt.show()
```

:::

## Exercise 3

**Background:** Your PI is constantly asking to see the 2 maximum intensity projections of each channel side by side for all of the images you collect, so you suspect that this request will continue to come.  

**Problem:** Rewrite your code above as a function that takes in two images, plots them side by side, and then saves the resulting plot. Use this function to plot the 2 maximum intensity projections of each channel side by side.

:::{dropdown} Solution

```python
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
    fig, axes = plt.subplots(1, 2, figsize=(8, 6), layout="constrained")  # 1 row, 2 columns, constrained layout

    # Plot images
    axes[0].imshow(img_1, cmap="gray", vmin=img_1.min(), vmax=img_1.max())
    axes[0].axis("off")  # Turn off axis label
    axes[1].imshow(img_2, cmap="gray", vmin=img_2.min(), vmax=img_2.max())
    axes[1].axis("off")  # Turn off axis label

    # Show the plot
    plt.show()

double_image_plotter(mip_channel_1, mip_channel_2)
```

:::
