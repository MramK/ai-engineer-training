

def count_words(text:str) -> int:
    '''Split text into words and return the number of words'''

    if not isinstance(text, str):
        raise TypeError("text must be a string") 
    '''type hints don't enforce types at runtime. Your isinstance() check does that explicitly. Pydantic already validates requests entering through your API, but this check also protects the function when called directly from other Python code.'''

    words = text.split()
    return len(words)

