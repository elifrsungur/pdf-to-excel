# PDF to Excel Converter

This Python script extracts data from PDF files and organizes it into an Excel file. It is designed to handle hierarchical folder structures, where:
- Project names come from the main folder name.
- District names are taken from subfolders.
- Village names are derived from the PDF filenames.

## Features
- Extracts data from PDF files using `pdfplumber`.
- Processes hierarchical folder structures for project, district, and village.
- Outputs the extracted data into a structured Excel file.

Usage
1. Organize your folder structure as follows:

Project_Folder/
├── ProjectName/
│   ├── DistrictName/
│   │   ├── Village1.pdf
│   │   ├── Village2.pdf


2. Run the script:

python pdf_to_excel.py

3. The output Excel file (detailed_project_summary.xlsx) will be saved in the main folder.

Dependencies

Python 3.7 or above
pdfplumber
pandas
openpyxl

