# pylint: disable=missing-docstring
# pylint: disable=W0613:unused-argument
from cmd import Cmd
import sys
import os
import re
from library.classes.messages.message_handler import MessageHandler
from library.classes.tracker.tracker import Tracker
from library.classes.history import History


class CMDTracker(Cmd):
    prompt = 'DHL Parcel Tracker >> '
    welcome_message = "Welcome to DHL Parcel Tracker."
    subtitle = "A CLI-based Python tool to track your DHL parcels."
    motivation = "No cookies, no personal data."
    help_message = "Type \"help\" for available commands."
    separator = "~" * len(subtitle)

    intro = f'{welcome_message}\n{subtitle}\n{motivation}\n\n{help_message}\n{separator}\n'

    o_message_handler = MessageHandler()

    def default(self, line):
        self.stdout.write(
            f'{self.o_message_handler.show_message("error", 300)}{line}\n')

    def do_track(self, line):
        """ Main function to track a parcel
        usage: track <tracking number>"""
        self.do_clear(line)
        try:
            if isinstance(line, str):
                tracking_numbers = []
                tracking_numbers.append(line)

            o_tracker = Tracker()
            o_tracker.run(tracking_number=tracking_numbers)

        except IndexError:
            print(self.o_message_handler.show_message("error", 200))
        except ModuleNotFoundError:
            print(self.o_message_handler.show_message("error", 200))

    def do_history(self, line):
        """ Shows the history of a parcel
        usage: history <tracking number> """

        self.do_clear(line)
        o_history = History()

        o_history.get_parcel_history(line)

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
