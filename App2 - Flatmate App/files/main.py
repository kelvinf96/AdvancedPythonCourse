
from billing import Flatmate, Bill

from pdf_gen import PdfReport

fm1_name = input("Enter flatmate 1's name: ")
fm1_days = int(input("How many days did " + fm1_name + " stay? "))

fm2_name = input("\nEnter flatmate 2's name: ")
fm2_days = int(input("How many days did " + fm2_name + " stay? "))

bill_period = input("\nWhat is the billing month ? ")
bill_amount = int(input("What is the bill total? "))

generate_bill = Bill(bill_amount, bill_period)
fm1 = Flatmate(fm1_name, fm1_days)
fm2 = Flatmate(fm2_name, fm2_days)

mypdf = PdfReport("billpdf.pdf")
mypdf.generate(fm1, fm2, generate_bill)

