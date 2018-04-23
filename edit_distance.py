def edit_distance(str1,str2):
    m = len(str1)
    n = len(str2)

    L = [[0]*(n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if str1[i-1] == str2[j-1]:
                L[i][j] = L[i-1][j-1]
            elif j ==0:
                L[i][j] = i
            elif i==0:
                L[i][j] = j
            else:
                L[i][j] = 1+min(L[i][j-1],L[i-1][j],L[i-1][j-1])

    print (L[m][n])

str1 = 'Monday'
str2 = 'saturday'
edit_distance(str1,str2)