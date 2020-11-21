# understand what question is asking
# write a program which will sum of all items in the list from the user

# list_1 = [1, 2, 3, 4]                 Output = 10
# list_1 = [1, Nishant, 2, Ranjan]      Output = 1Nishant2Ranjan
# list_3 = [Nishant, Ranjan]            Output = Nishant Ranjan

# sum = mathematical terms means number or interger
# combine or concatenate = strings

# list_1 = [1, 2, 3, 4]                 Output = 10
# list_1 = [1, 2, 3, 4, 5]              Output = 15

list = [4,5,6,7]  # from the user

sum = 0
for i in list:
    sum +=i
print(sum)

# from the user = paramters or arguments

def sum_list(list_param):
    sum = 0
    for i in list_param:
        sum +=i
    print(sum)


list = [4, 5, 6, 7]
sum_list(list)

# expecting user to send n numbers
# add those numbers in list
# sum of the items of the list

# input 1
# input 1, 2, 3, 4

# input total_numbers_for_list
# input 5

# input 1
# input 2
# input 3
# input 4
# input 5

lst1 = []
x = int(input("enter total numbers: "))

for i in range(x):
    y = int(input("enter number: "))
    lst1.append(y)

sum_list(lst1)
