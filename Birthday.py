from datetime import datetime

from Field import Field
from constants import DATE_FORMAT

class Birthday(Field):
    def __init__(self, value: str):
        try:
            self.value = datetime.strptime(value, DATE_FORMAT)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
