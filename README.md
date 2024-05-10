# WebAnno ⟶ spaCy

A tool that helps you to convert the
[WebAnno TSV 3.2](https://webanno.github.io/webanno/releases/3.4.5/docs/user-guide.html#sect_webannotsv)
files to [spaCy](https://spacy.io)'s `Doc` format.

## Usage

```bash
$ python webanno2spacy.py --help
Usage: webanno2spacy.py [OPTIONS] SPACY_MODEL INPUT_TEXT_FILE
                        INPUT_WEBANNO_FILE

Arguments:
  SPACY_MODEL         [required]
  INPUT_TEXT_FILE     [required]
  INPUT_WEBANNO_FILE  [required]

Options:
  --output-file PATH
  --help              Show this message and exit.
```