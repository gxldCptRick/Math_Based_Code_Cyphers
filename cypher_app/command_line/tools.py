import cypher_app.command_line.console_io as c_io
from docx import Document
import os


def determine_if_file_is_docx(file_name):
    return ".docx" in file_name


def read_in_file(file_name):
    if(determine_if_file_is_docx(file_name)):
        return read_all_lines_of_docx(Document(file_name))
    else:
        with open(file_name, 'r') as file:
            return format_lines(map(lambda e: e.strip(), file.readlines()))


def format_lines(lines):
    formatted = []
    current_text = []
    for line in lines:
        if(line.strip() == ""):
            formatted.append('\n'.join(current_text))
            current_text = []
        else:
            current_text.append(line)
    formatted.append('\n'.join(current_text))
    return formatted


def read_all_lines_of_docx(document):
    return format_lines(map(lambda e: e.text, document.paragraphs))


def get_list_of_all_keys():
    files = []
    for names in os.listdir("."):
        if("pub" in names):
            files.append(names)
    return files
