import fpdf

"""
Class structures
"""


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


class PdfReport:

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = fpdf.FPDF("P")
        pdf.add_page("P")
        pdf.set_font("Arial", "B", 28)
        pdf.image('house.png', 10, 5, 10, 10)
        pdf.cell(100, 50, "This is the bill for " + bill.period, ln=1)
        pdf.set_font("Arial", "I", 16)
        pdf.cell(100, 30, "Bill total amount £" + str(bill.amount), ln=1)
        pdf.cell(100, 10, flatmate1.name + " owes £" + str(flatmate1.pays(bill, flatmate2)), ln=1)
        pdf.cell(100, 10, flatmate2.name + " owes £" + str(flatmate2.pays(bill, flatmate1)), ln=1)
        pdf.output(self.filename)


"""

Implementation

"""

bill1 = Bill(amount=200, period="June")
billy = Flatmate("Billy", 20)
john = Flatmate("John", 27)

mypdf = PdfReport("billpdf.pdf")
mypdf.generate(billy, john, bill1)

