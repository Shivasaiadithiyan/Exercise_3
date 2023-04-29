"""
This module provides a class that represents a vector object
whiich has  dimension and coordinates as members and
add(), sub(), mul(), truediv(), as
member functions.

This is a part of the exercises given under the 
course UIT2201 (Programming and Data Structures).

This is a sample implementation and may contain bugs!
We have tried to follow good coding practices but don't
claim that this source code is perfect!

Your comments and suggestions are welcome.

Created on Fri Apr 20 2023

Revised on Sat Apr 25 2023

Original Author: S.Shiva sai adithiyan <shivasaiadithiyan2210687@ssn.edu.in>

$Id: 115571315$

"""


class vector:
    """
    A class to represent a Vector.
    ...

    Attributes
    ------------
    dim: int
        represents the length of the vector.

    coord: array
        contains the coordinates as a secquence
    
    Methods
    -----------

    __len__()
        provides the length of a vector object.

    __getitem__()
        function which allow to acces the 
        vector coordinates using index.

    __setitem__()
        function which is used to assign
        values for coordinates using index.

    __add__()
        function to add 2 vector object 
        of same dimension.

    __sub__()
        function to subtract 2 vector
        objects of same dimension.
    
    __mul__()
        function to multiply 2 vector
        objects of same dimension.
    
    __truediv__()
        function to divided 2 vector 
        objects of same dimension.
    
    
    """

    def __init__(self,length=0) -> None:
        self.dim=length
        self.coord=[0]*length
    #end of constructor __init__().


    
    def __len__(self):
        """
        function which returns the 
        length of a vector.

        returns: int
    
        """
        return self.dim
    #end of method __len__().

    
    def __getitem__(self,index):
        """
        function which is used to fetch
        a particular coordinate of vector
        using index.

        self: vector object
        index: int

        """
        return self.coord[index]
    #end of method __getitem__().

    
    def __setitem__ (self,index,value):
        """
        function which is used to assign
        a particular coordinate using index.

        self: vector object
        index: int
        value: float
        
        """
        self.coord[index]=value
    #end of __setitem__().

    
    def __add__ (self,other):
        """
        function wuhich adds two vector objects
        having same dimension.

        self: vector object
        other: vector object

        returns a vector object

        """

        if self.dim!=other.dim:
            raise ValueError
        
        result=vector(self.dim)

        for coord in range(self.dim):
            result.coord[coord]=self.coord[coord] + other.coord[coord]
        
        return result
    #end od method __add__().

    
    def __sub__ (self,other):
        """
        function wuhich subs two vector objects
        having same dimension.

        self: vector object
        other: vector object

        returns a vector object

        """

        if self.dim!=other.dim:
            raise ValueError
        
        result=vector(self.dim)

        for coord in range(self.dim):
            result.coord[coord]=self.coord[coord] - other.coord[coord]
            
        return result
    #end of method __sub__().

    
    def __mul__ (self,other):
        """
        function wuhich multiply two vector objects
        having same dimension.

        self: vector object
        other: vector object

        returns a vector object

        """

        if self.dim!=other.dim:
            raise ValueError
        
        result=vector(self.dim)

        for coord in range(self.dim):
            result.coord[coord]=self.coord[coord] * other.coord[coord]

        return result
    #end of method __mul__().

    
    def __truediv__ (self,other):
        """
        function wuhich division two vector objects
        having same dimension.

        self: vector object
        other: vector object

        returns a vector object

        """


        if self.dim!=other.dim:
            raise ValueError
        
        result=vector(self.dim)

        for coord in range(self.dim):
            result.coord[coord]=int(self.coord[coord] / other.coord[coord])
        
        return result
    #end of method __truediv__().


    def __str__(self) -> str:
        """
        function which overides the inbuilt 
        print() function.

        """
        return str(self.coord)
    #end of method __str__().


#using random library to generate random values to vector.
import random

if __name__=="__main__":
    
    # Following code will be executed only when this Python
    # file is run directly.  Code will be ignored if this
    # file is imported by another Python source.
    
    #creating 4 vectors for testing
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
#end of program
