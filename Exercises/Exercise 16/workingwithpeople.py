from employee import Employee
from person import Person
from customer import Customer


#create an instance of the Employee object. passing the following args to the constructor
employee1 = Employee('Phil','Daly',40,200345,12)

#change the employee's first and last name using setter and function that parses a string and splits on space
employee1.fullname = 'John smith'

#use the weekly_wage mothod to work out how much the employee earnt based on the number of hours
employee1.weekly_wage(40)
print(f'employee {employee1.fullname} worked {employee1.hours_worked} hours last week at a rate of £{employee1.hourly_wage} an hour, earning: £{employee1.pay}')
print(f'This user\'s email is {employee1.email}' )


employee2 = Employee('John','Davis',24,344050,10)
employee2.weekly_wage(24)
print(f'employee {employee2.fullname} worked {employee2.hours_worked} hours last week at a rate of £{employee2.hourly_wage} an hour, earning: £{employee2.pay}')
print(f'This user\'s email is {employee2.email}' )

customer1 = Customer('Phil','Daly', 100000, 'Bread')
print(f'The customer {customer1.first_name} {customer1.last_name} ordered {customer1.purchase}')

person1 = Person('Phil', 'Daly', 34, 'going for Walks on the beach')
print(f'The person in question is name {person1.first_name} {person1.last_name} {person1.age} he loved all sorts of things but his main hobby is: {person1.hobbies}')