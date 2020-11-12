# # # # # # # # # python = ['cool']
# # # # # # # # # x = python in python

# # # # # # # # # print(x)


# # # # # # # # print('''\
# # # # # # # #  A
# # # # # # # #  B
# # # # # # # #  C
# # # # # # # #  ''')
# # # # # # # length = int(input("enter the length of the rectangle \n"))
# # # # # # # breadth = int(input('enter the breadth of the rectangle \n'))

# # # # # # # if length == breadth:
# # # # # # #     print("it is a sqaure")
# # # # # # # else:
# # # # # # #     print("it is not sqaure")
# # # # # # a = int(input("enter the number \n"))
# # # # # # b = int(input("enter the number \n"))

# # # # # # if a > b:
# # # # # #     print("a is greater")
# # # # # # else:
# # # # # #     print("b is greatest")
# # # # # quantity = int(input('enter the quantity'))
# # # # # if quantity * 100 > 1000:
# # # # #     purchasecost1 = (quantity * 100) - (.1 * quantity * 100)
# # # # #     print(f"price with discount {purchasecost1}")
# # # # # else:
# # # # #     purchasecost2 = quantity * 100
# # # # #     print(f"no discount and ypur amount is {purchasecost2}")
# # # # salary = int(input("enter the salary"))
# # # # year = int(input("enter the year"))
# # # # if year > 5:
# # # #     netamount = (salary + (0.5 * salary))
# # # #     print(f" congratulation!!! {netamount}")
# # # # else:
# # # #     print(f"Good luck for the future {salary}")
# # # marks = int(input("enter the marks"))

# # # if marks > 80:
# # #     print("A")
# # # elif marks < 80 and marks >= 60:
# # #     print("B")
# # # elif marks < 60 and marks >= 50:
# # #     print("C")
# # # elif marks < 50 and marks >= 45:
# # #     print("D")
# # # elif marks < 45 and marks >= 25:
# # #     print("E")
# # # else:
# # #     print("F")
# # p1 = int(input("enter the age of first person"))
# # p2 = int(input("enter the age of second person"))
# # p3 = int(input("enter the age of third person"))

# # if p1 > p2 and p1 > p3:
# #     print("p1 is oldest person")
# # elif p2 > p3:
# #     print("p2 is oldest")
# # else:
# #     print("p3 is oldest")
# x = int(input("enter the first number"))
# if x < 0:
#     output = x * -1
#     print(output)
# else:
#     output = x 
#     print(output)
tcls = int(input("enter the total days"))
atcls = int(input("enter the attended days"))
medi_cause = input("medical reason")
atclsper = ((atcls // tcls)*100)
if medi_cause == 'Y':
    print("you are allowed")
else:
    if atclsper >= 75:
        print("you are allowed to seat")
    else:
        print("you are not  allowed")
