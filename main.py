# Task 1

# num1 = int(input('Enter your first number: '))
#
# num2 = int(input('Enter your second number: '))
#
# num3 = int(input('Enter your third number: '))
#
# total=num1+num2+num3
#
# print(f"Your total is {total}")

# Task 2

# diagonal1=int(input('Enter length on diagonal length 1: '))
#
# diagonal2=int(input('Enter length on diagonal length 2: '))
#
# rhombusArea=(diagonal1*diagonal2)/2
#
# print(f"Your rhombus area is {rhombusArea}")

# Task 3

# userNumber=int(input("Enter any 4-digit number: "))
#
# num1=userNumber // 1000
# print(num1)
#
# num2=userNumber % 1000 // 100
# print(num2)
#
# num3=userNumber // 10 % 10
# print(num3)
#
# num4=userNumber % 10
# print(num4)
#
# result=num1*num2*num3*num4
#
# print(f"Your total result is {result}")

# Task 4

# num1 = int(input("Enter first digit: "))
# num2 = int(input("Enter second digit: "))
# num3 = int(input("Enter third digit: "))

# userChoice = input("Choose your option: highest, lowerst or average value?\n")

# if userChoice == "highest":
#     if num1 > num2 > num3:
#         print(num1)
#     elif num2 > num3 > num1:
#         print(num2)
#     else:
#         print(num3)
# elif userChoice == "lowerst":
#     if num1 < num2 < num3:
#         print(num1)
#     elif num2 < num3 < num1:
#         print(num2)
#     else:
#         print(num3)
# else:
#     print((num1 + num2 + num3) / 3)

#  Task 5

# metersEntered = float(input("Enter number of meters to convert: "))
# convertTo = input("Choose system to convert: miles, inches or yards?\n")

# if convertTo == "miles":
#     print(metersEntered * 0.00062137)
# elif convertTo == "inches":
#     print(metersEntered * 39.370)
# else:
#     print(metersEntered * 1.0936)

# Task 6
# try:
#     dayChoice = int(input("Choose, please, the day of the week by entering number from 1 to 7: "))
#
#     match dayChoice:
#         case 1:
#             print("It's Monday")
#         case 2:
#             print("It's Tuesday")
#         case 3:
#             print("It's Wednesday")
#         case 4:
#             print("It's Thursday")
#         case 5:
#             print("It's Friday")
#         case 6:
#             print("It's Saturday")
#         case 7:
#             print("It's Sunday")
#         case _:
#             print("Incorrect menu item")
#
# except Exception as e:
#     print("Enter only numbers, please!")
#     print(f"ValueError: {e}")

#  Task 7
# try:
#     while True:
#         num1=int(input("Enter first number: "))
#         num2=int(input("Enter second number: "))
#
#         if num1 > num2:
#             print (num2, num1)
#         elif num2>num1:
#             print(num1, num2)
#         else:
#             print("Numbers are equal")
#             break
# except Exception as e:
#     print("Enter digits only!")
#     print(f"Error: {e}")

# Task 8

# try:
#     while True:
#         num1=float(input("Enter first number: "))
#         num2=float(input("Enter second number: "))
#         actions=input("What to do with numbers: +, -, *, /? ")
#         sumnums=(num1+num2)
#         extractnums=(num1-num2)
#         multiplynums=(num1*num2)
#         dividenums=(num1/num2)
#
#         match actions:
#             case '+':
#                 print(sumnums)
#             case '-':
#                 print(extractnums)
#             case '*':
#                 print(multiplynums)
#             case '/':
#                 if num2 !=0:
#                     print(dividenums)
#                 else:
#                     break
#
# except ZeroDivisionError as error:
#     print("Division by 0!")
#     print(f"ZeroDivisionError occurred: {error}")
# except Exception as e:
#     print("Enter digits only!")
#     print(f"Error: {e}")