# Завдання 2
# Створіть клас, який описує відгук до книги. Додайте до класу книги поле – список відгуків. 
# Зробіть так, щоб при виведенні 
# книги на екран за допомогою функції print також виводилися відгуки до неї. 

class Comment:
    def __init__(self, comment_text):
        self.comment_text = comment_text
    def __str__(self):
        return f'Comment:{self.comment_text}'
    
class Book:
    def __init__(self, title):
        self.title = title
        self.comments_list = []
    
    def add_comment(self,comment_text):
       comment = Comment(comment_text)
       self.comments_list.append(comment)

    def __str__(self):
        book_info = "\n".join(str(comment)for comment in self.comments_list)
        return f'Book Title: {self.title}\nComments:\n{book_info}'
    
b1 = Book(title="Eragon")
b1.add_comment(comment_text='ksjdvbksjv')
b1.add_comment(comment_text='ksjdvbksjv')

print(b1)