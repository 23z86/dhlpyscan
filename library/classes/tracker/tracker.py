# pylint: disable=missing-docstring

from .itracker import ITracker
from ..parcel_status import ParcelStatus
from ..messages.translator import Translation
from ..pretty_table import Table
from ..requester import Requester


class Tracker(ITracker):
    def __init__(self,):
        self.o_status = ParcelStatus()
        self.o_translation = Translation()
        self.o_table = Table()
        self.o_requester = Requester()

    def run(self, **kwargs):
        tracking_number = kwargs.get('tracking_number')
        assert tracking_number is not None

        single_tracking_number = tracking_number[0].split()
        url_list = []

        for tracking_number in single_tracking_number:
            url = "https://www.dhl.de/int-verfolgen/data/search/?piececode=" + \
                tracking_number + "&language=" + self.o_translation.get_language() + \
                "&cid=pulltorefresh"
            url_list.append(url)

        json_raw_data = self.o_requester.execute_request(url_list)
        parcel_status = self.o_status.executor(json_raw_data)

        self.o_table.add_rows(parcel_status)

        self.o_table.print_data_as_table()
