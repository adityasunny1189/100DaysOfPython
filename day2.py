numStr = input("Enter a two digit number: ")
finalAns = int(numStr[0]) + int(numStr[1])
print(finalAns)

# Challanage - 2

age = int(input("Enter your age: "))
years_left = 90 - age
days_left = years_left * 365
months_left = years_left * 12
weeks_left = years_left * 54
print(f"You have {days_left} days, {months_left} months and {weeks_left} weeks left in your life")

# Final Project

bill_amount = float(input("Enter the total bill: "))
tip = int(input("Enter the tip 12, 15, 20: "))
no_of_friends = int(input("Enter the no of persons: "))
total_bill_with_tip = bill_amount + bill_amount * (tip / 100)
each_person_share = total_bill_with_tip / no_of_friends
print(f"Each person share is {each_person_share}")
