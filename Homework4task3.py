# Опишіть клас співробітника, який вміщує такі поля: ім'я, прізвище, відділ і рік початку роботи. Конструктор має генерувати виняток, якщо 
# вказано неправильні дані. Введіть список працівників із клавіатури. 
# Виведіть усіх співробітників, які були прийняті після цього року
class EmployeeApearMistake(Exception):
        pass
class Employee:
    def __init__(self, name, surname, department, start_year):
        
        self.name = name
        self.surname = surname
        self._department = department
        self._start_year = start_year
        self.employee_data = {}
        if surname in self.employee_data: 
            raise EmployeeApearMistake("Employee already exists!")

    class EmployeeApearMistake(Exception):
        pass

    def add_employee(self, surname, name,department, start_year):
        if surname not in self.employee_data.keys():
            self.employee_data[surname] = {'surname': surname,'name':name, 'department': department, 'start_year':start_year}
            return f'Employee {name} {surname} added successfully'
        else:
            return f'Employee  {self.employee_data[surname]} already exists'
        
    def find_employee(self, employee):
        if employee not in self.employee_data.keys():
                raise EmployeeApearMistake("was not found")
        else:
                return f'{self.employee_data[employee]} was found'    
    
        
   
    def get_employees_after_year(self, year):
        result = []
        for surname, data in self.employee_data.items():
            if data['start_year'] >= year:
                result.append(f"{data['name']} {data['surname']}: {data['start_year']}")
        return "\n".join(result) if result else "No employees found after this year"
                
    
    def __str__(self):
        if not self.employee_data:
            return "No employees in the system"
        finish = "\n".join(
            f"{data['surname']}: {data['start_year']}" for surname, data in self.employee_data.items()
        )
        return f'Employees:\n{finish}'

while True:
    try:
        print('Welcome to HR menu. Print 1.To add employees.2. To serarcy. 3.Filtr of th yera of work.4-q to quit.:')
        choice = input('Enter choice')
        if choice == 'q':
            break
        elif choice == '1':
            while True:
                emp = Employee(None, None, None,None)
                name = input("Enter name:")
                surname = input("Enter surname:")
                department = input("Enter department:")
                start_year = int(input("Enter start year of work:"))
                print(emp.add_employee(surname, name, department, start_year))
                break
        elif choice == "2":
            while True:
                surnamesearch = input("Search surname;")
                print(emp.find_employee(surnamesearch))
                break
        elif choice == "3":
            while True:
                year = int(input("Enter year to filter:"))
                print(emp.get_employees_after_year(year))
    except EmployeeApearMistake as e:
        print(f"Error: {e}")
  