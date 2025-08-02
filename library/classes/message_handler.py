from library.classes.error_message import ErrorMessage
from library.classes.title_message import TitleMessage
from library.classes.status_message import StatusMessage


class MessageHandler:
    def __init__(self):
        self.o_error = ErrorMessage()
        self.o_title = TitleMessage()
        self.o_status = StatusMessage()

    def show_message(self, message_type, message_code):
        if message_type == "error":
            return self.o_error.get_message(message_code)

        if message_type == "title":
            return self.o_title.get_message(message_code)

        if message_type == "status":
            return self.o_status.get_message(message_code)

        raise ValueError(f"Unbekannter Nachrichtentyp: {message_type}")
