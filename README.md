# File Processing Tool

The File Processing Tool is a Python script that reads all the doc, html, and txt files in a folder, extracts the file name and content, and writes them into a CSV file.

## Prerequisites

- Python 3.x installed. Visit [Python website](https://www.python.org/downloads/) for instructions.
- Required Python packages: 'beautifulsoup4'
- Pandoc Installed. Visit [Pandoc website](https://pandoc.org/installing.html) for instructions.

## Installation

1. Clone or download this repository.

2. Open a terminal or command prompt and navigate to the project folder.

3. Create a virtual environment (optional but recommended):
   ```
   python -m venv .env
   ```

4. Activate the virtual environment:
   - On Windows:
     ```
     env\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source env/bin/activate
     ```

5. Install the required Python packages:
   ```
   pip install beautifulsoup4
   ```

## Usage

1. Place your docx, html, and txt files in the source folder.

2. Open a terminal or command prompt and navigate to the project folder.

3. Activate the virtual environment (if created).

4. Run the script:
   ```
   python script.py
   ```

5. The tool will read all the files in the folder, extract the file name and content, and store them in a CSV file named 'products.csv'.

## Customization

You can customize the tool by modifying the following variables in the script file:

- `folder_path`: Path to the folder containing the files to be processed.
- `csv_file_path`: Path to the CSV file where the file name and content will be stored.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please open an issue or submit a pull request.

## License

This tool is licensed under the [MIT License](LICENSE).