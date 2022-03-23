"""
An array contains both positive and negative numbers in random order. Rearrange the array elements so that all negative numbers appear before all positive numbers.

Examples : 

Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
Output: -12 -13 -5 -7 -3 -6 11 6 5

Note: Order of elements is not important here.
"""
#########################################################################
# Approach 1: three pointer method 
# initialize low and high with zero and n-1
# if element is less than zero its position is low and vice versa 
##########################################################################


"""class Solution:
    def NegativePositive(self,arr,n):
        low = 0
        mid =0
        high= n-1
        while mid <= high:
            if arr[mid]<0:
                arr[mid],arr[low]=arr[low],arr[mid]
                low+=1
                mid+=1
            elif arr[mid]>0:
                arr[mid],arr[high]=arr[high],arr[mid]
                high-=1
                
            else:
                mid+=1
"""


############################################################################
# Approach 2: Using quick partition using 0 as piviot
############################################################################

class Solution:
    def NegativePositive(self,arr,n):
        pIndex = 0
        for i in range(0,n):
            if arr[i]<0:
                arr[pIndex],arr[i]=arr[i],arr[pIndex]
                pIndex+=1
                
            

#DriverCode
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.NegativePositive(arr,n)
        for i in arr:
            print(i, end=' ')
        print()
    