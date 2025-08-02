from cmd import Cmd
import sys
import os
import re
from library.classes.tracking_factory import TrackingFactory
from library.classes.error_message import ErrorMessage
from library.classes.title_message import TitleMessage
from library.classes.status_message import StatusMessage


class CMDScanner(Cmd):
    prompt = 'DHL Parcel Scanner >> '
    welcome_message = "Welcome to DHL Parcel Scanner."
    subtitle = "A CLI-based Python tool to track your DHL parcels."
    help_message = "Type \"help\" for available commands."
    separator = "~" * len(subtitle)

    intro = f'{welcome_message}\n{subtitle}\n{help_message}\n{separator}\n'

    o_error = ErrorMessage()
    o_title = TitleMessage()
    o_status = StatusMessage()

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
            print(self.o_error.get_message(200))

    def do_exit(self, line):
        """ Exits the programm """

        input(self.o_status.get_message(100))
        sys.exit()

    def do_quit(self, line):
        """ Exits the programm """

        self.do_exit(line)

    def do_clear(self, line):
        """ Clears the console """

        os.system('cls')

    def do_info(self, line):
        """ Shows some information about the project"""

        print(self.intro)
