#Calculate eigenvectors and eigenvalues for 2x2 matrices
import numpy as np
import random
import math

def input_matrix():
    print('Input your 2X2 matrix one number at a time.')
    numbers=[0.0,0.0,0.0,0.0]
    numbers[0]=input('Input the first number in the first row and press Enter:')
    numbers[1]=input('Input the second number in the first row and press Enter:')
    numbers[2]=input('Input the first number in the second row and press Enter:')
    numbers[3]=input('Input the second number in the second row and press Enter:')
    
    for i in range(0,4):
        try:
            numbers[i]=int(numbers[i])
        except ValueError:
            try:
                numbers[i]=float(numbers[i])
            except ValueError:
                numbers[i]=random.randint(0,100)
    matrix=np.array([[numbers[0],numbers[1]],[numbers[2],numbers[3]]])
    print('This is your matrix:')
    print(matrix)
    return matrix

def find_eigenvalue(matrix):
    a=1
    b=-1*(matrix[0][0]+matrix[1][1])
    c=matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    d=b*b-4*a*c
    l=[]
    if d>0:
        l.append((-b+math.sqrt(d))/2)
        l.append((-b-math.sqrt(d))/2)
    if d==0:
        l.append(-b/2)
    if d<0:
        l.append((-b+math.sqrt(d)*1j)/2)
        l.append((-b-math.sqrt(d)*1j)/2)
    print(l)
    return l

def plug_value_into_matrix(value, matrix):
    return np.array([[matrix[0][0]-value,matrix[0][1]],[matrix[1][0],matrix[1][1]-value]])

def row_reduce_operations(matrix):
    for i in range(0,2):
        if (matrix[0][0]==0):
            #swap
            matrix=np.array([matrix[1],matrix[0]])
        if (matrix[0][0]*matrix[1][0]!=0):
            #row op
            matrix[1][1]=-matrix[0][1]*(matrix[1][0]/matrix[0][0])+matrix[1][1]
            matrix[1][0]=0
        #if (matrix[0][1]*matrix[1][1]!=0):
            #row op
            #matrix[0][1]=0
            
    if (matrix[0][0]!=0):
        matrix[0][1]/=matrix[0][0]
        matrix[0][0]=1
    #if (matrix[1][1]!=0):
        #scale to 1
        #matrix[1][0]/=matrix[1][1]
        #matrix[1][1]=1
    return matrix
    
def find_eigenvector(matrix):
    vector=[]
    if matrix[0][0]!=0:
        vector=[-matrix[0][1], 1]
    return vector
   
#referenced: https://www.emathhelp.net/calculators/linear-algebra/eigenvalue-and-eigenvector-calculator/?i=%5B%5B1%2C2%5D%2C%5B3%2C4%5D%5D&steps=on
#referenced: https://gist.github.com/DingWeizhe/d087c6869a596fc01e04
if __name__ == '__main__':
    matrix=input_matrix()
    print('These are your eigenvalues:')
    vals=find_eigenvalue(matrix)
    print('------------------------')
    for val in vals:
        print('For eigenvalue ', val)
        m=plug_value_into_matrix(val, matrix)
        print('Plug the eigenvalue into the matrix')
        print(m)
        m2=row_reduce_operations(m)
        print('Obtain the rref of the matrix')
        print(m2)
        v=find_eigenvector(m2)
        print('Solve to find the eigenvector')
        print(v)
        print('------------------------')