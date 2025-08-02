class Messenger:
    def get_parcel_status(self, raw_data):
        current_state_date = raw_data['sendungen'][0]['sendungsdetails']['sendungsverlauf']['datumAktuellerStatus']
        tracking_number = raw_data['sendungen'][0]['id']
        current_state = raw_data['sendungen'][0]['sendungsdetails']['sendungsverlauf']['aktuellerStatus']
        short_state = raw_data['sendungen'][0]['sendungsdetails']['sendungsverlauf']['kurzStatus']
        short_step = raw_data['sendungen'][0]['sendungsdetails']['sendungsverlauf']['fortschritt']
        max_steps = raw_data['sendungen'][0]['sendungsdetails']['sendungsverlauf']['maximalFortschritt']

        return f'Your parcel {tracking_number} last change was on {current_state_date} and has the state {current_state}.'