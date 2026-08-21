# test 1: from text_processing import clean_text, count_words

# test 2:from text_processing import clean_text
from text_processing import clean_text, count_words


document = "   Hellooo Maci   "

cleaned_text = clean_text(document)
word_count = count_words(cleaned_text)

print("Cleaned text:", cleaned_text)
print("Word count:", word_count)

