"""
Kadane’s Algorithm:
Initialize:
    max_sum = INT_MIN
    curr_sum = 0

Loop for each element of the array
  (a) curr_sum = curr_sum + a[i]
  (b) if(max_sum < curr_sum)
            max_sum = curr_sum
  (c) if(curr_sum < 0)
            curr_sum = 0
return max_sum


Lets take the example:
    {-2, -3, 4, -1, -2, 1, 5, -3}

    max_sum = curr_sum = 0

    for i=0,  a[0] =  -2
    curr_sum = curr_sum + (-2)
    Set curr_sum = 0 because curr_sum < 0

    for i=1,  a[1] =  -3
    curr_sum = curr_sum + (-3)
    Set curr_sum = 0 because curr_sum < 0

    for i=2,  a[2] =  4
    curr_sum = curr_sum + (4)
    curr_sum = 4
    max_sum is updated to 4 because curr_sum greater 
    than max_sum which was 0 till now

    for i=3,  a[3] =  -1
    curr_sum = curr_sum + (-1)
    curr_sum = 3

    for i=4,  a[4] =  -2
    curr_sum = curr_sum + (-2)
    curr_sum = 1

    for i=5,  a[5] =  1
    curr_sum = curr_sum + (1)
    curr_sum = 2

    for i=6,  a[6] =  5
    curr_sum = curr_sum + (5)
    curr_sum = 7
    max_sum is updated to 7 because curr_sum is 
    greater than max_sum

    for i=7,  a[7] =  -3
    curr_sum = curr_sum + (-3)
    curr_sum = 4



    


"""





class MaxSubArrSum:
    def bruteForce(self,arr):
        # Initializing global sum
        max_sum = 0
        # just to keep track of sub arrays 
        s, a=[], []
        # initializing first loop
        for i in range(0,len(arr)):
            # this is to compare local sum and compare with max sum
            curr_sum = 0
            # For main taining sub array
            s.append(arr[i])
            print (s)

            curr_sum = curr_sum + arr[i]
            if curr_sum > max_sum:
                max_sum = curr_sum
            
            for j in range (i+1, len(arr)):
                a.append(s[:])
                s.append(arr[j])
                print (s)
                curr_sum= curr_sum + arr[j]
                if curr_sum > max_sum:
                    max_sum = curr_sum
                
            a.append(s[:])
            s= []
            
            curr_sum = 0
                        
        return max_sum
    
    def kadaneAlgo(self, arr, n):
        curr_sum ,max_sum = 0, 0
        for i in range (n):
            curr_sum += arr[i]
            if curr_sum < 0:
                curr_sum = 0
            elif curr_sum > max_sum:
                max_sum = curr_sum

        return max_sum


    """
    ###########################################################################


    --> but this will not work if alll the elements in array are negative
        Dynamic Programing comes to rescue.

    """
    def maxSubArrSum(self,arr):
        max_sum , curr_sum = 0, 0
        
        for i in arr:
            curr_sum = max(i , curr_sum + i)
            max_sum = max(curr_sum, max_sum)
        return max_sum


a = [-2, -3, 4, -1, -2, 1, 5, -3]
ob = MaxSubArrSum()
#ob.bruteForce(a)
#w = ob.kadaneAlgo(a, len(a))
b = ob.maxSubArrSum(a)
print("....",b)
