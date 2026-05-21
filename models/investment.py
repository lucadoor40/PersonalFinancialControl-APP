class Investment:
    def __init__(self, name, investment_total,investment_month):
        self.name=name
        self.investment_total=investment_total
        self.investment_month=investment_month

        self.investment_final=(
            self.investment_total+self.investment_month
        )
        self.monthly_income_without_work=(
            (self.investment_total + self.investment_month) * 0.01
        )




    def to_dict(self):
        return {
            'name':self.name,
            'investment total':self.investment_total,
            'investment month':self.investment_month,
            'investment final':self.investment_final,
            'monthly income without work':self.monthly_income_without_work
        }