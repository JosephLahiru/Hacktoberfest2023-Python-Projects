class Node:
    def __init__(self,value):
      self.value=value
      self.next=None

class LinkedList:
    def __init__(self,value):
      newNode = Node(value)
      self.head=newNode
      self.tail=newNode
      self.length=1
      
    def printList(self):
        temp=self.head
        while temp :
          print(temp.value, end="->")
          temp=temp.next
        print(end="\n")

    def append(self,value):
        newNode=Node(value)

        if self.head is None:
          self.head=newNode
          self.tail=newNode
        else:
           self.tail.next=newNode
           self.tail=newNode
        self.length+=1

    def remove_last(self):
        if self.head is None:
          return None
        
        temp=self.head
        pre=self.head
        
        while temp.next:
           pre=temp
           temp=temp.next

        self.tail=pre
        self.tail.next=None
        self.length-=1

        return temp
    
    def prepend(self,value):
        newNode=Node(value)

        if self.head is None:
          self.head=newNode
        else:
           newNode.next=self.head
           self.head=newNode
        self.length+=1
          

    def get_length(self):
       return self.length
    




ll = LinkedList(5)
ll.append(3)
ll.append(4)

ll.printList()


ll.remove_last()

print(ll.get_length())

ll.prepend(9)

ll.printList()
print(ll.get_length())
