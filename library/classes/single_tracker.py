from ..interfaces.itracker import ITracker
from ..classes.messenger import Messenger
from ..classes.history import History
import requests


class SingleTracker(ITracker):
    def __init__(self, history_option):
        self.o_messenger = Messenger()
        self.o_history = History()
        self.history_option = history_option

    def run(self, tracking_number):
        single_tracking_number = tracking_number[0]
        url = "https://www.dhl.de/int-verfolgen/data/search/?piececode=" + \
            single_tracking_number + "&language=de" + "&cid=pulltorefresh"
        json_raw_data = requests.get(url, timeout=None).json()

        if not requests.get(url, timeout=None).status_code == 200:
            print(f"Sendung {single_tracking_number} nicht gefunden")
            return

        print(self.o_messenger.get_parcel_status(json_raw_data))

        if self.history_option:
            self.o_history.get_parcel_history(
                json_raw_data['sendungen'][0]['sendungsdetails']['sendungsverlauf']['events'])
