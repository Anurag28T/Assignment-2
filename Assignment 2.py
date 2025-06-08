#Task 1

number=int(input("Enter an integer:"))
if number % 2 ==0:
    print(f"The Number {number} is even.")
else:print(f"The Number {number} is odd.")

#Task 2

total_sum=0
for number in range (1,51):
    total_sum+=number
    print("The sum of numbers from 1 to 50 is :",total_sum)

