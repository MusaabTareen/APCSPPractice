global amount_owed_score
global amount_past_due_score
global percent_payments_ontime_score



def payment_history():
  def amount_owed():
    global amount_owed_score
    amount_still_owed = int(input("How much do you still owe? "))
    if amount_still_owed == 0:
      amount_owed_score = 3
      print("You're amount owed rank is", amount_owed_score)
    elif amount_still_owed <= 5000:
      amount_owed_score = 2
      print("You're amount owed rank is",amount_owed_score)
    elif amount_still_owed <= 10000:
      amount_owed_score = 1
      print("You're amount owed rank is",amount_owed_score)
    else:
      amount_owed_score = 0
      print("You're amount owed rank is",amount_owed_score)
  def past_due_items():
    global amount_past_due_score
    amount_past_due = int(input("How many past due items are on you're credit report? "))
    if amount_past_due == 0:
      amount_past_due_score = 3
      print("You're past due items score is",amount_past_due_score)
    elif amount_past_due <= 4:
      amount_past_due_score = 2
      print("You're past due items score is",amount_past_due_score)
    elif amount_past_due <= 9:
      amount_past_due_score = 1
      print("You're past due items score is",amount_past_due_score)
    else:
      amount_past_due_score = 0
      print("You're past due items score is",amount_past_due_score) 
  def percent_of_payments_on_time():
    global percent_payments_ontime_score
    payments_ontime = int(input("What percentage of payments have you made on time? "))
    if payments_ontime >= 95:
      percent_payments_ontime_score = 3
      print("You're payments on time rank is", percent_payments_ontime_score)
    elif payments_ontime >= 75:
      percent_payments_ontime_score = 2
      print("You're payments on time rank is", percent_payments_ontime_score)
    elif payments_ontime >= 50:
      percent_payments_ontime_score = 1
      print("You're payments on time rank is", percent_payments_ontime_score)
    else:
      percent_payments_ontime_score = 0
      print("You're payments on time rank is", percent_payments_ontime_score)
  def average_payment_history():
    global amount_owed_score
    global amount_past_due_score
    global percent_payments_ontime_score
    average_payment_history = ((amount_owed_score + amount_past_due_score + percent_payments_ontime_score)/3)
    print("Payment History Average Score = ", average_payment_history)
  amount_owed()
  past_due_items()
  percent_of_payments_on_time()
  average_payment_history()