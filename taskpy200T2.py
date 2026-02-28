# task_Py200_T2 - Program to chaeck if the number is Positive, Negative, or Zero
# Author : Akanksha Singh

# Take input from user
num = float(input("Enter a number:"))

#check condition
if num > 0:
    print(f"your intered number {num} is positive.")

elif num < 0:
    positive_value = -num
    print(f"your intered number {num} was negative, however positive value of your number is {positive_value}.")

else:
    print(f"Your entered number {num} is zero.")
