# fasta-tool

Небольшая библиотека на Python для чтения fasta-файлов (без Biopython).

## Установка
```
git clone https://github.com/<ваш-ник>/fasta-tool.git
cd fasta-tool
```
Нужен Python 3.8+. Внешние библиотеки не требуются.

## Запуск
```
python demo.py                  # демо на файлах из examples/
python demo.py мой_файл.fasta   # на своём файле
```

## Документация
HTML лежит в `docs/` (собрана через pdoc).

## Структура
- `fasta_tool/seq.py` - класс `Seq`
- `fasta_tool/reader.py` - класс `FastaReader`
- `uml.png` - UML-диаграмма
