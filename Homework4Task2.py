
# Імпорт math обходить помилку зведення в ступінь та всеодно помилка лікується базовим except ValueError програма викон без стопу.
import math
def summing(num1, num2): return num1 + num2
def difference(num1, num2): return num1 - num2
def multiplication(num1, num2): return num1 * num2
def division(num1, num2):
    try:
        return num1 / num2
        
    except ZeroDivisionError:
        return (f'Division by zero is not alloweded')  
def sinusing(num1): return math.sin(math.radians(num1))
def cosine(num1): return math.cos(math.radians(num1))
def tangents(num1): return math.tan(math.radians(num1))
def atan2(num1, num2): return math.atan2(num1, num2)
def logging(num1): return math.log(num1)
def exponential(num1): return math.exp(num1)
def square_root(num1): return math.sqrt(num1)
def hypothypotenusing(num1, num2): return math.hypot(num1, num2)
def radians(num1): return math.degrees(num1)
def degrees(num1): return math.radians(num1)
def powing(num1, num2): return math.pow(num1, num2)

# 1 Спосіб
def calculating():
    while True:
        print('======Welcome to calculator======\n'
                'Choose operation:\n'
                '1 to calculate\n'
                '2 to engeniring calculating\n'
                '3 to Exiting calculation')
        try:
            operation = int(input('Enter your choose:'))
            match operation:
                case 1:
                    try:
                        print('Enter numbers and operation')
                        num1 = float(input('Enter number:'))
                        while True:
                            operation = input('enter operation:')
                            if operation in ['+', '-', '*', '/']:
                                num2 = float(input('Enter number:'))
                                match operation:
                                    case '+':
                                        result = summing(num1, num2)
                                        print(f'Result:{num1} + {num2} = {result}')
                                    case '-':
                                        result = difference(num1, num2)
                                        print(f'Result:{num1} - {num2} = {result}')
                                    case '*':
                                        result = multiplication(num1, num2)
                                        print(f'Result:{num1} * {num2} = {result}')
                                    case '/':
                                        result = division(num1, num2)
                                        print(f'{result}')
                                        break
                            else:
                                print('please enter a valid operation (+,-,*, /)')            
                    except ValueError:
                        print('please enter an integer') 
                    continue                   
                case 2:
                    print('enter operation:1-sin,2-cos,3-tan,4-atan,5-log\n'
                        '6-exponent,7-sqrt,8-hypot,9-radians,10-degrees,11-powing')
                    operation = int(input('Enter operation:'))
                    num1 = float(input('Enter number:'))
                    match operation:
                        case 1:
                            result = sinusing(num1)
                            print(f'Result:sin({num1}) = {result}')
                        case 2:
                            result = cosine(num1)
                            print(f'Result:cos({num1}) = {result}')
                        case 3:
                            result = tangents(num1)
                            print(f'Result:tan({num1}) = {result}')
                        case 4:
                            num2 = float(input('enter number 2:'))
                            result = atan2(num1, num2)
                            print(f'Result:atan2({num1},{num2}) = {result}')
                        case 5:
                            result = logging(num1)
                            print(f'Result:log({num1}) = {result}')
                        case 6:
                            result = exponential(num1)
                            print(f'Result:exp({num1}) = {result}')
                        case 7:
                            result = square_root(num1)
                            print(f'Result:sqrt({num1}) = {result}')
                        case 8:
                            num2 = float(input('Enter lenth of second side of triangle:'))
                            result = hypothypotenusing(num1, num2)
                            print(f'Result:hypot with sides({num1},{num2}) = {result}')
                        case 9:
                            result = radians(num1)
                            print(f'Result:radians({num1}) = {result}')
                        case 10:
                            result = degrees(num1)
                            print(f'Result:degrees({num1}) = {result}')
                        case 11:
                            num2 = float(input('Enter pow:'))
                            result = powing(num1, num2)
                            print(f'Result:pow({num1},{num2}) = {result}')
                case 3:
                    print('Exiting...')
                    break
        except ValueError:
            print('Sorry, you need to enter one of proposed values')       
calculating()
