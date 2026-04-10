import re

def clean_text(text):
    text = re.sub(r"[^a-zA-Z ]", "", text)
    text = text.lower()
    return text