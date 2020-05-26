from random import randint
A = [[],[]]
A[0] = [randint(0,10) for i in range(0,10)]
A[1] = [0 for i in range(0,10)]
print(A)

l = None
r = None
for i in range(1,9):
    l=i
    r=i
    for j in range(i-1,-1,-1): # finding the left largest element's index
        if A[0][j] > A[0][l]:
            l=j
    for j in range(i+1,9,1): # finding the right largest element's index
        if A[0][j] > A[0][r]:
            r=j;
    if A[0][l] < A[0][r]: # assigning which is less among left largest and right leargest
        A[1][i] = A[0][l]-A[0][i] # we need to minus the quantity of that element
    else:
        A[1][i] = A[0][r]-A[0][i]
print(A)


