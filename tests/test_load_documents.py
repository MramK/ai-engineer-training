import pytest

from data_processing import load_documents

def test_load_empty_file(tmp_path):
    file_path = tmp_path / "empty.jsonl"
    file_path.write_text("",encoding="utf-8")

    documents = load_documents(file_path)

    assert documents == []


def test_valid_file(tmp_path):
    file_path = tmp_path / "valid.jsonl"
    file_path.write_text('{"id":1,"text":"I am text"}\n',
                          encoding = "utf-8",
                          )

    result = load_documents(file_path)

    assert result == [{"id":1, "text": "I am text"}]

def test_invalid_document(tmp_path):
    file_path = tmp_path / "invalid.jsonl"
    file_path.write_text('{"id":1,"text":""}\n',
                         encoding ="utf-8",
                         )

    with pytest.raises(ValueError, match="Line 1"):
            load_documents(file_path)

