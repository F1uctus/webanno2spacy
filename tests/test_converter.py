import csv
from pathlib import Path

import pytest
import spacy

from webanno2spacy import convert_rows


@pytest.mark.parametrize("model_name", ["ru_core_news_lg"])
def test_convert_rows(model_name):
    nlp = spacy.load(model_name)
    input_text_file = Path(__file__).parent / model_name / "Путь-Королей-00.txt"
    input_webanno_file = input_text_file.with_suffix(".tsv")
    text = input_text_file.read_text()
    with open(input_webanno_file) as fd:
        rd = csv.reader(fd, delimiter="\t", quotechar='"')
        doc = convert_rows(nlp, text, rd)

    assert len(doc._.rel) == 231
