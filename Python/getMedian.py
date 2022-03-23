def getMedian(a,b):
    c=merge(a,b)
    print(c
    )
    if len(c)%2 == 0:
        return c[(len(c)-1)//2] + c[((len(c)-1)//2) +1] // 2
    else :
        return c[(len(c)-1)//2]

def merge(l1,l2):
    c =[]
    i,j=0,0
    while i > len(l1) and j > len(l2):
        if l1[i] > l2[j]:
            c.append(l2[j])
            j+=1
        elif l1[i]< l2[j]:
            c.append(l1[i])
            i+=1
        else:
            c.append(l1[i])
            c.append(l1[j])
            i+=1
            j+=1
    while i<len(l1):
        c.append(l1[i])
        i+=1
    while(j<len(l2)):
        c.append(l2[j])
        j+=1
    return c

#Driver code
a = [900]
b = [5, 8, 10, 20]
 
#n1 = len(ar1)
#n2 = len(ar2)
print(getMedian(a,b))