#!/bin/bash

# Fail fast: abort (and thus fail the deploy) if any command errors, an unset
# variable is used, or a piped command fails. Without this, a Sphinx build
# crash was silently ignored and a broken, half-built site got deployed.
set -euo pipefail

# Check if OpenGL is available
echo "🔍 Verifying OpenGL setup..."
if ! glxinfo | grep -q "OpenGL version"; then
  echo "❌ OpenGL is not available! Exiting build."
  exit 1
else
  glxinfo | grep "OpenGL version"
  echo "✅ OpenGL is available."
fi

# Build the book
echo "🔧 Building Jupyter Book with Sphinx..."
# DISPLAY is set in github workflows in deploy-book.yml. This is needed
# to visualize glfw, vispy, or napari-based notebooks without errors.
# NDV_CANVAS_BACKEND is set to vispy because the pygfx (wgpu) backend fails
# to find a GPU adapter that supports FLOAT32_FILTERABLE on the headless
# Mesa/llvmpipe software renderer used in CI. This only affects notebook
# execution during the build; the notebook source still uses ndv's default
# (pygfx) backend for students running it locally.
NDV_CANVAS_BACKEND=vispy DISPLAY=${DISPLAY:-:99} python -m sphinx -a . -b html _build/html
echo "📘 Book built successfully at _build/html/"

# update notebook html styles
echo "🎨 Applying HTML styles to headers..."
python "$(dirname "$0")/update_html_styles.py" _build/html/content
python "$(dirname "$0")/update_html_styles.py" _build/html/landing-page.html
echo "✅ HTML styles applied successfully."

# Prepare built notebook downloads in _build/html/notebooks/ and 
# prepare built colab notebook in _build/html/colab_notebooks/
folders=("content")
manifest=()
echo "📁 Preparing notebooks for download and colab..."
for folder in "${folders[@]}"; do
  for notebook in $(find "$folder" -name "*.ipynb"); do
    rel_path="${notebook#$folder/}"  # remove folder prefix dynamically
    notebook_teacher_path="_build/html/notebooks_teacher/$rel_path"
    notebook_path="_build/html/notebooks/$rel_path"
    colab_path="_build/html/colab_notebooks/$rel_path"

    mkdir -p "$(dirname "$notebook_teacher_path")"
    mkdir -p "$(dirname "$notebook_path")"
    mkdir -p "$(dirname "$colab_path")"

    # The colab-specific notebooks are only meant to be opened in Colab, so
    # they are excluded from the "download all notebooks" manifest used by
    # the student/teacher download buttons.
    if [[ "$rel_path" != *_colab.ipynb && "$rel_path" != *.ipynb_checkpoints/* ]]; then
      manifest+=("$rel_path")
    fi

    echo "📓 Processing $folder/$rel_path..."
    (
      python "$(dirname "$0")/update_notebooks.py" "$notebook" "$notebook_teacher_path" true
      python "$(dirname "$0")/update_notebooks.py" "$notebook" "$notebook_path" false
      python "$(dirname "$0")/update_notebooks_colab.py" "$notebook" "$colab_path" true
    ) &
  done
done
wait

echo "✅ Updated notebooks copied to _build/html/notebooks_teacher/"
echo "✅ Updated notebooks copied to _build/html/notebooks/"
echo "✅ Colab notebooks copied to _build/html/colab_notebooks/"

# Generate a manifest of downloadable notebook paths (excluding *_colab.ipynb)
# so the "Download All Course Jupyter Notebooks" buttons always reflect the
# current set of notebooks instead of a hardcoded list in custom.js.
echo "📝 Generating notebook manifest..."
printf '%s\n' "${manifest[@]}" | sort | python -c "
import json, sys
files = [line.strip() for line in sys.stdin if line.strip()]
with open('_build/html/notebooks_manifest.json', 'w') as f:
    json.dump(files, f, indent=2)
"
echo "✅ Notebook manifest written to _build/html/notebooks_manifest.json"

# Prepare PDF downloads in _build/html/pdfs/
echo "📁 Copying PDF files to _build/html/pdfs/..."
for pdf in $(find content/ -name "*.pdf"); do
  rel_path="${pdf#content/}"  # remove 'content/' prefix
  out_path="_build/html/pdfs/$rel_path"
  out_dir=$(dirname "$out_path")
  mkdir -p "$out_dir"
  echo "📄 Copying $rel_path..."
  cp "$pdf" "$out_path"
done

echo "✅ PDF files copied to _build/html/pdfs/"