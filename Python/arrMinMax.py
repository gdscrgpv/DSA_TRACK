"""
METHOD 1 (Simple Linear Search) 
Initialize values of min and max as minimum and maximum of the first two elements respectively. Starting from 3rd, compare each element with max and min, and change max and min accordingly (i.e., if the element is smaller than min then change min, else if the element is greater than max then change max, else ignore the element).
"""
def arrMinMax(arr):
    if arr[0] > arr[1]:#comparing the first two elements
        max = arr[0]
        min = arr[1]
    else:
        max = arr[1]
        min = arr[0]

    for i in range (2,len(arr)):#Lenear search for min and max 
        if (arr[i]<min):
            min =arr[i]
        elif (arr[i]>max):
            max = arr[i]
    
    return max, min
arr = [1000, 11, 445, 1, 330, 3000]
print (arrMinMax(arr))

""" 
-----------------------------------------------------------------------------


METHOD 2 (Tournament Method) 
Divide the array into two parts and compare the maximums and minimums of the two parts to get the maximum and the minimum of the whole array.

Pair MaxMin(array, array_size)
   if array_size = 1
      return element as both max and min
   else if arry_size = 2
      one comparison to determine max and min
      return that pair
   else    /* array_size  > 2 */
      recur for max and min of left half
      recur for max and min of right half
      one comparison determines true max of the two candidates
      one comparison determines true min of the two candidates
      return the pair of max and min
"""
#Program of above implementation
def getMinMax (low,high,arr):
    arr_max = arr[low]
    arr_min = arr[low]

    #if there is only one element 
    if low == high:
        arr_max = arr[low]
        arr_min = arr[low]
        return (arr_max,arr_min)
    
    #if there are only two elements
    elif high == (low + 1) :
        if arr[low] > arr[high]:
            arr_max = arr[low]
            arr_min = arr[high]
        else :
            arr_max = arr[high]
            arr_min = arr[low]
        return (arr_max,arr_min)
    
    #if there are more then two elements
    else:
        mid = int((low + high)/2)
        arr_max1, arr_min1 = getMinMax(low, mid, arr)
        arr_max2, arr_min2 = getMinMax(mid+1, high, arr)
    return (max(arr_max1, arr_max2),min(arr_min1,arr_min2))

#Driver Code

arr = [1000, 11, 445, 1, 330, 3000]
high = len(arr) - 1
low = 0
arr_max, arr_min = getMinMax(low, high, arr)
print('Minimum element is ', arr_min)
print('nMaximum element is ', arr_max)

"""
Time Complexity: O(n) 

Total number of comparisons: let the number of comparisons be T(n). T(n) can be written as follows: 
Algorithmic Paradigm: Divide and Conquer 

             
  T(n) = T(floor(n/2)) + T(ceil(n/2)) + 2  
  T(2) = 1
  T(1) = 0

If n is a power of 2, then we can write T(n) as: 


   T(n) = 2T(n/2) + 2

After solving the above recursion, we get 

  T(n)  = 3n/2 -2

Thus, the approach does 3n/2 -2 comparisons if n is a power of 2. And it does more than 3n/2 -2 comparisons if n is not a power of 2.
-----------------------------------------------------------------------------
"""

"""
METHOD 3 (Compare in Pairs) 
If n is odd then initialize min and max as first element. 
If n is even then initialize min and max as minimum and maximum of the first two elements respectively. 
For rest of the elements, pick them in pairs and compare their 
maximum and minimum with max and min respectively. 
"""
# program of above implementation
def getMaxMin(arr):
    n = len(arr)
    #if array has even number of elements then 
    #initialize the first teo elements as minimum and maximum
    if (n%2==0):
        _max = max(arr[0],arr[1])
        _min = min(arr[0],arr[1])
        i=2             # setting staring point for loop
    
    
    # if array has odd number of elements then 
    #initialize the first elements as minimum and maximum
    else :
        _max = _min = arr[0]
        i=1             # setting staring point for loop
    

    #in the while loop, pick elements in pair and caompare the pair with 
    # min and max so far
    while (i < n-1):
        if arr[i] < arr[i+1]:
            _max= max(_max, arr[i+1])
            _min = min (_min , arr[i])
        else:
            _max = max(_max, arr[i])
            _min = min (_min , arr[i+1])
            #increment the index by 2 
            i += 2
    return (_min, _max)


# Driver Code
if __name__ =='__main__':
     
    arr = [1000, 11, 445, 1, 330, 3000]
    mx, mn = getMaxMin(arr)
    print("Minimum element is", mn)
    print("Maximum element is", mx)

    """
    Time Complexity: O(n)

Total number of comparisons: Different for even and odd n, see below: 

       If n is odd:    3*(n-1)/2  
       If n is even:   1 Initial comparison for initializing min and max, and 3(n-2)/2 comparisons for rest of the elements  
        =  1 + 3*(n-2)/2 = 3n/2 -2

Second and third approaches make the equal number of comparisons when n is a power of 2. 
In general, method 3 seems to be the best.
"""