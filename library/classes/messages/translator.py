import ctypes


class Translation:
    def __init__(self):
        self.language = ctypes.windll.kernel32.GetUserDefaultUILanguage()

    def get_language(self) -> str:
        if self.language != 1031:
            return "en"
        return "de"

    def get_error(self, error_code):

        errors = {
            1031: {
                100: 'Sendung {} konnte nicht gefunden werden.',
                200: 'Sendungsverfolgungsnummer fehlt.',
                300: 'Unbekannter Befehl: '
            },
            1033: {
                100: 'Parcel {} not found.',
                200: 'Tracking number is missing.',
                300: 'Unknown command: '
            }
        }

        return errors[self.language][error_code]

    def get_title(self, title_code):

        titles = {
            1031: {
                100: 'Sendungsnummer',
                200: 'Aktualisiert am',
                300: 'Aktueller Status'
            },
            1033: {
                100: 'Tracking number',
                200: 'Changed on',
                300: 'Current state'
            }
        }

        return titles[self.language][title_code]

    def get_message(self, message_code):
        messages = {
            1031: {
                100: 'Vielen Dank, dass du DHLPyScan nutzst - Drücke ENTER zum Verlassen...',
                200: 'Keine Daten!'


            },
            1033: {
                100: 'Thank you for using DHLPyScan - Press ENTER to quit...',
                200: 'No data!'

            }
        }

        return messages[self.language][message_code]
