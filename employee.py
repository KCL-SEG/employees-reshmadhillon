
"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""


class Employee:
    def __init__(self, name, Commission):
        self.name = name
        self.myCommission = Commission
        self.contract_pay = 0
        self.total_pay = 0

    def get_pay(self):
        return self.total_pay

    def __str__(self):
        return self.name

    def get_contract_pay(self):
        return self.contract_pay

    def calc_contract_pay(self):
        pass

    def calc_total_pay(self):
        self.calc_contract_pay()
        self.total_pay = self.get_contract_pay() + self.myCommission.get_commission_pay()

class Salary_Employee(Employee):
    def __init__(self, name, salary, myCommission):
        super().__init__(name, myCommission)
        self.salary = salary
        super().calc_total_pay()

    def calc_contract_pay(self):
        self.contract_pay = self.salary

class Hourly_Employee(Employee):
    def __init__(self, name, hours, pay_per_hour, myCommission):
        super().__init__(name, myCommission)
        self.hours = hours
        self.pay_per_hour = pay_per_hour
        super().calc_total_pay()

    def calc_contract_pay(self):
        self.contract_pay = self.hours * self.pay_per_hour

class Commission():
    def __init__(self):
        pass

    def get_commission_pay(self):
        return self.commission_pay

class Bonus_Commission(Commission):
    def __init__(self, commission):
        super().__init__()
        self.commission_pay= commission

class Contract_Commission(Commission):
    def __init__(self, contract_number, pay_per_commission):
        super().__init__()
        self.contract_number = contract_number
        self.pay_per_commission = pay_per_commission
        self.commission_pay = self.contract_number * self.pay_per_commission

class No_Commission(Commission):
    def __init__(self):
        super().__init__()
        self.commission_pay = 0

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Salary_Employee('Billie', 4000, No_Commission())
#print(billie.__str__(),billie.get_pay())

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Hourly_Employee('Charlie', 100, 25, No_Commission())
#print(charlie.__str__(),charlie.get_pay())

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Salary_Employee('Renee', 3000, Contract_Commission(4,200))
#print(renee.__str__(),renee.get_pay())

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Hourly_Employee('Jan', 150, 25, Contract_Commission(3,220))
#print(jan.__str__(),jan.get_pay())

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Salary_Employee('Robbie', 2000, Bonus_Commission(1500))
#print(robbie.__str__(),robbie.get_pay())

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Hourly_Employee('Ariel', 120, 30, Bonus_Commission(600))
#print(ariel.__str__(),ariel.get_pay())
