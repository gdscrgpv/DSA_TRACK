#User function Template for python3
##########################################################################################################
"""
Method 1
using three pointers to keep track of o,1 and 2

"""
#######################################################################################################
class Solution:
    def sort012(self,arr,n):
        # code here
        low = 0 #KEEPIN TRACK OF 0
        mid = 0 # KEEPING TRACK OF 1
        high = len(arr)-1 # KEEPING TRACK OF 2
        while mid<=high: #IF MID > HIGH WE ARE CROOSING THE BOUNDARY
            if arr[mid]==2: # MID =2 , CORRECT PLACE IS HIGH AND UPDATE HIGH
                arr[mid],arr[high]=arr[high],arr[mid]
                high -=1
                #print("high:",arr)
            elif arr[mid]==0: # IF MID =0 , CORRECT PLACE IS LOW AND UPDATE LOW
                arr[mid],arr[low]=arr[low],arr[mid]
                low+=1
                mid+=1
            else:# AT IS CORRECCT POSITION 
                mid+=1
                #print("low",arr)
# complexity O(N)              

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends