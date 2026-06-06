"""Merge w1/w2 single-channel TIFs into 2-channel TIFs (ch0=w2, ch1=w1)."""

from pathlib import Path

import numpy as np
import tifffile

SOURCE = Path("/Users/fdrgsp/Desktop/MP6843_img_full")
DEST = SOURCE.parent / (SOURCE.name + "_2ch")

# LUTs: shape (3, 256) — rows are R, G, B; columns are intensity 0-255
_ramp = np.arange(256, dtype=np.uint8)
MAGENTA_LUT = np.stack([_ramp, np.zeros(256, dtype=np.uint8), _ramp])  # R+B
GREEN_LUT = np.stack(
    [np.zeros(256, dtype=np.uint8), _ramp, np.zeros(256, dtype=np.uint8)]
)


def main() -> None:
    DEST.mkdir(exist_ok=True)

    w2_files = sorted(SOURCE.glob("*w2.TIF"))
    for w2_path in w2_files:
        w1_path = Path(str(w2_path).replace("w2.TIF", "w1.TIF"))
        if not w1_path.exists():
            print(f"Missing w1 for {w2_path.name}, skipping")
            continue

        w2 = tifffile.imread(w2_path)
        w1 = tifffile.imread(w1_path)

        merged = np.stack([w2, w1])  # shape: (2, Y, X) — ch0=w2, ch1=w1

        stem = w2_path.name.replace("w2.TIF", "")
        out_path = DEST / f"{stem}.TIF"
        tifffile.imwrite(
            out_path,
            merged,
            imagej=True,
            metadata={
                "axes": "CYX",
                "mode": "composite",
                "LUTs": [MAGENTA_LUT, GREEN_LUT],
            },
        )
        print(f"Saved {out_path.name}  {merged.shape}")


if __name__ == "__main__":
    main()
