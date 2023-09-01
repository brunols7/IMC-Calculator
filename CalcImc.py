#IMC Calc - by brunols7
from time import sleep

print("Welcome to IMC Calculator!")
sleep(1)

weight = float(input("Enter your weight(kg) - (ex 64.7): "))
height = float(input("Enter your height(m) - (ex 1.80): "))

calc1 = height * height
result = weight / calc1

print("=-"*15)
print("Calculating...")
print("=-"*15)
sleep(2)

if (result <= 18.5):
    print("{:.2f}, Your status is Underweight.".format(result))
elif (result <= 24.9):
    print("{:.2f}, Your status is Normal.".format(result))
elif (result <= 39.9):
    print("{:.2f}, Your status is Overweight".format(result))
elif (result >= 40):
    print("{:.2f}, Your status is Obese".format(result))