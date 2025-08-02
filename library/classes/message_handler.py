from library.classes.error_message import ErrorMessage
from library.classes.title_message import TitleMessage
from library.classes.status_message import StatusMessage


class MessageHandler:
    def __init__(self):
        self.o_error = ErrorMessage()
        self.o_title = TitleMessage()
        self.o_status = StatusMessage()

    def show_message(self, message_type, message_code):

        valid_types = {
            "error": self.o_error,
            "title": self.o_title,
            "status": self.o_status,
        }

        handler = valid_types.get(message_type)

        if handler is None:
            raise ValueError
        return handler.get_message(message_code)
