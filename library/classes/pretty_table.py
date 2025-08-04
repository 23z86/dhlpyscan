from prettytable import PrettyTable
from library.classes.messages.message_handler import MessageHandler


class Table:
    def __init__(self):
        self.o_table = PrettyTable()
        self.o_message_handler = MessageHandler()

    def print_data_as_table(self):
        self._add_field_names()
        self._print_data()

    def _add_field_names(self):
        self.o_table.field_names = [ self.o_message_handler.show_message("title", 100),
                                     self.o_message_handler.show_message("title", 200),
                                     self.o_message_handler.show_message("title", 300)]

    def add_rows(self, data):
        self.o_table.add_rows(data)

    def _print_data(self):
        print(self.o_table)
