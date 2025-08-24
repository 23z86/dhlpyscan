from .date_converter import DateConverter
from library.classes.messages.message_handler import MessageHandler
from .messages.title_message import TitleMessage
from concurrent.futures import ThreadPoolExecutor
from itertools import chain


class ParcelStatus:
    def __init__(self):
        self.o_date_converter = DateConverter()
        self.o_message = MessageHandler()
        self.o_title = TitleMessage()

    def execute(self, raw_data):
        with ThreadPoolExecutor(max_workers=4) as executor:
            results = executor.map(self.get_parcel_status, raw_data)

        return list(chain.from_iterable(results))
    
    def get_parcel_status(self, raw_data):
        status_data = []
        incomplete_status_data = []
        o_message_handler = MessageHandler()

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
                [raw_data['sendungen'][0]['id'], o_message_handler.show_message("status", 200), o_message_handler.show_message("status", 200)])
            return incomplete_status_data

    def validate_data_is_available(self, raw_data):
        if 'aktuellerStatus' not in raw_data['sendungen'][0]['sendungsdetails']['sendungsverlauf']:
            raise ValueError
