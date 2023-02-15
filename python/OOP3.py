class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def print_info(self):
        print(f"Name: {self.name}\nID: {self.id}")

class FullTimeEmployee(Employee):
    def __init__(self, name, id, monthly_salary):
        super().__init__(name, id)
        self.monthly_salary = monthly_salary

    def calculate_monthly_salary(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, id, day_salary, work_day):
        super().__init__(name, id)
        self.day_salary = day_salary
        self.work_day = work_day

    def calculate_day_salary(self):
        return self.day_salary * self.work_day


e1 = FullTimeEmployee("Adam", "114115", 10000)
e2 = PartTimeEmployee("Bert", "115114", 200, 30)

e1.print_info()
e2.print_info()

print(e1.calculate_monthly_salary())
print(e2.calculate_day_salary())