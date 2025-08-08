from .pretty_table import Table
from .requester import Requester
from .messages.translator import Translation
from .history_status import HistoryStatus

class History:
    def __init__(self):
        self.o_translation = Translation()
        self.o_table = Table()
        self.o_requester = Requester()
        self.o_history_status = HistoryStatus()


    def get_parcel_history(self, tracking_number):
        url_list = []
        url = "https://www.dhl.de/int-verfolgen/data/search/?piececode=" + \
                tracking_number + "&language=" + self.o_translation.get_language() + \
                "&cid=pulltorefresh"
        url_list.append(url)

        json_raw_data = self.o_requester.executor(url_list)[0]
        history = self.o_history_status.get_history(json_raw_data['sendungen'])

        self.o_table.add_rows(history)

        self.o_table.print_data_as_table()
