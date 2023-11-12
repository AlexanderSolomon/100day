

print("what was the tolat bill?")
total_bill = float(input())

print("what percentage tip would you like to give? 10,12,15" )
tip = float(input()) / 100
print(tip)

print("how many people will split the bill?")
people = int(input())
bill_pr_person = float(total_bill/people)



total_cost = round(float(total_bill) * float(tip) /int(people) + bill_pr_person,2) 
print(f"each person is paying: {total_cost}")
