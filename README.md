# WebAnno ⟶ spaCy

[![](https://img.shields.io/pypi/v/webanno2spacy)](https://pypi.org/project/webanno2spacy)
[![](https://img.shields.io/pypi/wheel/webanno2spacy)](https://pypi.org/project/webanno2spacy/#files)

A tool that helps you to convert the
[WebAnno TSV 3.2](https://webanno.github.io/webanno/releases/3.4.5/docs/user-guide.html#sect_webannotsv)
files to [spaCy](https://spacy.io)'s `Doc` format.
The relations are saved into the Doc's `rel` extension attribute,
in the same way as done in the [spaCy tutorial video](https://www.youtube.com/watch?v=8HL-Ap5_Axo&t=1530s):
```python
{
    (0, 6): { "label1": 1.0, "label2": 0.0, ... },
    (6, 0): { "label1": 0.0, "label2": 0.0, ... },
    ...
}
```

## Usage

```
$ poetry install
$ webanno2spacy --help
Usage: webanno2spacy [OPTIONS] SPACY_MODEL INPUT_TEXT_FILE INPUT_WEBANNO_FILE

Arguments:
  SPACY_MODEL         [required]
  INPUT_TEXT_FILE     [required]
  INPUT_WEBANNO_FILE  [required]

Options:
  --output-file PATH
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.
```

## TODO
- Implement batch conversion of multiple files to DocBin 

## See also

- [WebAnno TSV 3.2 File format](https://webanno.github.io/webanno/releases/3.4.5/docs/user-guide.html#sect_webannotsv)
- [spaCy custom relation extraction pipeline (YouTube)](https://www.youtube.com/watch?v=8HL-Ap5_Axo)
- [spaCy custom relation extraction pipeline (code)](https://github.com/explosion/projects/tree/v3/tutorials/rel_component)
