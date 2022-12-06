import csv

parser = CSVParser('exampleCSV.csv')
data = parser.parse_csv()
third_column = parser.get_column(2)