class Alexmustnt666(Exception):
    pass
class Num:
    def __init__(self, num):
        if num  == '666':
            raise Alexmustnt666("666 is not allowed")
        self._num = num

    def get_num(self):
        return self._num
    def set_num(self):
        num = input('enter:')
        self._num = num

    def __str__(self) -> str:
        return f'Num: {self._num}'
while True:
    try:    
        d = Num(input('enter except 666:'))
        d.set_num()
        print(d)
        break
    except Alexmustnt666:
        print('666 is not allowed')
