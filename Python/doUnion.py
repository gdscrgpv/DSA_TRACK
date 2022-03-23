"""
Input:
5 3
1 2 3 4 5
1 2 3
Output: 
5
Explanation: 
1, 2, 3, 4 and 5 are the
elements which comes in the union set
of both arrays. So count is 5.

##############################################################################################
Solution:

    Insert all elements of the first array in a Set or HashSet.
    Insert all elements of the second array in the Set or HashSet.
    Remember Set or HashSet does not contain duplicate elements.
    Return the size of Set or HashSet which is total number of elements in them.


"""




class Solution:
    def doUnion(self,a,n,b,m):
        s=set()
        for i in a:
            s.add(i)
        for i in b:
            s.add(i)
        return len(s)




#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n,m=[int(x) for x in input().strip().split()]
        
        a=[int(x) for x in input().strip().split()]
        b=[int(x) for x in input().strip().split()]
        ob=Solution()
        
        print(ob.doUnion(a,n,b,m))
# } Driver Code Ends

