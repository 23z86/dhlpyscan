from abc import ABC, abstractmethod

class IMessage(ABC):
    @abstractmethod
    def get_message(self, message_code):
        pass