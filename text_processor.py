import re
import nltk

from nltk.tokenize import word_tokenize


# Download required NLTK resources
nltk.download("punkt")
nltk.download("punkt_tab")


def preprocess_text(text):

    # Convert text to lowercase
    text = text.lower()

    # Remove unwanted characters
    text = re.sub(
        r"[^a-zA-Z0-9.,!?'\s]",
        "",
        text
    )

    # Remove extra spaces
    text = re.sub(
        r"\s+",
        " ",
        text
    ).strip()

    # Tokenization
    tokens = word_tokenize(text)

    return text, tokens