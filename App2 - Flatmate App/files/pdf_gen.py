import os

import fpdf
import webbrowser


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
        pdf.set_font("Arial", size=16)
        pdf.cell(100, 10, flatmate1.name + " owes £" + str(flatmate1.pays(bill, flatmate2)), ln=1)
        pdf.cell(100, 10, flatmate2.name + " owes £" + str(flatmate2.pays(bill, flatmate1)), ln=1)
        pdf.output(self.filename)
        webbrowser.open('file://' + os.path.realpath(self.filename))

