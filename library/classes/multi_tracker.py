from ..interfaces.itracker import ITracker
from ..classes.messenger import Messenger
import requests


class MultiTracker(ITracker):
    def __init__(self, history_option):
        self.o_messenger = Messenger()
        self.history_option = history_option

    def run(self, tracking_number):
        pass
