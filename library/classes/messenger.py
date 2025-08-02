from datetime import datetime

class Messenger:
    def get_parcel_status(self, raw_data):
        horizontal_spacer = '=' * 15

        current_state_date = raw_data['sendungen'][0]['sendungsdetails']['sendungsverlauf']['datumAktuellerStatus']
        tracking_number = raw_data['sendungen'][0]['id']
        current_state = raw_data['sendungen'][0]['sendungsdetails']['sendungsverlauf']['aktuellerStatus']
        short_state = raw_data['sendungen'][0]['sendungsdetails']['sendungsverlauf']['kurzStatus']
        short_step = raw_data['sendungen'][0]['sendungsdetails']['sendungsverlauf']['fortschritt']
        max_steps = raw_data['sendungen'][0]['sendungsdetails']['sendungsverlauf']['maximalFortschritt']


        iso_date = current_state_date
        dt = datetime.fromisoformat(iso_date)
        formatted_date = dt.strftime("%d.%m.%Y")

        print(f'{horizontal_spacer} Main Information {horizontal_spacer}')

        return f'Your parcel: {tracking_number}\nLast change: {formatted_date}\nCurrent state: {current_state}'