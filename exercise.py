
# ? 1 Write a Python program to print the following string in a specific format (see the output).
# print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")


#? 2 Write a Python program to find out what version of Python you are using.
# import pickle
# import sys
# print("Version of Python in this Laptop is: " + sys.version + ".")


#? 3 Write a Python program to display the current date and time.
# import datetime
# now = datetime.datetime.now()
# print ("Current date and time : ")
# print (now.strftime("%Y-%m-%d %H:%M:%S"))


#? 4 Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2).
# import math
# x1 = int(input('Enter a number: '))
# x2 = int(input('Enter a number: '))
# y1 = int(input('Enter a number: '))
# y2 = int(input('Enter a number: ')) 

# distance = math.sqrt((x1 - y1)**2 + (x2 - y2)**2)

# print(distance)

#? 5 Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.
# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# c = int(input("Enter a number: "))
# sum = a + b + c

# if a == b == c:
#     print(3 * sum)
# else:
#     print(sum)

#? 6 Write a Python program to check whether a file path is a file or a directory.
# import os
# path = input("Enter a file path: ")
# if os.path.isdir(path):
#     print("Its a directory")
# elif os.path.isfile(path):
#     print("Its a file")
# else:
#     print("Its a special file.")

#? 7 Write a Python program that checks whether a specified value is contained within a group of values.
# values = [1, 3, 7, 8]
# while True:
#     specified_value = int(input("Enter any value: "))
#     if specified_value in values:
#         print(True)
#     elif specified_value not in  values:
#         print(False)
#     else:
#         print("Invalid Input")

#? 8  Write a Python program to solve (x + y) * (x + y).
# x = int(input("Enter a Number: "))
# y = int(input("Enter a Number: "))

# program = (x + y)*(x + y)
# print(program)

#? 9 Write a Python program to get the users environment.
# import os
# import pprint

# print(os.environ)
# print("Prettyy print")
# pprint.pprint(dict(os.environ), width = 1)

#? 10 Write a Python program to extract the filename from a given path.
# import os
# print(os.path.basename('/Users\sanab\Desktop\Python-Exercise'))

#? 11 Write a Python program to convert all units of time into seconds.
# y = 31536000 
# m = 2628288
# d = 86400
# h = 3600
# mn =  60

# units = input("Enter unit (year/month/day/hour/minutes) ")
# number = int(input('Value you want to convert in seconds '))
# # print(number)
# if units == 'year':
#     print(number * y)
# elif units == 'month':
#     print(number * m)
# elif units == 'day':
#     print(number * d)
# elif units == 'hour':
#     print(number * h)
# elif units == 'minutes':
#     print(number * mn)
# else:
#     print("Invalid Input")

#? 12 Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2
# list_one = set(['White', 'Red', 'Purple', 'Brown'])
# list_two = set(['White', 'Pink', 'Yellow', 'Brown'])
# list_three = {'White', 'Red', 'Purple', 'Brown'}
# list_four = {'White', 'Pink', 'Yellow', 'Brown'}
# program1 = list_one - list_two
# program2 = list_three - list_four

# print(program1)
# print(program2)

#? 13  Write a Python function to check whether a number is divisible by another number. Accept two integer values from the user.
# def multiple(m,n):
#     if m % n == 0:
#         print(True)
#     else:
#         print(False)
# multiple(45, 5)

#! Another Part

# ? 1 Write a Python program that creates all possible strings using the letters 'a', 'e', 'i', 'o', and 'I'. Ensure that each character is used only once.
# import random
# list = ["a", "e", "i", "o", "u"]
# random.shuffle(list)
# print("".join(list))

# ? 2 Write a Python program to count the number of each character in a text file.
# import collections
# import pprint
# file_name = input("File Name: ")
# # with open (file_name, 'r') as info
# info = open (file_name, 'r') 
# count = collections.Counter(info.read().upper())
# value = pprint.pformat(count)
# print(value)

# ? 3 Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.
# def sequence(data):
#     if len(set(data)) == len(data):
#         return True 
#     else:
#         return False
# print(sequence([1,2,3,4]))
# print(sequence([2,4,5,5,7,9]))

#? 4 Write a Python program to make combinations of 3 digits.
# numbers = []
# for num in range(1000):
#     num = str(num).zfill(3)
# print(num)
# numbers.append(num)

#? 5 Write a Python program to get a list of locally installed Python modules.
# import pkg_resources as lib
# installed_packages = lib.working_set
# installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
#     for i in installed_packages])
# for m in installed_packages_list:
#     print(m)

#? 6 Write a Python program to check the sum of three elements (each from an array) from three arrays is equal to a target value. Print all those three-element combinations.
# ! Sample data:
# ! /*
# ! X = [10, 20, 20, 20]
# ! Y = [10, 20, 30, 40]
# ! Z = [10, 30, 40, 20]
# ! target = 70
# ! */
# import itertools
# from functools import partial
# X = [10, 20, 20, 20]
# Y = [10, 20, 30, 40]
# Z = [10, 30, 40, 20]
# T = 70

# def check_sum_array(N, *nums):
#     if sum(x for x in nums) == N:
#         return (True, nums)
#     else:
#         return(False, nums)
    
# pro = itertools.product(X,Y,Z)
# func = partial(check_sum_array, T) 
# sums = list(itertools.starmap(func, pro))

# result = set()
# for s in sums:
#     if s[0] == True and s[1] not in result:
#         result.add(s[1])
#         print(result)

#? 7 Write a Python program to get all possible two-digit letter combinations from a 1-9 digit string.
# def letter_combinations(digits):
#     if digits == "":
#         return []
#     string_maps = {
#         "1": "abc",
#         "2": "def",
#         "3": "ghi",
#         "4": "jkl",
#         "5": "mno",
#         "6": "pqrs",
#         "7": "tuv",
#         "8": "wxy",
#         "9": "z"
#     }
#     result = [""]
#     for num in digits:
#         temp = []
#         for an in result:
#             for char in string_maps[num]:
#                 temp.append(an + char)
#         result = temp
#     return result
# string = "47"
# print(letter_combinations(string))

#? 8 Write a Python program to get the third side of a right-angled triangle from two given sides.
# import math
# side_input = input("Input the side you want to find: (h/p/b)")

# if side_input == "b":
#     h = int(input("Enter a Value: "))
#     p = int(input("Enter a Value: "))
#     h_square = h**2
#     p_square = p**2
#     base = (h_square - p_square)
#     print("This is the value of base: "+ str(math.sqrt(base)))
# elif side_input == "p":
#     h = int(input("Enter a Value: "))
#     b = int(input("Enter a Value: "))
#     h_square = h**2
#     b_square = b**2
#     perpendicular = (h_square - b_square)
#     print("This is the value of base: "+ str(math.sqrt(perpendicular)))
# elif side_input == "h":
#     b = int(input("Enter a Value: "))
#     p = int(input("Enter a Value: "))
#     b_square = b**2
#     p_square = p**2
#     hypotenuse = (b_square + p_square)
#     print("This is the value of base: "+ str(math.sqrt(hypotenuse)))

#? 9 Write a Python program to find the median among three given numbers.
#! Method 1
# x = int(input("Enter any Number: ")) 
# y = int(input("Enter any Number: "))
# z = int(input("Enter any Number: "))

# if (x < y and x > z) or (x > y and x < z):
#     print(x)
# elif (y < z and y > x) or (y > z and y < x):
#     print(y)
# elif (z > x and z < y) or (z < x and z > y):
#     print(z)
# else:
#     print(False)
#! Method 2
# x = int(input("Enter any Number: ")) 
# y = int(input("Enter any Number: "))
# z = int(input("Enter any Number: "))

# if x < y and x > z:
#     print(x)
# elif y < z and y > x:
#     print(y)
# elif z > x and z < y:
#     print(z)
# elif x > y and x < z:
#     print(x)
# elif y > z and y < x:
#     print(y)
# elif z < x and z > y:
#     print(z)
# else:
    # print(False)

#? 10 Write a Python program to check whether three given lengths (integers) of three sides form a right triangle. Print "Yes" if the given sides form a right triangle otherwise print "No".
# a = int(input("Enter any Value: ")) 
# b = int(input("Enter any Value: "))
# c = int(input("Enter any Value: "))

# a2 = a**2
# b2 = b**2
# c2 = c**2

# if a > b and a > c:
#     if a2 == b2 + c2:
#         print(True)
#     else:
#         print(False)
# elif b > a and b > c:
#     if b2 == a2 + c2:
#         print(True)
#     else:
#         print(False)
# elif c > a and c > b:
#     if c2 == a2 + b2:
#         print(True)
#     else:
#         print(False)
# else:
#     print("Invalid Input")

#? 11  Write a program to compute the radius and the central coordinate (x, y) of a circle which is constructed from three given points on the plane surface.
# print("Input x1,y1,x2,y2,x3,y3,xp,yp:")
# x1, y1, x2, y2, x3, y3, x4, y4 = map(float, input().split())
# print('PQ and RS are parallel.' if abs((x2 - x1)*(y4 - y3) - (x4 - x3)*(y2 - y1)) == 0 else 'PQ and RS are not parallel')

#? 12 Write a Python program that accepts six numbers as input and sorts them in descending order.
# print("Input 6 numbers you want in descending order: ")
# nums = list(map(float, input().split()))
# nums.sort()                 #from smaller to greater
# nums.reverse()                 #from greater to smaller
# print(*nums)

#? 13 There are two circles C1 with radius r1, central coordinate (x1, y1) and C2 with radius r2 and central coordinate (x2, y2).
#! Write a Python program to test the followings -
#! "C2 is in C1" if C2 is in C1
#! "C1 is in C2" if C1 is in C2
#! "Circumference of C1 and C2 intersect" if circumference of C1 and C2 intersect
#! "C1 and C2 do not overlap" if C1 and C2 do not overlap and
#! "Circumference of C1 and C2 will touch" if C1 and C2 touch
# import math
# print('input x1, y1, x2, y2, r1, r2')
# x1,y1,x2,y2,r1,r2 = [float(i) for i in input().split()]
# d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
# if d <= r1-r2:
#     print("C2 is in C1")
# elif d <= r2-r1:
#     print("C1 is in C2")
# elif d < r1+r2:
#     print("Circumference of C1  and C2  intersect")
# elif d == r1+r2:
#     print("Circumferance will touch")
# else:
#     print("Do not overlap")


