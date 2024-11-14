class Temperature:
    def __init__(self, temperature_cel: float):
        self.temperature_cel = temperature_cel 

   
    def get_temperature_cel(self):
        return f'Temperature in Celsius: {self.temperature_cel:.2f}°C'
    
   
    def set_temperature_cel(self, temperature_cel):
        self.temperature_cel = temperature_cel
    
    
    def get_temperature_fahr(self):
        temperature_fahr = self.temperature_cel * 9 / 5 + 32
        return f'Temperature in Fahrenheit: {temperature_fahr:.2f}°F'
    
  
    def set_temperature_fahr(self, temperature_fahr):
        self.temperature_cel = (temperature_fahr - 32) * 5 / 9

    
    def temperature_both(self):
        return f'{self.get_temperature_cel()}, {self.get_temperature_fahr()}'
    
    def __str__(self):
        return self.temperature_both()
    

temp = Temperature(25) 
print(temp)  

temp.set_temperature_cel(6)
print(temp)  

temp.set_temperature_fahr(100)
print(temp) 





















# class Celsius:
#     def __init__(self, temperature_cel:int):
#         self.temperature_cel = temperature_cel

#     def get_temperature_cel(self):
#         return f'Temperature in Celsius {self.temperature_cel}'

#     def __str__(self):
#         return self.get_temperature_cel()
    


# class Fahrenheit:
#     def __init__(self, temperature_fahr:int):
#         self.temperature_fahr = temperature_fahr
    
#     def get_temperature_fahr(self):
#         return f'Temperature in Fahrenheit {self.temperature_fahr}'
#     def __str__(self):
#         return self.get_temperature_fahr()
    
# def convert_temperature(Celsius,Fahrenheit):
#     if convert_temperature(Celsius):
#         return Fahrenheit(Celsius.temperature_cel * 9/5 + 32)
#     elif convert_temperature(Fahrenheit):
#         return Celsius((Fahrenheit.temperature_fahr - 32) * 5/9)
#     else:
#         return 'Invalid input'
    
