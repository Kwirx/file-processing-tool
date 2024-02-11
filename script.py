import os
import subprocess
import csv
import re
from bs4 import BeautifulSoup

# Function to convert DOC or DOCX files to HTML format
def convert_to_html(file_path):
    html_file_path = file_path + ".html"
    
    # Convert DOC or DOCX to HTML using pandoc
    subprocess.run(["pandoc", file_path, "-o", html_file_path])    
    return html_file_path
    
# Function to extract text content from HTML file
def extract_html_text(file_path):
    with open(file_path, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
        content = soup.body.decode_contents()
        return re.sub(r'style\s?=\s?"[^"]+"', '', content) #Check and strip inline css

# Function to process each file in the folder
def process_file(file_path, csv_writer):
    file_name_with_extension = os.path.basename(file_path)
    file_name = os.path.splitext(file_name_with_extension)[0]  # Extract filename without extension
    content = ""

    if file_path.endswith('.docx'):
      html_file_path = convert_to_html(file_path)
      with open(html_file_path, 'r', encoding='utf-8') as file:
          content = file.read()
      os.remove(html_file_path)
    elif file_path.endswith('.html'):
        content = extract_html_text(file_path)
    elif file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as file:
            text_content = file.read()
            content = re.sub(r'style\s?=\s?"[^"]+"', '', text_content) #Check and strip inline css
    else:
        return # Skip for all other extensions.

    csv_writer.writerow([file_name, content]) #Adding the info to the csv

# Folder path
folder_path = 'source'

# CSV file path and name
csv_file_path = 'products.csv'

# Open the CSV file for writing
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write the headers
    csv_writer.writerow(['File Name', 'Content'])

    # Iterate through each file in the folder
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            process_file(file_path, csv_writer)

print("CSV file has been created successfully.")
