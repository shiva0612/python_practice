A = [4,-2,6,-10,8,1]
cur = 0
prev = 0
end=0
front=0
for i in range(0,len(A)):
    sum = cur+A[i]
    if sum<0:
        if A[i]<0:
            cur=sum;
            fron=i+1;
            print("cur = ", cur)
            print("prev = ", prev, front, end)
            continue
        else:
            cur=A[i];
            prev=cur
            front=i
            end=i
            print("cur = ", cur)
            print("prev = ", prev, front, end)
            continue

    else:
        if cur<0:
            cur=A[i];
            prev=cur;
            front=i
            end=i
        else:
            cur+=A[i]
            if cur>prev:
                prev=cur;
                end=i
    print("cur = ",cur)
    print("prev = ",prev,front,end)


