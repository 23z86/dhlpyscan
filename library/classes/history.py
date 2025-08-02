from ..classes.date_converter import DateConverter


class History:
    def __init__(self):
        self.o_date_converter = DateConverter()

    def get_parcel_history(self, raw_data):
        horizontal_spacer = '=' * 15

        print(f'{horizontal_spacer} History {horizontal_spacer}')

        for event_counter in range(len(raw_data)):

            print(
                f'{self.o_date_converter.convert(raw_data[event_counter]['date'])} -- {raw_data[event_counter]['status']}')
