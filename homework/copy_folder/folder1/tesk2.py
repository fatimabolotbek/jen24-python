# list_num = [a for a in range(1,51)]
# even_sum = 0
# for a in list_num:
#     if a%2==0:
#      even_sum += a
    
# print(even_sum)




# list_num = [a for a in range(1,51) if a % 2 != 0]
# odd_num = 1
# for a in list_num:
#   odd_num *= a
# print(list_num)   
# print("odd numbers:", odd_num)




#print(max(range(51)))




# nections = [
#     ('Amsterdam', 'Dublin', 100),
#     ('Amsterdam', 'Rome', 140),
#     ('Rome', 'Warsaw', 130),
#     ('Minsk', 'Prague', 95),
#     ('Stockholm', 'Rome', 190),
#     ('Copenhagen', 'Paris', 120),
#     ('Madrid', 'Rome', 135),
#     ('Lisbon', 'Rome', 170),
#     ('Dublin', 'Rome', 170),
#     ]

# city_finding = [name for name in connections if conn[1] == 'Rome']
# #name is just the place holder variable 
# #name[1] is the second list inthe list  if that qgual to rome
# # this checks if the second element of the tuple is equal to the string 'Rome'
# time_rome = sum(name[2] for name in city_finding) / len(city_finding) 
# #with sum we are finding all times summ and deviding it to length of the rome variable 
# #here we are geting all sum of the times conn[2] and / deviding it by the romes how many romes we have 
# print(f"{len(city_finding)} connections lead to Rome with an average flight time of {time_rome} minutes")
# #here f stands for specifing that the value is a floating-point number. and geting the tome-rome output
# # f is the string holder we can use f to write values get output from variables inside of the string 
# print(city_finding)
# print(len(city_finding)

# 
# num1 = 10
# num2 = 8
# num3 = 12
# if num1 < num2:
#    if num1 < num3:
#        print('smallest is:', num1)
# elif num2 < num1:
#    if num2 < num3:
#        print('smallest is:', num2)
# elif num3 < num1:
#    if num3 < num2:
#        print('smallest is:', num3)
# else:
#    print('else')



# pet="dog"
# for i in range(0,len(pet)):
#     print(pet[i])


# pet = "panda"
# for i in range(1,len(pet)):
#     print(pet[i])


# x = 7
# if x % 2 == 1:
#   print('x is an odd number')


# num = 3

# while num > 0:
#   print('Hello')
#   num = num + (num - 2)

# hash = 1

# while hash <= 6:
# 	hash += hash
# 	print('#', end='')
# else:
# 	print('#')

# x = "      "   
# print(len(x))


# x = 1 / 2 + 3 // 3 + 4 ** 2

#print(x)

# z = y = x = 1

# print(x, y, z, sep='*')



#print(3 / 5)

x = 2

y = 4

print(x + y)