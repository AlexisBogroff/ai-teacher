"""
Extract text from html file
"""
import re
from bs4 import BeautifulSoup

FOLDER_PATH = 'data/'
HTML_FILE_NAME = 'SDIS-78_SUAP_2023_tome_1_TH_web.html'

def remove_empty_lines(text, consecutive=2):
    """Remove consecutive empty lines"""
    return re.sub(rf'\n{{{consecutive},}}', '\n\n', text)

def extract_text_from_html(html_file_path):
    """Extract text from html file"""
    with open(html_file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        text = soup.get_text()
    return text

def save_to_txt_file(text):
    """Save text to txt file"""
    with open(FOLDER_PATH + 'content.txt', 'w', encoding='utf-8') as file:
        file.write(text)


# Extract text from html file
content = extract_text_from_html(FOLDER_PATH + HTML_FILE_NAME)
content = remove_empty_lines(content)
save_to_txt_file(content)
