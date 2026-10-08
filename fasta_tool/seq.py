"""Модуль с классом :class:`Seq` - одна биологическая последовательность."""
class Seq:
    """Последовательность (нуклеотидная или белковая) с заголовком.
    
    :param sequence: строка последовательности, например ``"ATGC"``
    :param header: заголовок fasta-записи (текст после ``>``)
    :raises ValueError: если последовательность пустая
    """
    NUCLEOTIDE_LETTERS = frozenset("ACGTUN")

    def __init__(self, sequence: str, header: str = "") -> None:
        if not sequence:
            raise ValueError("Последовательность не может быть пустой")
        self._sequence = sequence.upper()
        self._header = header

    @property
    def sequence(self) -> str:
        """Сама последовательность (только чтение)."""
        return self._sequence

    @property
    def header(self) -> str:
        """Заголовок fasta-записи без символа ``>`` (только чтение)."""
        return self._header

    @property
    def alphabet(self) -> str:
        """Алфавит последовательности.

        :return: ``"nucleotide"``, если все символы из ``ACGTUN``,
            иначе ``"protein"``.
        """
        if set(self._sequence) <= self.NUCLEOTIDE_LETTERS:
            return "nucleotide"
        return "protein"

    def __len__(self) -> int:
        """Длина последовательности: работает как ``len(seq)``."""
        return len(self._sequence)

    def __str__(self) -> str:
        """Красивое строковое представление: работает как ``print(seq)``."""
        short = self._sequence if len(self) <= 30 else self._sequence[:30] + "..."
        return f">{self._header} [{self.alphabet}, {len(self)}]\n{short}"

    def __repr__(self) -> str:
        """Техническое представление для отладки."""
        return f"Seq(sequence={self._sequence[:10]!r}..., header={self._header!r})"
