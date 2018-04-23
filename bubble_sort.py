

lst = [1,2,3]

def bubble_sort(lst):
    num_swaps=0
    for i in range(len(lst)):
        isSwapped = False
        for j in range(len(lst)-i-1):
            if lst[j+1]<lst[j]:
                lst[j+1],lst[j] = lst[j],lst[j+1]
                num_swaps+=1
                isSwapped = True

        if not isSwapped:
            print ("num swaps:", num_swaps)
            print("first element:", lst[0])
            print("last element:", lst[-1])
            return lst

print(bubble_sort(lst))