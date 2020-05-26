A = [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]
A = [[1,2,3],[4,5,6],[7,8,9]]
imin = 0;
imax = len(A)-1;
jmin = 0;
jmax = len(A[0])-1

while(imin != imax and jmin != jmax):
      j=jmin
      while(j<=jmax):
          print(A[imin][j])
          j+=1;
      imin+=1

      i=imin;
      while(i<=imax):
          print(A[i][jmax])
          i+=1;
      jmax-=1;

      j=jmax
      while(j>=jmin):
          print(A[imax][j])
          j-=1
      imax-=1

      i=imax
      while(i>=imin):
          print(A[i][jmin])
          i-=1;
      jmin+=1
print(A[imin][jmin])