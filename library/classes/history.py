from datetime import datetime


class History:
    def get_parcel_history(self, raw_data):
        horizontal_spacer = '=' * 15

        print(f'{horizontal_spacer} History {horizontal_spacer}')

        for event_counter in range(len(raw_data)):
            iso_date = raw_data[event_counter]['datum']
            dt = datetime.fromisoformat(iso_date)
            formatted_date = dt.strftime("%d.%m.%Y")

            print(
                f'{formatted_date} -- {raw_data[event_counter]['status']}')
