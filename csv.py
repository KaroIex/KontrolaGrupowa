class CSVParser:
    def __init__(self, filename):
        self.filename = filename

    def parse_csv(self):
        with open(self.filename, 'r') as file:
            csv_reader = csv.reader(file)
            data = list(csv_reader)
            return data

    def get_column(self, index):
        data = self.parse_csv()
        column = [row[index] for row in data]
        return column

    def get_row(self, index):
        data = self.parse_csv()
        row = data[index]
        return row