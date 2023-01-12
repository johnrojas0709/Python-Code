# John Rojas U13874585

# code will receive user input. User will decide what sequence to use and then what the number of values will be.
# for loops, lists, and functions utilized. 
''' I he code for this project represents my own, independent work. I have neither given nor 
received help on this exam from other students'''

class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

class Engineer:
    def __init__(self, name, employee_id, title, hours):
        Employee.__init__(self, name, employee_id)
        self.title = title
        self.hours = hours
        self.payrate = 0
        self.week_pay = 0 
        self.setPayRate()
        self.setweekly_pay()
    
    def setPayRate(self):
        self.dict_payrate = {'Engineering Intern' : 20, 'Senior Engineer' : 45, 'Lead Engineer' : 70}
        for key in self.dict_payrate:
            if self.title == key:
                self.payrate = self.dict_payrate[key]
                return self.payrate
    
    def setweekly_pay(self):
        self.week_pay = self.payrate * self.hours
        if self.hours > 40:
            self.week_pay = (40 * self.payrate) + ((self.hours - 40) * (self.payrate * 1.5))
            return self.week_pay
        else:
            return self.week_pay
            

    def __str__(self):
        return 'Payroll Data for employee ' + self.employee_id + ':\n' \
            + self.name + '\'s pay this week is: ${:,.2f}'.format(self.week_pay)


def main():
    employee_name = input('Enter employee\'s name: ')
    employee_id = input('Enter employee\'s ID number: ')
    title = input('Enter the employee\s title: ')
    num_hours_worked = int(input('Enter the number of hours the employee worked this week: '))
    while num_hours_worked < 0 or num_hours_worked > 60:
        print('Invalid. Hours worked cannot be negative or grater than 60.')
        num_hours_worked = int(input('Enter the number of hours the employee worked this week: '))
    
    employee_info = Engineer(employee_name, employee_id, title, num_hours_worked)
    print(employee_info)

main()


