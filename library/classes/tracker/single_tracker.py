# pylint: disable=missing-docstring
import requests


from .itracker import ITracker
from ..parcel_status import ParcelStatus
from ..messages.error_message import ErrorMessage
from ..messages.translator import Translation
from ..history import History
from ..pretty_table import Table


class SingleTracker(ITracker):
    def __init__(self, history_option):
        self.o_status = ParcelStatus()
        self.o_error = ErrorMessage()
        self.o_translation = Translation()
        self.o_history = History()
        self.o_table = Table()
        self.history_option = history_option

    def run(self, **kwargs):
        tracking_number = kwargs.get('tracking_number')
        assert tracking_number is not None
        single_tracking_number = tracking_number[0]

        url = "https://www.dhl.de/int-verfolgen/data/search/?piececode=" + \
            single_tracking_number + "&language=" + self.o_translation.get_language() + \
            "&cid=pulltorefresh"
        json_raw_data = requests.get(url, timeout=None).json()

        self.o_table.add_rows(self.o_status.get_parcel_status(json_raw_data))
        self.o_table.print_data_as_table()

        if self.history_option:
            self.o_history.get_parcel_history(
                json_raw_data['sendungen'][0]['sendungsdetails']['sendungsverlauf']['events'])
