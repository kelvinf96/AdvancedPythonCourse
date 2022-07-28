class Bill:

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:

    def __init__(self, name, days):
        self.name = name
        self.days = days

    def pays(self, bill, flatmate2):
        """
        P's days over total days, multiply this by bill.
        """
        total_days = self.days + flatmate2.days
        i_pay = round((self.days / total_days) * bill.amount, 2)
        return i_pay

