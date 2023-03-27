class Employee:
    def __init__(self, first_name, last_name, age, employee_number, hourly_wage):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.employee_number = employee_number
        self.hourly_wage = hourly_wage

    def weekly_wage(self, hours_worked):
        self.hours_worked = hours_worked
        self.pay = self.hours_worked * self.hourly_wage

# use the @property to allow method to be accessed like an attribute
    @property
    def fullname(self):
        return (f'{self.first_name} {self.last_name}')

    @property
    def email(self):
        return (f'{self.first_name}.{self.last_name}@email.com')

# use the .setter method to allow setting the vale of attributes of the object in another way
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first_name = first
        self.last_name = last