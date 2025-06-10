# Bioinformatics Playground

just something i did for funzies

## Requirements

- Python 3.13.4 (needs support for type hints)
- pyperclip

## Usage

to run the solutions to the [Rosalind Problems](https://rosalind.info/) first download the dataset for the problem into `pkg/rosalind/problems/` and run python from the root of the repository

```console
python run.py rosalind.[problem ID here]
```

remark: this is due to the weird project structure and the subsequent 'illegal' use of `exec()` to workaround import/module limitations
