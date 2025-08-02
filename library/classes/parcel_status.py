from .date_converter import DateConverter
from .status_message import StatusMessage
from .title_message import TitleMessage


class ParcelStatus:
    def __init__(self):
        self.o_date_converter = DateConverter()
        self.o_message = StatusMessage()
        self.o_title = TitleMessage()

    def get_parcel_status(self, raw_data):
        horizontal_spacer = '=' * 15

        current_state_date = raw_data['sendungen'][0]['sendungsdetails']['sendungsverlauf']['datumAktuellerStatus']
        tracking_number = raw_data['sendungen'][0]['id']
        current_state = raw_data['sendungen'][0]['sendungsdetails']['sendungsverlauf']['aktuellerStatus']

        print(
            f'{horizontal_spacer} {self.o_title.get_message(200)} {horizontal_spacer}')

        status_message = self.o_message.get_message(200)

        return status_message.format(tracking_number, self.o_date_converter.convert(current_state_date), current_state)
