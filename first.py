import numbers


num1 = int(input("Enter an integer number : "))
num2 = int(input("Enter an integer number : "))
num3 = int(input("Enter an integer number : "))
num4 = int(input("Enter an integer number : "))
num5 = int(input("Enter an integer number : "))
num6 = int(input("Enter an integer number : "))

li_number = [num1, num2, num3, num4, num5, num6]
filtered = []
even_list = []
odd_list = []
average = 0
count = 0

for number in li_number:
    if number >= 0:
        filtered.append(number)
for number in filtered:
    if number % 2==0:
        even_list.append(number)
        average = average + number
        count = count + 1
    elif number % 2 !=0:
        odd_list.append(number)


maximumEven = max(even_list)

print("Sum of ODD ",sum(odd_list))
print("Average of EVEN ", average/count)

filter_odd_list = (odd_list)
filter_odd_list.sort()
if range(len(filter_odd_list)):
  print ("Smallest ODD: ", filter_odd_list[0])
else:
        print ('Smallest ODD: no Odd')

print("Largest EVEN: ",maximumEven)


