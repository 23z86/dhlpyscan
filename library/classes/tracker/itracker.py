from abc import ABC, abstractmethod


class ITracker(ABC):
    @abstractmethod
    def run(self, **kwargs):
        pass
