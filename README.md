# Parser CSV

## Język

Python

## Klasa CSVParser

Klasa `CSVParser` umożliwia wczytanie danych z pliku CSV i zapisanie ich jako listy list łańcuchów. Klasa ta zawiera kilka metod pozwalających na dodatkowe operacje na wczytanych danych, takie jak pobranie konkretnej kolumny, wiersza lub komórki.

## Wymagania

Do skorzystania z klasy `CSVParser` niezbędny jest moduł csv z biblioteki standardowej Pythona.
Instalacja

Nie jest wymagana żadna dodatkowa instalacja. Wystarczy zaimportować klasę `CSVParser` z modułu csv:

```py
import csv
```

## Użycie

Aby skorzystać z klasy `CSVParser`, należy najpierw stworzyć jej obiekt z podaną nazwą pliku CSV:

```py
parser = CSVParser('filename.csv')
```

Następnie można wywołać metodę `parse_csv()`, aby wczytać dane z pliku i zapisać je jako listę list łańcuchów:

```py
data = parser.parse_csv()
```

Dodatkowo, klasa `CSVParser` zawiera następujące metody umożliwiające dodatkowe operacje na wczytanych danych:

* `get_column(index)` - pobiera dane z kolumny o podanym indeksie i zwraca je jako listę łańcuchów
* `get_row(index)` - pobiera dane z wiersza o podanym indeksie i zwraca je jako listę łańcuchów
* `get_cell(row, column)` - pobiera dane z komórki o podanym indeksie wiersza i kolumny i zwraca je jako łańcuch

## Przykład

Poniżej znajduje się przykład użycia klasy `CSVParser` do wczytania danych z pliku CSV i pobrania trzeciej kolumny:

```py
import csv

parser = CSVParser('filename.csv')
data = parser.parse_csv()
third_column = parser.get_column(2)
```