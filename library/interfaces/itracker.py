from abc import ABC, abstractmethod


class ITracker(ABC):
    @abstractmethod
    def run(self, **args):
        pass
