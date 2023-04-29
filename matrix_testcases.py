"""
This module contains the testcases
for matrix class.
"""

from matrix import matrix

matrix1=matrix(3,3)
matrix2=matrix(3,3)
matrix3=matrix(4,3)
matrix4=matrix(3,4)

#generating random values for all 4 matrices
matrix1.gen_values()
matrix2.gen_values()
matrix3.gen_values()
matrix4.gen_values()


print("-"*70)

#addition of matrices with same dimension
print("Addition of matrices of same dimension: ")
print(matrix1)
print(matrix2)
print("Result")
print(matrix1+ matrix2)

print("-"*70)
try :
    #addition of matrices with different dimension
    print("Addition of matrices of different dimension: ")
    print(matrix1)
    print(matrix3)
    print("Result")
    print(matrix1 + matrix3)

except ValueError:
    print("Given matrices are not compatible for addition")


print("-"*70)

#subtraction of matrices with same dimension
print("Subtraction of matrices of same dimension: ")
print(matrix1)
print(matrix2)
print("Result")
print(matrix1 - matrix2)

print("-"*70)
try :
    #Subtraction of matrices with different dimension
    print("Subtraction of matrices of different dimension: ")
    print(matrix1)
    print(matrix3)
    print("Result")
    print(matrix1 - matrix3)

except ValueError:
    print("Given matrices are not compatible for subtraction")


print("-"*70)

#Multiplication of 2 compatible matrices
print("Multiplication of 2 matrices ")
print(matrix1)
print(matrix2)
print("Result")
print(matrix1 * matrix2)

print("-"*70)
try :
    #multiplication of incompatible matrices
    print("multiplication of incompatible matrices")
    print(matrix1)
    print(matrix3)
    print("Result")
    print(matrix1 * matrix3)

except ValueError:
    print("Given matrices are not compatible for multiplication")

print("-"*70)

#finding determinants of square matrices
print("finding determinants of square matrices")
print(matrix2)
print("Result")
print(matrix2.det())

print("-"*70)
try :
    #Determinant of rectangular matrices
    print("Determinant of rectangular matrices")
    print(matrix4)
    print("Result")
    print(matrix4.det())

except ValueError:
    print("Only square matrices are eligible for determinants.")
