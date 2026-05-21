class Salary:
    def __init__(self,company,salary):
        self.company=company
        self.salary=salary

    def to_dict(self):
        return {
            'company':self.company,
            'salary':self.salary
        }