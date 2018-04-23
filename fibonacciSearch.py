

def fibonacci_search():
    fibMM2 = 0
    fibMM1 = 1
    fibMM = fibMM2+fibMM1
    while fibMM < len(input_arr):
        fibMM2 = fibMM1
        fibMM1 = fibMM
        fibMM = fibMM1+fibMM2

    offset = -1

    while fibMM >1:
        index = min(offset+fibMM2,len(input_arr)-1)

        if input_arr[index] < num_find:
            fibMM = fibMM1
            fibMM1 = fibMM2
            fibMM2 = fibMM-fibMM1
            offset = index
        elif input_arr[index] > num_find:
            fibMM  = fibMM2
            fibMM1 = fibMM1 - fibMM2
            fibMM2 = fibMM - fibMM1
        else:
            return index
    if fibMM1 and input_arr[offset+1] == num_find:
        return offset+1
    else :
        return -1

    pass


if __name__=="__main__":
    input_arr = [10, 22, 35, 40, 45, 50, 80, 82,
                 85, 90, 100]
    num_find = 21
    x = fibonacci_search()
    print("index of " + str(num_find) + ":", x)
