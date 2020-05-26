A=[[900,900,940,1100,1500,1800],[910,1120,1200,1130,1900,2000],[0,0,0,0,0,0]]
s=1
for i in range(0,len(A[0])):
    k=i
    j=i+1
    if A[2][i] != 0:
        continue
    else:
        while j < len(A[0]):
            if A[0][j] >= A[1][k] and A[2][j] == 0:
                A[2][j] = s
                k = j
            j += 1
        A[2][i] = s

        print(A[2][:])

    s+=1
print(A)

