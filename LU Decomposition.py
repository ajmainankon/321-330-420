import numpy as np

def LUDecomposition(M):
  #Initializing the Upper matrix that has to be simplified
  U = M
  #Initializing the Lower matrix as an identity matrix (all diagonals are 1)
  L = np.identity(U.shape[0])

  for i in range(1,len(U)):

    for j in range(i):

      fac=M[i,j]/M[j,j]
      temp=M[j]*fac
      U[i]=M[i]-temp
      L[i,j]=fac
 
  return L, U

b = np.array([[2,-1,3],
              [4,2,1],
              [-6,-1,2]])


L, U = LUDecomposition(b)
print("L and U of Matrix b: \n",L,"\n\n",U,"\n\n")


#####################


import numpy as np
L = np.array([[1,0,0],
              [2,1,0],
              [-3,-1,1]])

U = np.array([[2,-1,3],
              [0,4,-5],
              [0,0,6]])

B = np.array([4,1,2])


#Forward Substitution process
B_L = np.zeros(B.shape[0]) 

for i in range(L.shape[0]):
  summation=0
  for j in range(L.shape[0]):
    if i == j:
      B_L[j] = B[j] - summation
      B_L[j] = B_L[j]/L[i,j]
      break
    else:
      summation = summation + L[i,j]*B_L[j]
      

####Backward Substitution, your task is to complete this task
#Flip the U and B_L matrices if necessary using np.flip(array, axis) method
#U = np.flip(U, 0)
#U = np.flip(U, 1)
#B_L = np.flip(B_L)

B_LU = np.zeros(B.shape[0]) 
for i in range(U.shape[0]):
  summation=0
  for j in range(U.shape[0]):
    if i == j:
      B_LU[j] = B_L[j] - summation
      B_LU[j] = B_LU[j]/U[i,j]
      break
    else:
      summation = summation + U[i,j]*B_LU[j]
#Use U and B_L to populate B_LU, just like how L and B was used to populate B_L in forward substitution

#Place your code here (You may need nested loop)

################################################################


final_result = np.flip(B_LU)

print(final_result)
