import requests

class Employee:

    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def fullname(self):
        return f"{self.first} {self.last}"
    
    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        return self.pay
    
    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'