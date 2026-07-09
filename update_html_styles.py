from pathlib import Path

from bs4 import BeautifulSoup, Tag

from update_styles_data import EXAMPLE_STYLE, EXERCISE_STYLE, H2_STYLE, H3_STYLE

# List of HTML files to exclude from styling (filename only, not full path)
EXCLUDE_FROM_STYLING = [
    # Add HTML filenames here to exclude them from header styling
]


def apply_header_styles(html_content):
    """
    Apply styles to headers in HTML content based on the specified rules:
    - h2: TITLE_STYLE
    - h3: EXAMPLE_STYLE if "example" in text (case insensitive)
           EXERCISE_STYLE if "exercise" in text (case insensitive)
           TITLE_STYLE otherwise
    """
    soup = BeautifulSoup(html_content, "html.parser")
    modified = False

    # Process h2 headers
    for h2 in soup.find_all("h2"):
        if isinstance(h2, Tag):
            # Remove any existing style attribute to avoid conflicts
            if "style" in h2.attrs:
                del h2.attrs["style"]
            h2.attrs["style"] = H2_STYLE
            modified = True
            print(f"    ✅ Applied TITLE_STYLE to h2: {h2.get_text()[:50]}...")

    # Process h3 headers
    for h3 in soup.find_all("h3"):
        if isinstance(h3, Tag):
            text = h3.get_text().lower()

            # Remove any existing style attribute to avoid conflicts
            if "style" in h3.attrs:
                del h3.attrs["style"]

            if "example" in text:
                h3.attrs["style"] = EXAMPLE_STYLE
                style_name = "EXAMPLE_STYLE"
            elif "exercise" in text:
                h3.attrs["style"] = EXERCISE_STYLE
                style_name = "EXERCISE_STYLE"
            else:
                h3.attrs["style"] = H3_STYLE
                style_name = "H3_STYLE"

            modified = True
            print(f"    ✅ Applied {style_name} to h3: {h3.get_text()[:50]}...")

    return str(soup), modified


def apply_param_table_styles(html_content):
    """
    Add the `param-table` class and a matching <colgroup> to tables rendered
    from markdown inside <details> dropdowns, so columns line up across the
    several tables in a single dropdown.
    """
    soup = BeautifulSoup(html_content, "html.parser")
    modified = False

    # widths (in %) for the first N-1 columns, keyed by total column count.
    # the last column takes the remainder.
    widths_by_ncols = {2: [20], 3: [16, 24]}

    for table in soup.find_all("table"):
        if not isinstance(table, Tag):
            continue
        if table.find_parent("details") is None:
            continue

        header_row = table.find("tr")
        if header_row is None:
            continue
        ncols = len(header_row.find_all(["th", "td"]))

        existing_classes = table.get("class", [])
        if "param-table" not in existing_classes:
            table["class"] = [*existing_classes, "param-table"]

        if table.find("colgroup") is None:
            col_widths = widths_by_ncols.get(ncols)
            if col_widths is not None:
                col_widths = [*col_widths, 100 - sum(col_widths)]
            else:
                col_widths = [round(100 / ncols)] * ncols

            colgroup = soup.new_tag("colgroup")
            for w in col_widths:
                col = soup.new_tag("col")
                col["style"] = f"width: {w}%"
                colgroup.append(col)
            table.insert(0, colgroup)

        modified = True
        print(f"    ✅ Applied param-table styling to a {ncols}-column table")

    return str(soup), modified


def process_html_file(file_path):
    """Process a single HTML file and apply header styles."""
    # Check if this file should be excluded from styling
    if file_path.name in EXCLUDE_FROM_STYLING:
        return

    try:
        with open(file_path, encoding="utf-8") as f:
            content = f.read()

        modified_content, was_modified = apply_header_styles(content)
        modified_content, table_modified = apply_param_table_styles(
            modified_content
        )
        was_modified = was_modified or table_modified

        if was_modified:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(modified_content)
            print(f"  💾 Updated {file_path}")
        else:
            print(f"  ⏭️  No headers found in {file_path}")

    except Exception as e:
        print(f"  ❌ Error processing {file_path}: {e}")


def process_html_notebooks(input_path):
    """
    Process all HTML files in the specified directory and apply header styles.

    Args:
        input_path (str): Path to the directory containing HTML files to process
    """
    build_path = Path(input_path)

    if not build_path.exists():
        print(f"❌ Directory not found: {build_path}")
        return

    if not build_path.is_dir():
        print(f"❌ Path is not a directory: {build_path}")
        return

    print(f"🔍 Looking for HTML files in: {build_path}")

    # Find all HTML files recursively in the directory
    html_files = list(build_path.rglob("*.html"))

    if not html_files:
        print(f"❌ No HTML files found in {build_path}")
        return

    print(f"📝 Found {len(html_files)} HTML files to process")

    for html_file in html_files:
        print(f"\n🔄 Processing: {html_file}")
        process_html_file(html_file)

    print(f"\n✅ Finished processing {len(html_files)} HTML files")


if __name__ == "__main__":
    import sys

    # Require input path as command line argument
    if len(sys.argv) != 2:
        print("Usage: python update_html_styles.py <path_to_html_directory_or_file>")
        print("Example: python update_html_styles.py _build/html/content")
        print("         python update_html_styles.py _build/landing-page.html")
        sys.exit(1)

    input_path = sys.argv[1]
    input_path_obj = Path(input_path)

    if input_path_obj.is_dir():
        process_html_notebooks(input_path)
    elif input_path_obj.is_file():
        process_html_file(input_path_obj)
    else:
        print(f"❌ Path not found: {input_path}")
        sys.exit(1)
