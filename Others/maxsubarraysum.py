def solution(A):
    max_slice_ending_here = A[0]
    max_slice = A[0]

    for element in A[1:]:
        max_slice_ending_here = max(element, max_slice_ending_here + element)
        max_slice = max(max_slice, max_slice_ending_here)

    return max_slice
import numpy as np

def divide_and_conquer(A):
   # Array of cumulative sums allows for the computation of overlapping solution in constant time.
     sums = np.insert(np.cumsum(A), 0, 0)
     def loop(l,r):
         if l == r: return (A[l], sums[l], sums[l+1])
         else:
             # If I have more than one element, split the array and loop over left and right part.
             c = (l + r - 1) // 2
             resLeft, minPrefixLeft, maxPrefixLeft = loop(l, c)
             resRight, minPrefixRight, maxPrefixRight = loop(c + 1, r)
             minPrefix = min(minPrefixLeft, minPrefixRight)
             maxPrefix = max(maxPrefixLeft, maxPrefixRight)
             # Solution overlapping both the left and the right part can be computed as follows.
             resCenter = maxPrefixRight - minPrefixLeft
             # Overall solution is maximum of solutions on the left, on the right and overlapping.
             res = max(resLeft, resCenter, resRight)
             return (res, minPrefix, maxPrefix)
     res, _, _ = loop(0, len(A)-1)
     return res

print(divide_and_conquer([1,-1,-2,3,4,-6]))