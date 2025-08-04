# pylint: disable=missing-docstring
# pylint: disable=W0613:unused-argument
from cmd import Cmd
import sys
import os
import re
from library.classes.tracker.tracking_factory import TrackingFactory
from library.classes.messages.message_handler import MessageHandler


class CMDTracker(Cmd):
    prompt = 'DHL Parcel Tracker >> '
    welcome_message = "Welcome to DHL Parcel Tracker."
    subtitle = "A CLI-based Python tool to track your DHL parcels."
    motivation = "No cookies, no personal data."
    help_message = "Type \"help\" for available commands."
    separator = "~" * len(subtitle)

    intro = f'{welcome_message}\n{subtitle}\n{motivation}\n\n{help_message}\n{separator}\n'

    o_message_handler = MessageHandler()

    def do_track(self, line):
        """ Main function to track a parcel
        usage: track <tracking number> (--history) """
        history_option = None
        self.do_clear(line)
        try:
            if isinstance(line, str):
                tracking_numbers = []
                tracking_numbers.append(line)

            if "--history" in line:
                history_option = re.split(' ', line).pop()
                tracking_numbers = re.split(' ', line)
                tracking_numbers.pop()

            o_tracking_factory = TrackingFactory(tracking_numbers)
            concrete_tracker = o_tracking_factory.create_tracker(
                history_option)
            concrete_tracker.run(tracking_number=tracking_numbers)
            del line
        except IndexError:
            print(self.o_message_handler.show_message("error", 200))

    def do_exit(self, line):
        """ Exits the programm """

        input(self.o_message_handler.show_message("status", 100))
        sys.exit()

    def do_quit(self, line):
        """ Exits the programm """

        self.do_exit(line)

    def do_clear(self, line):
        """ Clears the console """

        os.system('cls')

    def do_info(self, line):
        """ Shows some information about the project"""
        self.do_clear(line)
        print(self.intro)
