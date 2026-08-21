def clean_text(text:str) -> str:
    """Strip surronding whitespace and convert text to lowercase."""
    text = text.strip()
    text = text.lower()
    return text

def count_words(text:str) -> int:
    """ Split text into words and return the number of words"""
    words = text.split()
    return len(words)
