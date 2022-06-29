class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.name == other.name and self.roll_number == other.roll_number
        return False

    def __str__(self) -> str:
        return f"Name: {self.name}, Roll Number: {self.roll_number}"

    def __repr__(self) -> str:
        return f"[Student: {self.name}, Roll Number: {self.roll_number}]"

    def __hash__(self) -> int:
        return super().__hash__()
