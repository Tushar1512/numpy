# ARRAY CREATING

import numpy as np

# -------------------------------------------1st Array == ( 1-D )-------------------------------------------------------

# x=[1,2,3,4,5]
# y = np.array(x)                                                         # type 1
# y1 = np.array([1,2,3,4,5])                                              #type 2
#
# print(y,y1)
# print("",type(y),"\n",type(y1),"\n",type(x),"\n")
#
# l =[]
#
# for i in range(1,5):
#     INT_1 = int(input("Enter a Number:-"))
#     l.append(INT_1)
# print(np.array(l))
#
# print(y.ndim,y1.ndim)

#-------------------------------------------------- 2nd Array == ( 2-D ) -----------------------------------------------

# ar2 = np.array([[1,2,3,4,5],[1,2,3,4,5]])
# print(ar2)
# print(ar2.ndim)                                                        # give to type of array  ===== .ndim   |
# print(ar2.shape)                                                       # give to shape of array ===== .shape  |
# print(ar2.size)                                                        # give to size of array  ===== .size   |


#-------------------------------------------------- 3nd Array == ( 3-D ) -----------------------------------------------

# ar3 = np.array([[[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]])
# print(ar3)
# print(ar3.ndim)

#----------------------------- nth Array == ( N-D ) --------------------------------------------------------------------

# arn = np.array([1,2,3], ndmin =2)
# print(arn)
# print(arn.ndim)


#----------------------------create Array with numpy function-----------------------------------------------------------
#
# 1.Array filled with 0's
#
# 1-D
# ar_zero = np.zeros(4)
# print(ar_zero)
#
#2-D
# ar_zero1 = np.zeros((3,4))
# print(ar_zero1)


# 2. Array filled  with 1's
#
# ar1 = np.ones(3)
# print(ar1)


# 3. Array filled empty
#
# ar = np.empty(4)
# print(ar)

# 4. Range Array
#
# ar = np.arange(4)
# print(ar)

# 5. Array diagonal element filled wioth 1's
#
# ar = np.eye(5)
# print(ar)

# 6. Create an array with value that are spaced linearly in a specified interval

# ar = np.linspace(0,10,num=2)
# print(ar)


# Numpy Array with Random Numbers
#
#
# 1. rand() , range 0 to 1                                              # rand()
# var = np.random.rand(4)
# print(var)
#
# 2. randn() , range = close to zero , positive and negative            #randn()
# var1 = np.random.randn(1)
# print(var1)
#
# 3. ranf()  range = [ 0.0 , 1.0 ]                                      #ranf()
# var = np.random.ranf(2)
# print(var)
#
# randint() generate a random num given range (min,max,total value)    #randint()
# var = np.random.randint(1,5,2)
# print(var)


#  Data-type  ( chack and change )
#
#
# tushar = np.array([1,2,5,0])
# print("Data type is :- ",tushar.dtype)        # how to check data type = .dtype()
#
# type - 0 (change to data type)
# tushar = np.array([1,2,5,6,0],dtype=np.int8)  # how to change data type = dtyp = np.(data type)
# print("Data type is :- ",tushar.dtype)
#
# type - 1 (change to data type)
# t = np.array([1,3,85,],dtype ="f")            # data type change short hand method
# print(t.dtype)
#
#
# type - 2 (chang eto data type)
# t = np.array([4.5,5.6,9.3])
# tex = np.float32(t)                          # data type change short hand method
# print(tex.dtype)
#
#
# type -3 (change to  data type)
# t= np.array([1,2,6,8])
# tt = t.astype(float)
# print(t,"their data type :-",t.dtype)
# print(tt,"their data type :-",tt.dtype)



