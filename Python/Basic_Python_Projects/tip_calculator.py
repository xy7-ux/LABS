print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))

tip = int(input("What percentage tip would you like to give? 10 12 15 "))

people = int(input("How many people to split the bill? "))

bill_plus_tip = (bill + (bill * (tip * 0.01)))
each_person_pay = bill_plus_tip / people
rounded_each_pearson = round(each_person_pay, 2)


print(f"Each person should pay: {rounded_each_pearson} $.")

