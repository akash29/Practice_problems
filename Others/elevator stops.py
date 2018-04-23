def solution (A, B, M ,X, Y):
    trip_weight = 0
    person_count = 0
    stops = []
    stop_count=0
    if len(A)==len(B):
        for i in range(len(A)):
            if B[i] <= M:
                if person_count+1 > X or trip_weight+A[i] > Y:
                    stop_count += len(set(stops))
                    stops[:] = []
                    trip_weight = 0
                    person_count = 0
                    stop_count += 1
                stops.insert(i,B[i])
                person_count += 1
                trip_weight += A[i]
            else:
                raise ValueError('pressed floor is greater than M(max available)') #should I return -1?
    else:
        raise ValueError('A and B are not of same size') # should I return -1?



    if len(stops) > 0:
        stop_count += len(set(stops))+1

    return stop_count


print(solution([40,40,100,80,20,12,18,100],[2,3,5,1,2,3,4,5],5,3,200))

