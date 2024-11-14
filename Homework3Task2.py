class English:
    def __init__(self, language_name="English"):
        self.language_name = language_name

    @staticmethod
    def greeting():
        return "Good day, my friend!"

    def __str__(self):
        return self.greeting()  


class Spanish:
    def __init__(self, language_name="Spanish"):
        self.language_name = language_name

    @staticmethod
    def greeting():
        return "Buen día, mi amigo!"

    def __str__(self):
        return self.greeting()  


def hello_friend(english, spanish):
    return f'{english.greeting()} and {spanish.greeting()}'



eng = English()
spa = Spanish()


print(eng)             
print(spa)             
print(hello_friend(eng, spa))  


    

    
