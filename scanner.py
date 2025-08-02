from cmd import Cmd
import sys
import re
from library.classes.tracking_factory import TrackingFactory


class CMDScanner(Cmd):
    prompt = 'DHL Parcel Scanner >> '
    welcome_message = "Welcome to DHL Parcel Scanner."
    subtitle = "A CLI-based Python tool to track your DHL parcels."
    help_message = "Type \"help\" for available commands."
    separator = "~" * len(subtitle)

    intro = f'{welcome_message}\n{subtitle}\n{help_message}\n{separator}\n'

    def do_track(self, line):
        """ Main function to track a parcel
        usage: track <tracking number> (--history) """
        
        try:
            if isinstance(line, str):
                tracking_numbers = []
                tracking_numbers.append(line)
                history_option = None

            if "--history" in line:
                history_option = re.split(' ', line).pop()
                tracking_numbers = re.split(' ', line)
                tracking_numbers.pop()

            o_tracking_factory = TrackingFactory(tracking_numbers)
            concrete_tracker = o_tracking_factory.create_tracker(
                history_option)
            concrete_tracker.run(tracking_numbers)
        except IndexError:
            print("Error - no tracking number provided")

    def do_exit(self, line):
        """ Exits the programm """

        input("Thank you for using DHLPyScan - Press ENTER to quit...")
        sys.exit()

    def do_quit(self, line):
        """ Exits the programm """

        self.do_exit(line)
