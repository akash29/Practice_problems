def solution(A,B):
    count=0
    for i in range(A,B+1):
        j=1
        while j*j <= i:
            if j*j == i:
                count+=1
            j+=1

    print (count)


print (solution(-1000,1000))