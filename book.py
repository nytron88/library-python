dclass Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.name == other.name and self.author == other.author
        return False

    def __hash__(self) -> int:
        return super().__hash__()

    def __str__(self):
        return "Book: " + self.name, "Author: " + self.author
