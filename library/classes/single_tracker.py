from ..interfaces.itracker import ITracker
from ..classes.messenger import Messenger

import requests


class SingleTracker(ITracker):
    def __init__(self, history_option):
        self.o_messenger = Messenger()
        self.history_option = history_option

    def run(self, tracking_number):
        single_tracking_number = tracking_number[0]
        url = "https://www.dhl.de/int-verfolgen/data/search/?piececode=" + \
            single_tracking_number + "&language=de" + "&cid=pulltorefresh"
        json_raw_data = requests.get(url).json()

        if "keineDatenVerfuegbar" in json_raw_data['sendungen'][0]['sendungNichtGefunden']:
            print(f"Sendung {single_tracking_number} nicht gefunden")
            return

        print(self.o_messenger.get_parcel_status(json_raw_data))
