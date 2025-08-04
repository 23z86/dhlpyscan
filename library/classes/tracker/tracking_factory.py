from .itracker import ITracker
from library.classes.tracker.single_tracker import SingleTracker
from library.classes.tracker.multi_tracker import MultiTracker
import re

class TrackingFactory:
    def __init__(self, tracking_numbers):
        self.tracking_numbers = tracking_numbers

    def create_tracker(self, history_option) -> ITracker:
        tracking_numbers = self.tracking_numbers[0].split()

        if len(tracking_numbers) == 1:
            return SingleTracker(history_option)

        return MultiTracker(history_option)
