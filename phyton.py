"""
Xetalari tutmaq ucun:
try >> calisacaq kod bu blogun icinde olur
except >> kodun run zamani cixacaq xetalari ele aliriq
finally >> her zaman calisacaq kod setri


2 cur xeta var:
1. Sintaksis xeta
print("Salam')
"""

# number = int(input("Reqem daxil edin: "))
# print(number + 5)

# try:
#     number = int(input("Reqem daxil edin: "))
#     print(number + 5)

# except:
#     print("Xeta !!!")

# finally:
#     print("Sonunda...")


# while True:
#     try:
#         number = int(input("Reqem daxil edin: "))
#         print(number + 5)
#         successfully = True

#     except ValueError:
#         print("Xais edirik reqem daxil edin !!!")
#         successfully = False

#     if successfully:
#         print("Tebrikler...")
#         break


"""
Modallar (Paketler)
2 cur modal var
1. Built in >> Python daxilinde movcud olan modullar (math, random, os, sys)
2. Userin ozunun yaradib istifade etdiyi modallar

modallar .py fayllarinda movcud olan kodlar, funksiyalardir
"""

# import math
# print(math.pi)
# print(math.sqrt.__doc__)
# print(math.pow.__doc__)
# print(math.sqrt(64))
# print(int(math.sqrt(64)))
# print(math.isqrt(80))
# print(math.ceil(6.2))
# print(math.floor(6.9))


# import random

# print(random.random())
# print(random.randint(20, 50))
# print(random.randrange(10, 20, 3))
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# print(random.choice(list))
# print(random.sample(list, 2))


# import platform

# print(platform.platform())
# print(platform.architecture())
# print(platform.machine())
# print(platform.system())



# from math import isqrt as kokalti
# print(kokalti(64))




# import IlkModul
# print(IlkModul.__doc__)
# IlkModul.salamla()


# import InputFunctions
# print(InputFunctions.string_goster.__doc__)
# print(InputFunctions.string_goster())
# print(InputFunctions.reqem_goster())








import random
import math

def numbersm():
    numbers = []
    for _ in range(5):
        numbers.append(random.randint(20, 50))
    
    print("Random reqem:", numbers)
    
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            numbers[i] = math.pow(numbers[i], 2)
    
    print("poü Reqem", numbers)

numbersm()











