class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next


class LinkedList:
    def __init__(self):
        self.head=None
    
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        lstr = ''
        while itr :
            lstr += str(itr.data) + ' --> ' 
            itr = itr.next
        print(lstr)
    
    def getLength(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr=itr.next
        return count
    
    def insertAtBegining(self,data):
        node = Node(data,self.head)
        self.head = node

    def insertAtEnd(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        
        while itr.next:
            itr=itr.next
        itr.next = Node(data,None)

    def insertAt(self, index, data):
        if index<0 or index > self.getLength():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insertAtBegining(data)
            return
        count=0
        itr =self.head
        while itr :
            if count ==index -1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def removeAt(self, index):
        if index <0 or index > self.getLength():
            raise Exception ('Invalid Index')
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr :
            if count == index -1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1
    def insertValues(self, data_list):
        self.head = None
        for data in data_list:
            self.insertAtEnd(data)

if __name__ == '__main__':
    ll = LinkedList()
    ll.insertValues(["banana","mango","grapes","orange"])
    ll.insertAt(1,"blueberry")
    ll.removeAt(2)
    ll.print()

    ll.insertValues([45,7,12,567,99])
    ll.insertAtEnd(67)
    ll.print()
