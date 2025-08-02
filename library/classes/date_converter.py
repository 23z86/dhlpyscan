from datetime import datetime

class DateConverter:
    def convert(self, raw_datetime):
        iso_date = raw_datetime
        dt = datetime.fromisoformat(iso_date)
        formatted_date = dt.strftime("%d.%m.%Y")

        return formatted_date