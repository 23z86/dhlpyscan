from ..classes.date_converter import DateConverter


class Messenger:
    def __init__(self):
        self.o_date_converter = DateConverter()

    def get_parcel_status(self, raw_data):
        horizontal_spacer = '=' * 15

        current_state_date = raw_data['sendungen'][0]['sendungsdetails']['sendungsverlauf']['datumAktuellerStatus']
        tracking_number = raw_data['sendungen'][0]['id']
        current_state = raw_data['sendungen'][0]['sendungsdetails']['sendungsverlauf']['aktuellerStatus']

        print(f'{horizontal_spacer} Main Information {horizontal_spacer}')

        return f'Your parcel: {tracking_number}\nLast change: {self.o_date_converter.convert(current_state_date)}\nCurrent state: {current_state}'
