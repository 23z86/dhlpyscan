import ctypes


class Translation:
    def __init__(self):
        self.language = ctypes.windll.kernel32.GetUserDefaultUILanguage()

    def get_language(self) -> str:
        if self.language != 1031:
            return "en"
        return "de"

    def get_errors(self, error_code):

        errors = {
            1031: {
                100: 'Sendung {} konnte nicht gefunden werden.',
                200: 'Sendungsverfolgungsnummer fehlt.'
            },
            1033: {
                100: 'Parcel {} not found.',
                200: 'Tracking number is missing.'
            }
        }

        return errors[self.language][error_code]

    def get_title(self, title_code):

        titles = {
            1031: {
                100: 'Sendungsverlauf',
                200: 'Hauptinformationen'
            },
            1033: {
                100: 'History',
                200: 'Main Information'
            }
        }

        return titles[self.language][title_code]

    def get_message(self, message_code):
        messages = {
            1031: {
                100: 'Vielen Dank, dass du DHLPyScan nutzst - Drücke ENTER zum Verlassen...',
                200: 'Sendungsnummer: {}\nAktualisiert am: {}\nAktueller Status: {}'


            },
            1033: {
                100: 'Thank you for using DHLPyScan - Press ENTER to quit...',
                200: 'Your parcel: {}\nLast change: {}\nCurrent state: {}'

            }
        }

        return messages[self.language][message_code]
