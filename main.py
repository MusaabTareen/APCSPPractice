# from business import NetIncome
# from business import MarkupPercent
# from business import NetWorth
# from business import BreakEvenPoint
# from business import ROI
# from business import ProfitMargin
from paymenthistory import payment_history
from amountsowed import amounts_owed
from newcredit import new_credit
from lengthofcredithistory import length_of_credit_history
from creditmix import credit_mix


#print(MarkupPercent(120,100),"%")
#print("$",NetWorth(200,100))
#print("$",NetIncome(120,100))
#print(BreakEvenPoint(200,100,150))
#print(ROI(120,100),"%")
#print(ProfitMargin(200,100),"%")

PHweight = 35
AOweight = 30
NCweight = 10
LCHweight = 15
CMweight = 10

print("Payment History Questions:")
payment_history()

print("Amounts Owed Questions:")
amounts_owed()

print("New Credit Questions:")
new_credit()

print("Length of Credit History Questions:")
length_of_credit_history()

print("Credit Mix Questions:")
credit_mix()
  

