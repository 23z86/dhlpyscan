from ..interfaces.itracker import ITracker
import requests


class SingleTracker(ITracker):
    def run(self, tracking_number):
        single_tracking_number = tracking_number[0]
        url = "https://www.dhl.de/int-verfolgen/data/search/?piececode=" + \
            single_tracking_number + "&language=de" + "&cid=pulltorefresh"
        json_raw_data = requests.get(url).json()

        if "sendungNichtGefunden" in json_raw_data['sendungen'][0]:
            print(f"Sendung {single_tracking_number} nicht gefunden")
            return

        current_state_date = json_raw_data['sendungen'][0]['sendungsdetails']['sendungsverlauf']['datumAktuellerStatus']
        tracking_number = json_raw_data['sendungen'][0]['id']
        current_state = json_raw_data['sendungen'][0]['sendungsdetails']['sendungsverlauf']['aktuellerStatus']
        short_state = json_raw_data['sendungen'][0]['sendungsdetails']['sendungsverlauf']['kurzStatus']
        short_step = json_raw_data['sendungen'][0]['sendungsdetails']['sendungsverlauf']['fortschritt']
        max_steps = json_raw_data['sendungen'][0]['sendungsdetails']['sendungsverlauf']['maximalFortschritt']

        print([tracking_number, current_state, current_state_date,
              short_state, short_step, max_steps])
        print(json_raw_data)
