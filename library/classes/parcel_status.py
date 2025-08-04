from .date_converter import DateConverter
from .messages.status_message import StatusMessage
from .messages.title_message import TitleMessage


class ParcelStatus:
    def __init__(self):
        self.o_date_converter = DateConverter()
        self.o_message = StatusMessage()
        self.o_title = TitleMessage()

    def get_parcel_status(self, raw_data):
        status_data = []
        incomplete_status_data = []

        try:
            self.validate_data_is_available(raw_data)
            current_state_date = raw_data['sendungen'][0]['sendungsdetails']['sendungsverlauf']['datumAktuellerStatus']
            tracking_number = raw_data['sendungen'][0]['id']
            current_state = raw_data['sendungen'][0]['sendungsdetails']['sendungsverlauf']['aktuellerStatus']

            status_data.append(
                [tracking_number,  self.o_date_converter.convert(current_state_date), current_state])

            return status_data

        except ValueError:
            incomplete_status_data.append(
                [raw_data['sendungen'][0]['id'], "Keine Daten!", "Keine Daten!"])
            return incomplete_status_data

    def validate_data_is_available(self, raw_data):
        if 'aktuellerStatus' not in raw_data['sendungen'][0]['sendungsdetails']['sendungsverlauf']:
            raise ValueError
