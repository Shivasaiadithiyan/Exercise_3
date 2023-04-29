from vector import vector
import random

"""
This module contains the testcases for
vector class.

"""

vector1=vector(5)
vector2=vector(5)
vector3=vector(4)
vector4=vector(4)

#generating random values for all 4 vectors
for index in range(len(vector1)):
    vector1[index]=random.randint(10,100)
    vector2[index]=random.randint(10,100)

for index in range(len(vector3)):
    vector3[index]=random.randint(10,100)
    vector4[index]=random.randint(10,100)

#testing addition,subtraction,multiplication,division
#for vectors with same dimension.
print("-"*70)
print("adding 2 vectors of same dimension.")
print(vector1)
print(vector2)
print("Result")
print(vector1 + vector2)

print("-"*70)
print("subtracting 2 vectors of same dimension.")
print(vector3)
print(vector4)
print("Result")
print(vector3 - vector4)

print("-"*70)
print("multiplying 2 vectors of same dimension.")
print(vector3)
print(vector4)
print("Result")
print(vector3 * vector4)

print("-"*70)
print("division 2 vectors of same dimension.")
print(vector1)
print(vector2)
print("Result")
print(vector1 / vector2)

#testing addition,subtraction,multiplication,division
#for vectors of different dimension.
try:
    print("-"*70)
    print("adding 2 vectors of different dimension.")
    print(vector4)
    print(vector1)
    print("Result")
    print(vector1 + vector4)
except ValueError:
    print("vector dimensions are not same.")

try:
    print("-"*70)
    print("subtracting 2 vectors of different dimension.")
    print(vector2)
    print(vector3)
    print("Result")
    print(vector2 - vector3)
except ValueError:
    print("vector dimensions are not same.")

try:
    print("-"*70)
    print("multiplying 2 vectors of different dimension.")
    print(vector1)
    print(vector3)
    print("Result")
    print(vector1 * vector3)
except ValueError:
    print("vector dimensions are not same.")

try:
    print("-"*70)
    print("dividing 2 vectors of different dimension.")
    print(vector2)
    print(vector4)
    print("Result")
    print(vector2 / vector4)
except ValueError:
    print("vector dimensions are not same.")

print("-"*70)