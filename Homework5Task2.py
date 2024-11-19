class Contact:
    def __init__(self, surname, name, age, mob_phone, email):
        self.surname = surname
        self.name = name
        self.age = age
        self.mob_phone = mob_phone
        self.email = email

    def get_contact(self):
        return f"{self.surname}, {self.name} - Age: {self.age}, Mob Phone: {self.mob_phone}, Email: {self.email}"

    def sent_message(self, message):
        print(f"Message sent to {self.surname} {self.name}: {message}")


class UpdateContact(Contact):
    def __init__(self, surname, name, age, mob_phone, email, job):
        super().__init__(surname, name, age, mob_phone, email)
        self.job = job

    def get_contact(self):
        base_contact = super().get_contact()  #
        return f"{base_contact}, Job: {self.job}"


    def sent_message(self, message):
        super().sent_message(message)
        print(f"Additional info-Job: {self.job}): {message}")



contact_info = Contact("Doe", "John", 30, "1234567890", "johndoe@example.com")
print(contact_info.get_contact())  
contact_info.sent_message("Hi there!") 

updated_contact_info = UpdateContact("Doe", "Jane", 28, "9876543210", "janedoe@example.com", "Software Engineer")
print(updated_contact_info.get_contact())  
updated_contact_info.sent_message("Hello again!")

# __dict__==========
print(contact_info.__dict__)
print(updated_contact_info.__dict__)
d = updated_contact_info.__dict__
for k,i in d.items():
    print(f"{k}: {i}")

#  __base__==========
print(Contact.__base__)
print(UpdateContact.__base__)

# __bases__==========
print(Contact.__bases__)
print(UpdateContact.__bases__)

#  hasattr(), getattr(), setattr(), delattr()

#  hasattr()
print(hasattr(Contact, "job"))

# getattr()
print(getattr(updated_contact_info, "job"))
print('================================================================')
f = getattr(updated_contact_info, "job")
print(f)

# setattr()
setattr(updated_contact_info, "job", "Senior Software Engineer")
print(getattr(updated_contact_info, "job"))

# delattr()

delattr(updated_contact_info, "job")
print(hasattr(updated_contact_info, "job"))
print(hasattr(Contact, "job"))