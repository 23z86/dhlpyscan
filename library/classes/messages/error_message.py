from .translator import Translation
from .imessage import IMessage


class ErrorMessage(IMessage):
    def __init__(self):
        self.o_tranlator = Translation()

    def get_message(self, message_code):
        return self.o_tranlator.get_error(message_code)
