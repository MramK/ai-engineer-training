import json
import logging

logger = logging.getLogger(__name__)


def load_documents(path):
    documents = []

    with open(path, "r", encoding="utf-8") as f:
        for line_number,line in enumerate(f,start = 1):

        #for line in f:
            data = json.loads(line)
            if validate_document(data):
                documents.append(data)
            else:
                raise ValueError(
                    f"Invalid document at Line {line_number}:"
                     "text must be a non-empty string"
                     )
    return documents


def validate_document(document):
    if not isinstance(document,dict):
        return False
    if "text" not in document:
        return False
    if "id" not in document:
        return False
    text = document["text"]
    if not isinstance(text, str):
        return False
    if text.strip() == "":
        return False

    return True