"""Демонстрационная программа: python demo.py [файл.fasta ...]"""

import sys

from fasta_tool import FastaReader

DEFAULT_FILES = [
    "examples/dna.fasta",
    "examples/protein.fasta",
    "examples/broken.fasta",
]


def main(paths):
    for path in paths:
        print("=" * 50)
        print(f"Файл: {path}")
        reader = FastaReader(path)
        print("Корректный fasta:", reader.is_valid())
        try:
            for seq in reader.read():
                print(seq)
                print(f"  длина = {len(seq)}, алфавит = {seq.alphabet}\n")
        except ValueError as error:
            print("ОШИБКА ФОРМАТА:", error)


if __name__ == "__main__":
    main(sys.argv[1:] or DEFAULT_FILES)
