from prettytable import PrettyTable


class Table:
    def __init__(self):
        self.o_table = PrettyTable()

    def print_data_as_table(self):
        self._add_field_names()
        self._print_data()

    def _add_field_names(self):
        self.o_table.field_names = ["Tracking Number",
                                    "Changed on", "Current Status"]

    def add_rows(self, data):
        self.o_table.add_rows(data)

    def _print_data(self):
        print(self.o_table)
