from ..interfaces.itracker import ITracker
from .parcel_status import ParcelStatus
from ..classes.history import History
from ..classes.error_message import ErrorMessage
import requests


class SingleTracker(ITracker):
    def __init__(self, history_option):
        self.o_status = ParcelStatus()
        self.o_history = History()
        self.o_error = ErrorMessage()
        self.history_option = history_option

    def run(self, tracking_number):
        single_tracking_number = tracking_number[0]
        url = "https://www.dhl.de/int-verfolgen/data/search/?piececode=" + \
            single_tracking_number + "&language=de" + "&cid=pulltorefresh"
        json_raw_data = requests.get(url, timeout=None).json()

        if 'aktuellerStatus' not in json_raw_data['sendungen'][0]['sendungsdetails']['sendungsverlauf']:
            print(self.o_error.get_message(100).format(single_tracking_number))
            return

        print(self.o_status.get_parcel_status(json_raw_data))

        if self.history_option:
            self.o_history.get_parcel_history(
                json_raw_data['sendungen'][0]['sendungsdetails']['sendungsverlauf']['events'])
