import pytest

from text_processing import count_words

@pytest.mark.parametrize(
        "text,expected",
        [
            ("Hello world",2),
            ("FastAPI",1),
            ("one two three four",4),
            ("",0),
            ("  hello world  ",2),
        ]
)

def test_count_words(text, expected):
    assert count_words(text) == expected