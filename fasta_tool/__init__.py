"""fasta_tool: простая библиотека для чтения fasta-файлов (без Biopython)."""

from .seq import Seq
from .reader import FastaReader

__all__ = ["Seq", "FastaReader"]
