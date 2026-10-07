"""Модуль с классом :class:`FastaReader` - чтение fasta-файлов."""
import re
from typing import Iterator
from .seq import Seq
class FastaReader:
    """Читает fasta-файл по записям, не загружая его целиком в память.
    :param path: путь к fasta-файлу
    """
    _VALID_LINE = re.compile(r"[A-Za-z*\-]+")
    def __init__(self, path: str) -> None:
        self._path = path

    def is_valid(self) -> bool:
        """Проверяет, что файл соответствует формату fasta.
        :return: ``True``, если весь файл прочитан без ошибок формата
        """
        try:
            for _ in self.read():
                pass
        except ValueError:
            return False
        return True

    def read(self) -> Iterator[Seq]:
        """Генератор: по одной записи отдаёт объекты :class:`Seq`.
        Файл читается построчно, в памяти хранится только текущая запись.
        :raises ValueError: если файл не соответствует формату fasta
        :raises FileNotFoundError: если файла нет
        :return: итератор объектов Seq
        """
        header = None   # заголовок текущей записи
        chunks = []     # строки последовательности текущей записи
        found_any = False

        with open(self._path, encoding="utf-8") as file:
            for line_no, line in enumerate(file, start=1):
                line = line.strip()
                if not line:
                    continue  

                if line.startswith(">"):
                    if header is not None:
                        yield self._build(header, chunks, line_no)
                    header = line[1:].strip()
                    chunks = []
                    found_any = True
                else:
                    if header is None:
                        raise ValueError(
                            f"Строка {line_no}: последовательность без заголовка '>'")
                    if not self._VALID_LINE.fullmatch(line):
                        raise ValueError(
                            f"Строка {line_no}: недопустимые символы: {line[:20]!r}")
                    chunks.append(line)
        if not found_any:
            raise ValueError("Файл пуст или не содержит fasta-записей")
        yield self._build(header, chunks, line_no)

    @staticmethod
    def _build(header: str, chunks: list, line_no: int) -> Seq:
        """Собирает объект Seq из накопленных строк (внутренний метод)."""
        if not chunks:
            raise ValueError(f"Запись {header!r} не содержит последовательности")
        return Seq("".join(chunks), header)
