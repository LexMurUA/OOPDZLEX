# # Завдання 1

# # Реалізуйте цикл, який перебиратиме всі значення ітерабельного об'єкту iterable

# class Myliststrange:
#     def __init__(self, data):
#         self.data = data
#         self.current = 0
        

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.current < len(self.data):
#             result = self.data[self.current]
#             self.current += 1  # Збільшуємо індекс
#             return result
#         else:
#             raise StopIteration 
        
# mylist = Myliststrange(['a', 'b', 'c', 'd', 'e', 'f','g', 'h'])

# for i,v in enumerate(mylist):
#     print(f'{i} - {v}')

# Завдання 3
# Напишіть ітератор, який повертає елементи заданого списку у зворотному порядку (аналог reversed).

class Myliststrange:
    def __init__(self, data):
        self.data = data[::-1]
        self.current = 0
        

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < len(self.data):
            result = self.data[self.current]
            self.current += 1  # Збільшуємо індекс
            return result
        else:
            raise StopIteration 
        
mylist = Myliststrange(['a', 'b', 'c', 'd', 'e', 'f','g', 'h','d'])

for i,v in enumerate(mylist):
    print(f'{i} - {v}')
