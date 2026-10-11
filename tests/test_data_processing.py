import pytest

from data_processing import validate_document

def test_valid_document():
    result = validate_document({"id":1,"text":"I am text"})

    assert result is True

def test_empty_text():
    result = validate_document({"id":1,"text":""})

    assert result is False

def test_white_space():
    result = validate_document({"id":1, "text":" "})

    assert result is False

def test_missing_text():
    result = validate_document({"id":1})

    assert result is False

def test_missing_id():
    result = validate_document({"text":"I am text"})

    assert result is False

def test_non_dictionary():
    result =validate_document(None)

    assert result is False

def test_non_string():
    result = validate_document({"id":1, "text":None})

    assert result is False

