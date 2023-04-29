"""
This module provides a class that represents a matrix object
which has rows and coloumns as members and
addition, subtraction, multiplication, determinant as
member functions.

This is a part of the exercises given under the 
course UIT2201 (Programming and Data Structures).

This is a sample implementation and may contain bugs!
We have tried to follow good coding practices but don't
claim that this source code is perfect!

Your comments and suggestions are welcome.

Created on Fri Apr 20 2023

Revised on Sat Apr 26 2023

Original Author: S.Shiva sai adithiyan <shivasaiadithiyan2210687@ssn.edu.in>

$Id: 115571315$

"""

from vector import vector
"""
Importing vector class from the vector.py file

"""

class matrix:
    
    """
    A class to represent a Matrix.
    ...

    Attributes
    ------------
    row : int
        rows present in the matrix.
    coloumn : int
        coloumns present in the matrix.
    
    Methods
    -----------

    __setitem__()
        function to set values to element in matrix
        with the help of index.

    __getitem__()
        function to display element of matrix 
        with the help of index.

    __len__()
        function which display the number of elements present
        in the matrix.

    __eq__()
        function which checks whether 2 matrices are
        equal in magnitude.
  
    __add__()
        function to add 2 matrices of same dimension.

    __sub__()
        function to subtract 2 matrices of same dimension.

    __mul__()
        function to multiply 2 matrices of 
        compatible dimensions.

    det()
        function to find determinant of square matrices.

    gen_values()
        function to generate random values for all elements
        of a matrix.    
    
    """

    def __init__(self,r=0,c=0) -> None:
        
        self.row=r
        self.coloumn=c
        self.matrix=[]
        for object in range(r):
            col=vector(c)
            self.matrix.append(col)
    #end of constructor __int__().



    def __setitem__(self,r,c,val):
        """
        function which allows assign values
        using index on matrix objects.

        r: int -indicates row number of matrix
        c: int -indicates coloumn number of matrix
        val: float -value to be assigned

        
        """
        self.matrix[r][c]=val
    #end of method __setitem__().



    def __getitem__(self,r,c):
        """
        function to display a particular element 
        using index.

        r: int -row of the matrix
        c: int -coloumn of the matrix

        returns the element present at row {r} and 
        coloumn {c} of matrix {self}.
        """

        return self.matrix[r][c]
    #end of method __getitme__().



    def __len__ (self):
        """
        function which returns the number of elements present
        in the matrix

        returns: int -the number of elements
        """

        return self.row*self.coloumn
    #end of __len__() method.



    def __add__ (self,other):
        """
        function which adds two matrices
        having same dimension and returns a new matrix

        self: object of matrix class.
        other: object of matrix class.
        
        returns a object of matrix data type.
        """

        if self.row != other.row or self.coloumn != other.coloumn:
            raise ValueError

        result=matrix(self.row,self.coloumn)

        for item1 in range(self.row):
            for item2 in range(self.coloumn):
                result.matrix[item1][item2]=self.matrix[item1][item2]+other.matrix[item1][item2] 

        return result
    #end of __add__() method.

    
    def __sub__(self,other):
        """
        function which subtracts two matrices
        having same dimension and returns a new matrix

        self: object of matrix class.
        other: object of matrix class.
        
        returns a object of matrix data type.
        """

        if self.row != other.row or self.coloumn != other.coloumn:
            raise ValueError 

        result=matrix(self.row,self.coloumn)

        for item1 in range(self.row):
            for item2 in range(self.coloumn):
                result.matrix[item1][item2]=self.matrix[item1][item2] - other.matrix[item1][item2] 

        return result
    #end of method __sub__().


    def __mul__ (self,other):
        """
        function which multiplies two matrices
        which are compatible for multiplication
        and returns a new matrix

        self: object of matrix class.
        other: object of matrix class.
        
        returns a object of matrix data type.
        """

        if self.coloumn !=other.row:
            raise ValueError 
        
        result=matrix(self.row,other.coloumn)

        for item1 in range(self.row):
            for item2 in range(other.coloumn):
                for item3 in range(other.row):
                    result.matrix[item1][item2]+= self.matrix[item1][item3]*other.matrix[item3][item2]

        return result
    #end of method __mul__().


    def __eq__(self, other) -> bool:
        """
        function which checks whether two matrices 
        are equal in magnitude and returns True 
        or False

        self: object of matrix class.
        other: object of matrix class.
        
        returns True if matrices are equal in magnitude
        otherwise False.
        """

        if self.row != other.coloumn or self.coloumn != other.coloumn:
            return False
        else:
            for index1 in range(self.row):
                for index2 in range(self.coloumn):
                    if self.matrix[index1][index2]!= other.matrix[index1][index2]:
                        return False
        return True
    #end of method __eq__().



    def gen_values(self,low=10,high =100):
        """
        function which generates random values for all
        element of a matrix data type

        self: object of matrix data type.
        low: int -lower bound of random value
        high: int -higher bound of random value

        """
         
        import random
        if low > high:
            raise ValueError 

        for item1 in range (self.row):
            for item2 in range(self.coloumn):
                self.matrix[item1][item2]= random.randint(low,high)
        #end of method gen_values().    
    

    def det (self):
        """
        function to compute the determinant of a square
        matrix.

        numpy library is used for this computation

        returns : float 
        """
        if self.row !=self.coloumn:
            raise ValueError 
        else:
            import numpy
            return numpy.linalg.det(self.matrix)
    #end of method det().

    

    def __str__(self) -> str:
        """
        funciton which defines the inbuilt print()
        function.

        returns the matrix atribute of matrix data type.
        
        """
        final_str=''
        for i in range(self.row):
            for j in range(self.coloumn):
                final_str+=str(self.matrix[i][j])
                final_str+="\t"        
            final_str+="\n"
        return final_str
    #end of __str__() method.


   


if __name__ == "__main__":

    # Following code will be executed only when this Python
    # file is run directly.  Code will be ignored if this
    # file is imported by another Python source.

    try:
        #creating 4 matrices for test cases
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
    
    except ValueError:
        pass

    print("-"*70)

#end of program