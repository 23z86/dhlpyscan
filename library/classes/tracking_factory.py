from ..interfaces.itracker import ITracker
from library.classes.single_tracker import SingleTracker
from library.classes.multi_tracker import MultiTracker


class TrackingFactory:
    def __init__(self, tracking_numbers):
        self.tracking_numbers = tracking_numbers

    def create_tracker(self, history_option) -> ITracker:
        if len(self.tracking_numbers) == 1:
            return SingleTracker(history_option)

        return MultiTracker(history_option)
