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


def generate_gaussian_spots_2d(
    shape: tuple[int, int] = (256, 256),
    n_spots: int = 50,
    scale: tuple[float, float] = (0.1, 0.1),  # µm/pixel (y, x)
    na: float = 0.75,
    em_wvl_um: float = 0.520,  # emission wavelength in µm (GFP)
    sigma_scale_range: tuple[float, float] = (1.5, 4.5),  # per-spot size jitter
    background: float = 0.05,  # autofluorescence (fraction of max)
    noise: float = 0.02,  # read-noise std (fraction of max)
    seed: int | None = None,
) -> np.ndarray:
    """Return a 2-D image of Gaussian spots with physically-derived PSF size.

    Spot sigma is computed from NA and emission wavelength using the Gaussian PSF
    approximation, then converted to pixels via `scale`.
    `sigma_scale_range` adds per-spot variability as a random multiplier on that size.

    Args:
        shape:              Image dimensions (Y, X).
        n_spots:            Number of randomly placed spots.
        scale:              Physical pixel size in µm (y, x).
        na:                 Objective numerical aperture.
        em_wvl_um:          Emission wavelength in µm.
        sigma_scale_range:  (min, max) multiplicative jitter applied per spot.
        background:         Smooth autofluorescence level as fraction of peak intensity.
        noise:              Gaussian read-noise std as fraction of peak intensity.
        seed:               Optional RNG seed for reproducibility.
    """
    _, dx = scale  # assume square pixels

    # physical PSF sigma in µm (Gaussian PSF lateral approximation)
    sigma_xy_um = 0.21 * em_wvl_um / na

    # convert to pixels
    sigma_xy_pix = sigma_xy_um / dx

    rng = np.random.default_rng(seed)

    # independent per-spot size jitter
    jitter = rng.uniform(*sigma_scale_range, size=n_spots)
    sxy_vals = sigma_xy_pix * jitter
    intensities = rng.uniform(0.5, 1.0, size=n_spots)

    max_sigma = sigma_xy_pix * sigma_scale_range[1]
    margin = int(max_sigma * 4)
    lo, hi = margin, np.array(shape) - margin
    positions = rng.integers(lo, hi, size=(n_spots, 2))

    image = np.zeros(shape, dtype=np.float32)
    r = int(max_sigma * 4)
    for (y0, x0), sxy, amp in zip(positions, sxy_vals, intensities):
        ys = slice(max(0, y0 - r), min(shape[0], y0 + r + 1))
        xs = slice(max(0, x0 - r), min(shape[1], x0 + r + 1))
        yg = np.arange(ys.start, ys.stop) - y0
        xg = np.arange(xs.start, xs.stop) - x0
        YY, XX = np.meshgrid(yg, xg, indexing="ij")
        image[ys, xs] += amp * np.exp(-0.5 * ((YY / sxy) ** 2 + (XX / sxy) ** 2))

    # smooth autofluorescence background
    bg = gaussian(rng.uniform(0, 1, shape).astype(np.float32), sigma=20)
    bg = bg / bg.max() * background

    # Gaussian read noise
    read_noise = rng.normal(0, noise, shape).astype(np.float32)

    return image + bg + read_noise


# generate 2d spots
scale = (0.1, 0.1)
spots = generate_gaussian_spots_2d(
    seed=2,
    scale=scale,
    na=1.4,
    em_wvl_um=0.520,  # emission wavelength in µm (GFP)
    sigma_scale_range=(1, 3),  # per-spot size jitter
    background=0.09,  # autofluorescence (fraction of max)
    noise=0.04,  # read-noise std (fraction of max)
)

ndv.imshow(spots)

# scale float image to the full uint16 range before saving
# import tifffile

# spots_uint16 = (np.clip(spots, 0, 1) * 65535).astype(np.uint16)
# tifffile.imwrite("_static/images/spots/2d_spots.tif", spots_uint16)
