import io
from langdetect import detect


def is_english(text):
    lang = detect(text)
    return lang == 'en'
