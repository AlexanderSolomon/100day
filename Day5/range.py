
#print all even numbers added up
value = 5
# for number in range(1,10):
#     print(number)
counter = 0
for numbers in range(value+1):
    m = numbers % 2
    if m == 0:
        counter += numbers
    print(counter)