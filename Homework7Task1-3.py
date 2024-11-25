# # Завдання 1
# # Напишіть генератор, який повертає елементи заданого списку у зворотному порядку (аналог reversed).

# # повретає по елементу
# def generator(list):
#     for nums in list[::-1]:
#         yield nums

# my_list = [1, 2, 3, 4, 5, 6, 7, 8,'df','dfv']
# gen = generator(my_list)

# for _ in range(10):
#     print(next(gen))

# # повертає увесь список 
# def generator(list):
#     yield list[::-1]

# my_list = [1, 2, 3, 4, 5, 6, 7, 8,'df','dfv']
# gen = generator(my_list)
# print(next(gen))

# Завдання 2
# Виведіть із списку чисел список квадратів парних чисел. Використовуйте 2 варіанти рішення: генератор та цикл
# import math
# def generator(list):
#     yield [pow(nums, 2) for nums in list if isinstance(nums, (int, float)) and nums % 2 == 0]

# my_list = [1, 2, 3, 4, 5, 6, 7, 8,'df','dfv']
# gen = generator(my_list)

# print(next(gen))
# import math
# class Bill:
#     def __init__(self, item):
#         self.counter = 0
#         self.item = [pow(nums, 2) for nums in item if isinstance(nums, (int, float)) and nums % 2 == 0]
#     def __iter__(self):
#         self.counter = 0
#         return self
#     def __next__(self):
#         if self.counter >= len(self.item):
#             raise StopIteration
#         else:
#             result = self.item[self.counter]
#             self.counter += 1
#             return result
# emp = Bill([1, 2, 3, 4, 5, 6, 7, 8,'df','dfv'])
# for i in emp:
#     print(i)

# Завдання 3

# Напишіть функцію-генератор для отримання n перших простих чисел.
import math
import random

# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):  
#         if num % i == 0:
#             return False
#     return True


def generator(num):
    for nums in range(num):
        if nums > 1:
            if (nums*0.5) % nums == 0:
                yield nums



num = random.randint(2,100)
gen = generator(num)

print(next(gen))








