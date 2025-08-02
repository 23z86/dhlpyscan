from ..classes.date_converter import DateConverter
from .messages.title_message import TitleMessage


class History:
    def __init__(self):
        self.o_date_converter = DateConverter()
        self.o_title = TitleMessage()

    def get_parcel_history(self, raw_data):
        horizontal_spacer = '=' * 15

        print(
            f'{horizontal_spacer} {self.o_title.get_message(100)} {horizontal_spacer}')

        for event in raw_data:
            print(
                f"{self.o_date_converter.convert(event['datum'])} -- {event['status']}")
