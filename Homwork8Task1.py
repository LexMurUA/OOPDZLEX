# Завдання 1
# Напишіть скрипт, який створює текстовий файл і записує до нього 10000 випадкових дійсних чисел. Створіть ще один скрипт, 
# який читає числа з файлу та виводить на екран їхню суму.   
# Варіант 1
# import random
# import os

# PATH = os.path.abspath(__file__ +'/..')

# with open(os.path.join(PATH,'test.txt'), 'w') as f:
#     program = f.write(str(sum([random.randint(0,1000) for _ in range(1000)])))

# with open(os.path.join(PATH,'test.txt'), 'r') as f:
#     program = f.read()
# print(program)

# Варіант 2

import random
import os

PATH = os.path.abspath(__file__ +'/..')
with open(os.path.join(PATH,'test.txt'), 'w') as f:
    f.write('\n'.join(str(random.randint(0, 1000)) for _ in range(1000)))


with open(os.path.join(PATH,'test.txt'), 'r') as f:
    numbers = map(int, f)
    total = sum(numbers)

  
print("Сума чисел:", total)
