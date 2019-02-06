import cypher_app.command_line.console_io as c_io
from docx import Document
import os
import re

file_regex = re.compile(r"([A-z0-9]{0,}\.[A-z]{0,})")


def determine_if_file_is_docx(file_name):
    return ".docx" in file_name


def validate_file_name(file_name):
    if(file_regex.match(file_name) is None):
        raise AssertionError("file_name was not a file_name")


def read_in_file(file_name):
    validate_file_name(file_name)
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


def get_all_public_keys(dir="."):
    files = []
    for names in os.listdir(dir):
        if("pub" in names):
            files.append(names)
    return files


def get_all_private_keys(dir="."):
    files = []
    for names in os.listdir(dir):
        if("priv" in names):
            files.append(names)
    return files
