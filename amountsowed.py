global amounts_owed_score
global cards_balance_score


def amounts_owed():
  def amount_owed():
    global amounts_owed_score
    amount_still_owed = int(input("How much do you still owe on all of you accounts? "))
    if amount_still_owed == 0:
      amounts_owed_score = 3
      print("You're amount owed rank is", amounts_owed_score)
    elif amount_still_owed <= 5000:
      amounts_owed_score = 2
      print("You're amount owed rank is",amounts_owed_score)
    elif amount_still_owed <= 10000:
      amounts_owed_score = 1
      print("You're amount owed rank is",amounts_owed_score)
    else:
      amounts_owed_score = 0
      print("You're amount owed rank is",amounts_owed_score)
  def cards_balance():
    global cards_balance_score
    amount_past_due = int(input("How many past due items are on you're credit report? "))
    if amount_past_due == 0:
      cards_balance_score = 3
      print("You're past due items score is",cards_balance_score)
    elif amount_past_due <= 4:
      cards_balance_score = 2
      print("You're past due items score is",cards_balance_score)
    elif amount_past_due <= 9:
      cards_balance_score = 1
      print("You're past due items score is",cards_balance_score)
    else:
      cards_balance_score = 0
      print("You're past due items score is",cards_balance_score) 
  def average_amounts_owed():
    global amounts_owed_score
    global cards_balance_score
    average_payment_history = ((amounts_owed_score + cards_balance_score)/2)
    print("Payment History Average Score = ", average_payment_history)
  amount_owed()
  cards_balance()
  average_amounts_owed