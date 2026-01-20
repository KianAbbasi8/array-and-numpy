import numpy as np 
arr=np.arange(100) # this use for the creating array 0 to 99
arr=arr.reshape(10,10) # this will break into row and column 25 row and 4 colum this must be equll to 100 or number that you have entered 
print(arr)
print(arr.shape,arr.ndim)
sarr=arr.reshape(5,5,4) # array split into 5  blocks / samlpes and each block has 5 rows and each row has 4 coloum : logic is block * row * colomn
print(f"these are reshaped  :\n{arr}")
