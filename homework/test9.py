# def function_merge(lis1,lis2):
#     sorted_lst = []
#     for x in lis1:
#         if x in lis2 not in lis1:
#             sorted_lst.append(x)

#     sorted_lst.sort()

#     return sorted_lst 


# lis1 = [12,9,14,7,15]
# lis2 = [12,9,22,7,23]
# print(function_merge(lis1,lis2))


# def colculator_num():
#     return[7,9]
# num1 = int(input("Enter your number"))
# num2 = int(input("Enter second number"))
# print(input("Enter the operation +, -, *, /"))
# if colculator_num = '+':
#     return
#     if colculator_num = '-':
#         return
#         if colculator_num = '*':
#             return
#             else colculator_num ='/'


# def addition(num1,num2):
#     return num1 + num2

# def substring(num1,num2):
#     return num1 - num2

# def multiply(num1,num2):
#     return num1 * num2

# def divison(num1,num2):
#     try:
#         return num1 / num2
#     except ZeroDivisionError:
#         print("Cannot divide by zero")



# def calculator():
#     inp1 = int(input("First Number"))
#     inp2 = int(input("Second Number"))
#     inp3 = input("Please give the +-*/")


#     if inp3 == "+":
#         print(addition(num1, num2))
#     elif inp3 == "-":
#         print(substring(num1,num2))
#     elif inp3 == "*":
#         print(multiply(num1, num2))
#     elif inp3 == "/":
#         print(divison(num1 / num2))
#     else:
#         print(”The result of the operation“)



 
def unlimited_num(args):
    unlimited_num = sum(args) / len(args)
    return unlimited_num

args = [20,10,50,60]
print(unlimited_num(args))



 





