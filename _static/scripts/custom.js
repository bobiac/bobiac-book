// Force all external links to open in a new tab
document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll('a[href^="http"]').forEach(link => {
        console.log("Modifying link:", link.href);
        link.setAttribute('target', '_blank');
        link.setAttribute('rel', 'noopener noreferrer');
    });
});

document.addEventListener('DOMContentLoaded', function () {
    // handle Markdown links to download of files with specified extensions
    const markdownLinks = document.querySelectorAll('a');
    markdownLinks.forEach(link => {
        link.addEventListener('click', function (event) {
            const href = link.getAttribute('href');
            if (href) {
                const fileExtensions = [
                    '.pdf', '.tif', '.tiff', '.png',
                    '.jpg', '.jpeg', '.zip', '.ipynb'
                ];
                if (fileExtensions.some(ext => href.endsWith(ext))) {
                    event.preventDefault(); // Prevent navigation
                    const downloadLink = document.createElement('a');
                    downloadLink.href = href;
                    downloadLink.download = href.split('/').pop();
                    document.body.appendChild(downloadLink); // Ensure it's in DOM
                    downloadLink.click();
                    document.body.removeChild(downloadLink); // Clean up
                }
            }
        });
    });
});

// Function to download all PDF files
async function downloadPdfs() {
    // Hardcoded list of PDF files in the pdfs directory
    const pdfFiles = [
        '00_intro_to_bobiac/bobiac_intro.pdf',
        '01_getting_started_with_python/getting_started_python_uv.pdf',
        '02_python_basics/python_cheat_sheet.pdf',
        '03_digital_images_intro/digital_images_intro.pdf',
        '03_digital_images_intro/working_with_bioimages_in_python_beginners.pdf',
        '04_segmentation/classic/classic_segmentation.pdf',
        '07_measurement_and_quantification/introtoquantitativefluorescencemicroscopy.pdf',
        '08_colocalization/bobiac_coloc_intro.pdf',
        '08_colocalization/practical_object_based_coloc.pdf'
    ];
    
    // GitHub raw base URL for PDF files
    const githubRawBase = 'https://raw.githubusercontent.com/bobiac/bobiac-book/gh-pages/pdfs/';
    
    if (pdfFiles.length === 0) {
        alert('No PDF files found in the GitHub pdfs folder.');
        return;
    }
    
    // Show loading indicator
    const indicator = document.createElement('div');
    indicator.id = 'download-indicator';
    indicator.style.position = 'fixed';
    indicator.style.top = '0';
    indicator.style.left = '0';
    indicator.style.width = '100vw';
    indicator.style.height = '100vh';
    indicator.style.background = 'rgba(0,0,0,0.4)';
    indicator.style.display = 'flex';
    indicator.style.alignItems = 'center';
    indicator.style.justifyContent = 'center';
    indicator.style.zIndex = '9999';
    indicator.innerHTML = '<div style="background: #fff; padding: 30px 40px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.2); font-size: 1.2em; text-align: center;">Downloading PDFs...<br><span id="download-progress"></span></div>';
    document.body.appendChild(indicator);

    // Load JSZip library
    let JSZip;
    if (window.JSZip) {
        JSZip = window.JSZip;
    } else {
        const module = await import('https://cdn.jsdelivr.net/npm/jszip@3.10.1/dist/jszip.min.js');
        JSZip = module.default || module.JSZip || window.JSZip;
    }

    const zip = new JSZip();
    const pdfFolder = zip.folder("bobiac_pdfs");

    // Fetch and add each file to the zip from GitHub raw URLs
    for (let i = 0; i < pdfFiles.length; i++) {
        const filename = pdfFiles[i];
        try {
            const fileResponse = await fetch(githubRawBase + filename);
            if (!fileResponse.ok) throw new Error(`HTTP ${fileResponse.status}`);
            const fileBlob = await fileResponse.blob();
            pdfFolder.file(filename, fileBlob);
            // Update progress
            document.getElementById('download-progress').textContent = `(${i+1}/${pdfFiles.length})`;
        } catch (error) {
            console.error(`Failed to fetch ${filename} from GitHub:`, error);
        }
    }

    // Generate and download the combined zip
    document.getElementById('download-progress').textContent = 'Zipping files...';
    const zipBlob = await zip.generateAsync({type: "blob"});
    const link = document.createElement('a');
    link.href = window.URL.createObjectURL(zipBlob);
    link.download = 'bobiac_pdfs.zip';
    link.style.display = 'none';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    window.URL.revokeObjectURL(link.href);
    // Remove indicator
    document.body.removeChild(indicator);
}

// Function to download all notebook files
async function downloadNotebooks() {
    // GitHub raw base URL for student notebooks
    const githubRawBase = 'https://raw.githubusercontent.com/bobiac/bobiac-book/gh-pages/notebooks/';

    // The list of notebooks (excluding *_colab.ipynb) is generated at build
    // time by build.sh into notebooks_manifest.json, so it always matches
    // the notebooks actually published for the current version of the book.
    let notebookFiles;
    try {
        const manifestResponse = await fetch('https://raw.githubusercontent.com/bobiac/bobiac-book/gh-pages/notebooks_manifest.json');
        if (!manifestResponse.ok) throw new Error(`HTTP ${manifestResponse.status}`);
        notebookFiles = await manifestResponse.json();
    } catch (error) {
        console.error('Failed to fetch notebook manifest:', error);
        alert('Could not load the list of notebooks. Please try again later.');
        return;
    }

    if (!notebookFiles || notebookFiles.length === 0) {
        alert('No notebook files found in the GitHub notebooks folder.');
        return;
    }

    // Show loading indicator
    const indicator = document.createElement('div');
    indicator.id = 'download-indicator';
    indicator.style.position = 'fixed';
    indicator.style.top = '0';
    indicator.style.left = '0';
    indicator.style.width = '100vw';
    indicator.style.height = '100vh';
    indicator.style.background = 'rgba(0,0,0,0.4)';
    indicator.style.display = 'flex';
    indicator.style.alignItems = 'center';
    indicator.style.justifyContent = 'center';
    indicator.style.zIndex = '9999';
    indicator.innerHTML = '<div style="background: #fff; padding: 30px 40px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.2); font-size: 1.2em; text-align: center;">Downloading student notebooks...<br><span id="download-progress"></span></div>';
    document.body.appendChild(indicator);

    // Load JSZip library
    let JSZip;
    if (window.JSZip) {
        JSZip = window.JSZip;
    } else {
        const module = await import('https://cdn.jsdelivr.net/npm/jszip@3.10.1/dist/jszip.min.js');
        JSZip = module.default || module.JSZip || window.JSZip;
    }

    const zip = new JSZip();
    const notebookFolder = zip.folder("bobiac_notebooks_student");

    // Fetch and add each file to the zip from GitHub raw URLs
    for (let i = 0; i < notebookFiles.length; i++) {
        const filename = notebookFiles[i];
        try {
            const fileResponse = await fetch(githubRawBase + filename);
            if (!fileResponse.ok) throw new Error(`HTTP ${fileResponse.status}`);
            const fileBlob = await fileResponse.blob();
            notebookFolder.file(filename, fileBlob);
            // Update progress
            document.getElementById('download-progress').textContent = `(${i+1}/${notebookFiles.length})`;
        } catch (error) {
            console.error(`Failed to fetch ${filename} from GitHub:`, error);
        }
    }

    // Generate and download the combined zip
    document.getElementById('download-progress').textContent = 'Zipping files...';
    const zipBlob = await zip.generateAsync({type: "blob"});
    const link = document.createElement('a');
    link.href = window.URL.createObjectURL(zipBlob);
    link.download = 'bobiac_notebooks_student.zip';
    link.style.display = 'none';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    window.URL.revokeObjectURL(link.href);
    // Remove indicator
    document.body.removeChild(indicator);
}

// Function to download all teacher notebook files
async function downloadNotebooksTeacher() {
    // GitHub raw base URL for teacher notebooks
    const githubRawBase = 'https://raw.githubusercontent.com/bobiac/bobiac-book/gh-pages/notebooks_teacher/';

    // The list of notebooks (excluding *_colab.ipynb) is generated at build
    // time by build.sh into notebooks_manifest.json, so it always matches
    // the notebooks actually published for the current version of the book.
    let notebookFiles;
    try {
        const manifestResponse = await fetch('https://raw.githubusercontent.com/bobiac/bobiac-book/gh-pages/notebooks_manifest.json');
        if (!manifestResponse.ok) throw new Error(`HTTP ${manifestResponse.status}`);
        notebookFiles = await manifestResponse.json();
    } catch (error) {
        console.error('Failed to fetch notebook manifest:', error);
        alert('Could not load the list of notebooks. Please try again later.');
        return;
    }

    if (!notebookFiles || notebookFiles.length === 0) {
        alert('No notebook files found in the GitHub notebooks_teacher folder.');
        return;
    }

    // Show loading indicator
    const indicator = document.createElement('div');
    indicator.id = 'download-indicator';
    indicator.style.position = 'fixed';
    indicator.style.top = '0';
    indicator.style.left = '0';
    indicator.style.width = '100vw';
    indicator.style.height = '100vh';
    indicator.style.background = 'rgba(0,0,0,0.4)';
    indicator.style.display = 'flex';
    indicator.style.alignItems = 'center';
    indicator.style.justifyContent = 'center';
    indicator.style.zIndex = '9999';
    indicator.innerHTML = '<div style="background: #fff; padding: 30px 40px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.2); font-size: 1.2em; text-align: center;">Downloading teacher notebooks...<br><span id="download-progress"></span></div>';
    document.body.appendChild(indicator);

    // Load JSZip library
    let JSZip;
    if (window.JSZip) {
        JSZip = window.JSZip;
    } else {
        const module = await import('https://cdn.jsdelivr.net/npm/jszip@3.10.1/dist/jszip.min.js');
        JSZip = module.default || module.JSZip || window.JSZip;
    }

    const zip = new JSZip();
    const notebookFolder = zip.folder("bobiac_notebooks_teacher");

    // Fetch and add each file to the zip from GitHub raw URLs
    for (let i = 0; i < notebookFiles.length; i++) {
        const filename = notebookFiles[i];
        try {
            const fileResponse = await fetch(githubRawBase + filename);
            if (!fileResponse.ok) throw new Error(`HTTP ${fileResponse.status}`);
            const fileBlob = await fileResponse.blob();
            notebookFolder.file(filename, fileBlob);
            // Update progress
            document.getElementById('download-progress').textContent = `(${i+1}/${notebookFiles.length})`;
        } catch (error) {
            console.error(`Failed to fetch ${filename} from GitHub:`, error);
        }
    }

    // Generate and download the combined zip
    document.getElementById('download-progress').textContent = 'Zipping files...';
    const zipBlob = await zip.generateAsync({type: "blob"});
    const link = document.createElement('a');
    link.href = window.URL.createObjectURL(zipBlob);
    link.download = 'bobiac_notebooks_teacher.zip';
    link.style.display = 'none';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    window.URL.revokeObjectURL(link.href);
    // Remove indicator
    document.body.removeChild(indicator);
}