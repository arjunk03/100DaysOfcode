print("wecome to the tip calculator ")
bill = float(input("What was the total bill amount? \n"))
perc = float(input("How much tip would you like to give? 10, 12 or 15? \n"))
num_of_people = float(input("How many people to split the bill? \n"))

bill_per_person = round((bill + bill * (perc / 100)) / num_of_people, 2)
print(bill_per_person)
