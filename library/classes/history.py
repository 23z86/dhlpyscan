from ..classes.date_converter import DateConverter
from ..classes.translator import Translation

class History:
    def __init__(self):
        self.o_date_converter = DateConverter()
        self.o_translation = Translation()

    def get_parcel_history(self, raw_data):
        horizontal_spacer = '=' * 15

        print(f'{horizontal_spacer} {self.o_translation.get_title(100)} {horizontal_spacer}')


        for event in raw_data:
            print(
                f"{self.o_date_converter.convert(event['datum'])} -- {event['status']}")
