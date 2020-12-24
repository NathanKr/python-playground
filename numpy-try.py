import numpy as np
print("np.__version__ : \n",np.__version__)

vec1 = np.array([1, 2, 3, 4, 5]) # [1 2 3 4 5] is created 
print("vec1 : \n",vec1)
print("vec1.size : \n",vec1.size)
vec2 = np.arange(5) # [0 1 2 3 4] is created 
print("vec2 : \n",vec2)
print("vec2.size : \n",vec2.size)

print("np.dot(vec1,vec2) : ",np.dot(vec1,vec2)) # multiply vectors item by item and sum -> 40

vec1 = np.append(vec1,6)
print("vec1 after np.append(vec1,6)",vec1)

# create matrix from vector
mat_vec1 = np.array([vec1]) # matrix 1x6 
mat_vec1_transpose = mat_vec1.T # matrix 6x1

print("vec1'*vec1",np.matmul(mat_vec1_transpose,mat_vec1)) # 6 x 6

# ************** handle matrix
mat1 = np.array([[1 , 0] , [3 , 4]])
print("mat1.shape : \n",mat1.shape) # number rows , number cols -> 2 , 2
print("mat1 : \n",mat1)
mat2 = np.array([[0 , 5] , [6 , 7]])
print("mat2 : \n",mat2)

# ----- multiply matrix
print("np.matmul(mat1,mat2) : \n",np.matmul(mat1,mat2))

# ----- transpose matrix
print("mat1.T : \n",mat1.T)

# ----- inverse matrix
print("inverse mat1 \n",np.linalg.inv(mat1))
print("mat1*inverse mat1 is identity\n",np.matmul(mat1,np.linalg.inv(mat1)))
