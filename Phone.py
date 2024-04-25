from Field import Field

class Phone(Field):
    def __init__(self, number):
        self.value = self.validate_number(number)

    def validate_number(self, number):
        if len(number) != 10:
            raise ValueError("Номер телефону повинен містити 10 цифр")
        
        if not number.isdigit():
            raise ValueError("Номер телефону повинен містити лише цифри")
        
        return number
