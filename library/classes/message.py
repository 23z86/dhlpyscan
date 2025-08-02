from ..classes.translator import Translation
from ..interfaces.imessage import IMessage


class ErrorMessage(IMessage):
    def __init__(self):
        self.o_tranlator = Translation()

    def get_message(self, message_code):
        return self.o_tranlator.get_errors(message_code)