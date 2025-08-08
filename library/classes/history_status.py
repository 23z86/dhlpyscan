from .date_converter import DateConverter
from library.classes.messages.message_handler import MessageHandler
from .messages.title_message import TitleMessage


class HistoryStatus:
    def __init__(self):
        self.o_date_converter = DateConverter()
        self.o_message = MessageHandler()
        self.o_title = TitleMessage()


    def get_history(self, raw_data):
        history_data = []
        incomplete_status_data = []
        o_message_handler = MessageHandler()

        try:
            self.validate_data_is_available(raw_data)

            parcel_events = raw_data[0]['sendungsdetails']['sendungsverlauf']['events']
            tracking_number = raw_data[0]['id']

            for event in parcel_events:
                history_data.append([tracking_number, self.o_date_converter.convert(event['datum']), event['status']])

            return history_data

        except ValueError:
            incomplete_status_data.append(
                [raw_data[0]['id'], o_message_handler.show_message("status", 200), o_message_handler.show_message("status", 200)])
            return incomplete_status_data

    def validate_data_is_available(self, raw_data):
        if 'aktuellerStatus' not in raw_data[0]['sendungsdetails']['sendungsverlauf']:
            raise ValueError
