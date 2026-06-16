# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "ndv[qt,vispy]",
#     "numpy",
#     "scikit-image",
#     "tifffile",
# ]
# ///

import ndv
import numpy as np
from skimage.filters import gaussian


def generate_gaussian_spots(
    shape: tuple[int, int, int] = (256, 256, 256),
    n_spots: int = 50,
    scale: tuple[float, float, float] = (0.5, 0.1, 0.1),  # µm/voxel (z, y, x)
    na: float = 0.75,
    ri: float = 1,  # immersion medium refractive index
    em_wvl_um: float = 0.520,  # emission wavelength in µm (GFP)
    sigma_scale_range: tuple[float, float] = (1, 4),  # per-spot size jitter
    background: float = 0.05,  # autofluorescence (fraction of max)
    noise: float = 0.02,  # read-noise std (fraction of max)
    seed: int | None = None,
) -> np.ndarray:
    """Return a 3-D volume of Gaussian spots with physically-derived PSF size.

    Spot sigma is computed from NA, refractive index, and emission wavelength using
    the Gaussian PSF approximation, then converted to voxels via `scale`.
    `sigma_scale_range` adds per-spot variability as a random multiplier on that size.

    Args:
        shape:              Volume dimensions (Z, Y, X).
        n_spots:            Number of randomly placed spots.
        scale:              Physical voxel size in µm (z, y, x).
        na:                 Objective numerical aperture.
        ri:                 Refractive index of the immersion medium.
        em_wvl_um:          Emission wavelength in µm.
        sigma_scale_range:  (min, max) multiplicative jitter applied per spot.
        background:         Smooth autofluorescence level as fraction of peak intensity.
        noise:              Gaussian read-noise std as fraction of peak intensity.
        seed:               Optional RNG seed for reproducibility.
    """
    dz, _, dx = scale  # assume square XY pixels

    # physical PSF sigmas in µm (Gaussian PSF approximation)
    sigma_xy_um = 0.21 * em_wvl_um / na
    sigma_z_um = 0.45 * em_wvl_um * ri / na**2

    # convert to voxels
    sigma_xy_vox = sigma_xy_um / dx
    sigma_z_vox = sigma_z_um / dz

    rng = np.random.default_rng(seed)

    # independent per-spot size jitter
    jitter = rng.uniform(*sigma_scale_range, size=n_spots)
    sz_vals = sigma_z_vox * jitter
    sxy_vals = sigma_xy_vox * jitter
    intensities = rng.uniform(0.5, 1.0, size=n_spots)

    max_sigma = max(sigma_z_vox, sigma_xy_vox) * sigma_scale_range[1]
    margin = int(max_sigma * 4)
    lo, hi = margin, np.array(shape) - margin
    positions = rng.integers(lo, hi, size=(n_spots, 3))

    volume = np.zeros(shape, dtype=np.float32)
    r = int(max_sigma * 4)
    for (z0, y0, x0), sz, sxy, amp in zip(positions, sz_vals, sxy_vals, intensities):
        zs = slice(max(0, z0 - r), min(shape[0], z0 + r + 1))
        ys = slice(max(0, y0 - r), min(shape[1], y0 + r + 1))
        xs = slice(max(0, x0 - r), min(shape[2], x0 + r + 1))
        zg = np.arange(zs.start, zs.stop) - z0
        yg = np.arange(ys.start, ys.stop) - y0
        xg = np.arange(xs.start, xs.stop) - x0
        ZZ, YY, XX = np.meshgrid(zg, yg, xg, indexing="ij")
        volume[zs, ys, xs] += amp * np.exp(
            -0.5 * ((ZZ / sz) ** 2 + (YY / sxy) ** 2 + (XX / sxy) ** 2)
        )

    # smooth autofluorescence background
    bg = gaussian(rng.uniform(0, 1, shape).astype(np.float32), sigma=20)
    bg = bg / bg.max() * background

    # Gaussian read noise
    read_noise = rng.normal(0, noise, shape).astype(np.float32)

    return volume + bg + read_noise


# generate 3d spots
scale = (0.3, 0.1, 0.1)
spots = generate_gaussian_spots(
    seed=2,
    scale=scale,
    na=1.4,
    ri=1.52,  # immersion medium refractive index
    em_wvl_um=0.520,  # emission wavelength in µm (GFP)
    sigma_scale_range=(1, 3),  # per-spot size jitter
    background=0.09,  # autofluorescence (fraction of max)
    noise=0.04,  # read-noise std (fraction of max)
)

ndv.imshow(spots)

# scale float volume to the full uint16 range before saving
# import tifffile

# spots_uint16 = (np.clip(spots, 0, 1) * 65535).astype(np.uint16)
# tifffile.imwrite("_static/images/spots/3d_spots.tif", spots_uint16)

# # generate binary mask with Otsu thresholding
# filtered_spots = gaussian(spots, sigma=1)
# mask = (filtered_spots > threshold_otsu(filtered_spots)).astype(np.uint8)

# # compute the distance transform (sampling accounts for anisotropic voxel size)
# distance_transform = distance_transform_edt(mask, sampling=scale)

# # find local maxima coordinates in the distance transform
# local_maxima_coords = peak_local_max(
#     distance_transform, footprint=np.ones((10, 10, 10)), min_distance=5
# )

# # create image that's the same size and dtype as mask
# local_maxima_image = np.zeros_like(mask, dtype=bool)

# # add the local_maxima_coords to the created local_maxima image
# local_maxima_image[tuple(local_maxima_coords.T)] = True

# # label the local_maxima image to create seeds for the watershed function
# seeds = label(local_maxima_image)

# # apply the watershed algorithm to segment the image and get labels
# labels_3d = watershed(-distance_transform, seeds, mask=mask)
# ndv.imshow(labels_3d, default_lut={"cmap": "glasbey"})
