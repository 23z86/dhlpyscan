from .imessage import IMessage
from .translator import Translation


class TitleMessage(IMessage):
    def __init__(self):
        self.o_translator = Translation()

    def get_message(self, message_code):
        return self.o_translator.get_title(message_code)
