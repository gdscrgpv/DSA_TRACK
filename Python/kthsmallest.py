import random
"""
Given an array arr[] and a number K where K is smaller than size of array, the task is to find the Kth smallest element in the given array. It is given that all array elements are distinct.

Example 1:

Input:
N = 6
arr[] = 7 10 4 3 20 15
K = 3
Output : 7
Explanation :
3rd smallest element in the given 
array is 7.

Example 2:

Input:
N = 5
arr[] = 7 10 4 20 15
K = 4
Output : 15
Explanation :
4th smallest element in the given 
array is 15.

Your Task:
You don't have to read input or print anything. Your task is to complete the function kthSmallest() which takes the array, it's size and an integer k as input and returns the kth smallest element.
 
 
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 <= N <= 105
1 <= arr[i] <= 105
1 <= K <= N
"""

###################################################################################################
'''
def kthsmallest(arr, l, r, k):
    
#    arr : given array;
#    l : starting index of the array i.e 0 ;
#    r : ending index of the array i.e size-1 ;
#    k : find kth smallest element and return using this function;
    
    
    for i in range(r):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i+1, r):
            if arr[min_idx] > arr[j]:
                 min_idx = j

    # Swap the found minimum element with
    # the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print("Sorted array", arr)
    return arr[k-1]
# Driver code to test above


arr= [64, 25, 12, 22, 11]
r = len(arr)
l=0
k=int(input("enter the element kth element to be found   :"))
print (kthsmallest(arr,l,r,k)) 

for i in range(len(arr)):
    print("%d" % arr[i]),
 
#    Time Complecity : O(N^2)
'''
 
 
 ###############################################
# Method 2
###############################################


'''
class Solution:
    def __init__(self):
        self.arr = None
        self.k= None

    def kthSmallest(self, arr,l, r, k):
        arr.sort()  # in acending order 
        self.arr=arr # initializing 
        self.k = k
        return self.arr[self.k-1]

 #    Time Complecity : O(NlogN)
 
'''
########################################################################

# Method 3
# random Quick sort does this in expected linear time
########################################################################



class Solution:
    
    def LomutoPartion(self,arr, l, r):
        pivot = arr[r]
        pindex = l
        for i in range(l,r):
            if arr[i]<=pivot:
                pindex+=1
                arr[pindex],arr[i] = arr[i],arr[pindex]  
        arr[pindex ],arr[r] = arr[r],arr[pindex]
        return pindex

    
    def RandomPartion(self,arr, l, r):
        n= r - l +1
        pivot = random.randint(l,r)
        arr[l+pivot], arr[r] = arr[r], arr[l+pivot]
        return self.LomutoPartion(arr,l,r)

    
    def kthSmallest(self,arr, l, r, k):
        if (k>0 and k<= r-l+1):
            pos = self.RandomPartion(arr,l,r)
            
            if (pos-l == k-1):
                return arr[pos]
            if (pos-l > k-1):
                return self.kthSmallest(arr,l,pos-1,k)
            return self.kthSmallest(arr,pos+1,r,k-pos+l-1)
        return sys.maxsize

if __name__ == '__main__': 
    import random 
    import sys
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        k=int(input())
        ob=Solution()
        print(ob.kthSmallest(arr, 0, n-1, k))
