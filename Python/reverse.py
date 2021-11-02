# method 1 using iterative way does not work with immutable oblects i.e str, tupple etc.
# Time Complexity : O(n)
'''
1) Initialize start and end indexes as start = 0, end = n-1 
2) In a loop, swap arr[start] with arr[end] and change start and end as follows : 
start = start +1, end = end – 1

'''
def reverseWord(st):
    start,end=0,len(st)-1;
    while start < end :
        st[start],st[end]=st[end],st[start];
        start+=1;
        end-=1;
    return st;


b=[1,64,0.5,6541,651,65468,6465,65465]
reverseWord(b)
print("\nReversed list is")
print (b)


#Method 2: recursive way 
'''
1) Initialize start and end indexes as start = 0, end = n-1 
2) Swap arr[start] with arr[end] 
3) Recursively call reverse for rest of the array.

'''
def reverseList(A, start, end):
    if start >= end:
        return
    A[start], A[end] = A[end], A[start]
    reverseList(A, start+1, end-1)
 
# Driver function to test above function
A = [1, 2, 3, 4, 5, 6]
print("\nInitial list",A)
reverseList(A, 0, 5)
print("\nReversed list is")
print(A)