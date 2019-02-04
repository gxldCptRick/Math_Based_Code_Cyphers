import io
from langdetect import detect

file = io.open('words.txt')
words = file.read().split('\n')

def is_english(text):
    lang = detect(text);
    return lang == 'en'