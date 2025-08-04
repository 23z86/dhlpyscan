import requests

from .itracker import ITracker
from ..parcel_status import ParcelStatus
from ..messages.translator import Translation
from ..pretty_table import Table


class MultiTracker(ITracker):
    def __init__(self, history_option):
        self.o_status = ParcelStatus()
        self.o_translation = Translation()
        self.o_table = Table()

        self.history_option = history_option

    def run(self, **kwargs):
        tracking_number = kwargs.get('tracking_number')
        assert tracking_number is not None

        single_tracking_number = tracking_number[0].split()

        for tracking_number in single_tracking_number:
            url = "https://www.dhl.de/int-verfolgen/data/search/?piececode=" + \
                tracking_number + "&language=" + self.o_translation.get_language() + \
                "&cid=pulltorefresh"

            json_raw_data = requests.get(url, timeout=None).json()

            parcel_status = self.o_status.get_parcel_status(json_raw_data)

            self.o_table.add_rows(parcel_status)

        self.o_table.print_data_as_table()
