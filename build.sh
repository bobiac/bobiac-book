#!/bin/bash

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
DISPLAY=${DISPLAY:-:99} python -m sphinx -a . -b html _build/html
echo "📘 Book built successfully at _build/html/"

# update notebook html styles
echo "🎨 Applying HTML styles to headers..."
python "$(dirname "$0")/update_html_styles.py" _build/html/content
python "$(dirname "$0")/update_html_styles.py" _build/html/student_group_work
python "$(dirname "$0")/update_html_styles.py" _build/html/landing-page.html
echo "✅ HTML styles applied successfully."

# Prepare built notebook downloads in _build/html/notebooks/ and 
# prepare built colab notebook in _build/html/colab_notebooks/
folders=("content" "student_group_work")
echo "📁 Preparing notebooks for download and colab..."
for folder in "${folders[@]}"; do
  for notebook in $(find "$folder" -name "*.ipynb"); do
    rel_path="${notebook#$folder/}"  # remove folder prefix dynamically
    notebook_teacher_path="_build/html/notebooks_teacher/$rel_path"
    notebook_path="_build/html/notebooks/$rel_path" 
    colab_path="_build/html/colab_notebooks/$rel_path"

    notebook_teacher_dir=$(dirname "$notebook_teacher_path")
    notebook_dir=$(dirname "$notebook_path")
    colab_dir=$(dirname "$colab_path")

    mkdir -p "$notebook_teacher_dir"
    mkdir -p "$notebook_dir"
    mkdir -p "$colab_dir"

    echo "📓 Processing $folder/$rel_path..."
    python "$(dirname "$0")/update_notebooks.py" "$notebook" "$notebook_teacher_path" true
    python "$(dirname "$0")/update_notebooks.py" "$notebook" "$notebook_path" false
    python "$(dirname "$0")/update_notebooks_colab.py" "$notebook" "$colab_path" true
  done
done

echo "✅ Updated notebooks copied to _build/html/notebooks_teacher/"
echo "✅ Updated notebooks copied to _build/html/notebooks/"
echo "✅ Colab notebooks copied to _build/html/colab_notebooks/"

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