from .itracker import ITracker
from ..parcel_status import ParcelStatus
import requests


class MultiTracker(ITracker):
    def __init__(self, history_option):
        self.o_messenger = ParcelStatus()
        self.history_option = history_option

    def run(self, tracking_number):
        pass
