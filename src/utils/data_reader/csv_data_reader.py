import csv
import os


class CSVDataReader:
    _row_count = 0
    _column_headers = []
    _data=[]
    _current_row_index = 0

    def __init__(self, filepath: str):
        self._filepath = os.path.abspath(filepath)
        self._read_file()

    @property
    def row_count(self):
        return self._row_count

    @property
    def column_headers(self):
        return self._column_headers

    @property
    def current_row_index(self):
        return self._current_row_index

    def increase_row_count(self, by: int = 1):
        self._current_row_index += by
        if self._current_row_index >= self._row_count:
            self._current_row_index -= by
            raise ValueError("End of record reached cannot increase")

    def get_data(self, column_name: str, row_index: int = -1):
        cur_row_index = row_index if row_index > 0 else self._current_row_index
        return self._data[cur_row_index][column_name]

    def _read_file(self):
        if not os.path.isfile(self._filepath):
            raise IOError(f"File {self._filepath} is not exist.")
        with open(self._filepath, "r") as f:
            self._csvFile = csv.DictReader(f)
            self._column_headers = list(self._csvFile.fieldnames)
            
            for row in self._csvFile:
                self._data.append(row)
        self._row_count = len(self._data)

if __name__ == "__main__":
    csvDataReader=CSVDataReader('./src/utils/data_reader/test.csv')
    print(csvDataReader.column_headers)
    print(csvDataReader.row_count)
    csvDataReader.increase_row_count(2)
    print(csvDataReader.get_data('FirstName'))