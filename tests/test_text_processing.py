import pytest

from text_processing import clean_text, count_words


def test_clean_text():
    result = clean_text("  Hello Maci   ")

    assert result == "hello maci"

def test_already_clean_text():
    result = clean_text("hello maci")

    assert result == "hello maci"

def test_uppercase_clean_text():
    result = clean_text("HELLO MACI")

    assert result == "hello maci"

def test_extra_whitespace_clean_text():
    result = clean_text(" Hello Maci ")

    assert result == "hello maci"

def test_empty_string_clean_text():
    result = clean_text("")

    assert result == ""

@pytest.mark.parametrize(
        "text,expected",
        [
            ("Hello Maci", 2),
            ("Hello", 1),
            ("", 0),
            ("Hello   Maci", 2),
            ("   ", 0),
        ],
        )

def test_count_words(text, expected):
    assert count_words(text) == expected


def test_count_words_with_none():
    with pytest.raises(TypeError):
        count_words(None)


def test_count_words_with_int():
    with pytest.raises(TypeError):
        count_words(123)

def test_count_words_with_list():
    with pytest.raises(TypeError):
        count_words(["hello","world"])

