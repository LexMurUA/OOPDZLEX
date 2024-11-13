# Завдання 1
# Створіть клас, який описує книгу. Він повинен містити інформацію про автора, назву,
# рік видання та жанр. 
# Створіть кілька різних книжок. Визначте для нього методи _repr_ та _str_.
class Book:
    def __init__(self, title,author,year,genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    # def __str__(self):
    #     return f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Genre: {self.genre}"
    
    def __repr__(self):
        return f"Book({self.title!r}, {self.author!r}, {self.year!r}, {self.genre!r})"

book1 = Book(title="Eragon",author="Paolini",year=1987,genre="fantasy")

print(book1)
