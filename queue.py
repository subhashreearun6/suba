class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
    def enque(self,value):
        if(self.head==None):
            self.head=self.tail=Node(value)
        else:
            newnode=Node(value)
            newnode.next=self.head
            self.head=newnode

    def deque(self):
        if(self.head==None):
            print("List is empty")
        else:
            temp=self.head
            while(temp.next is not None):
                prev = temp
                temp = prev.next
            self.tail=prev
            self.tail.next=None

    def searching(self,key):
        if(self.head==None):
            print("List is empty")
        else:
            temp=self.head
            while(temp.data is not key):
                if(temp.next is not None):
                    temp=temp.next
                else:
                    print("Value is not found in the list")
                    break
            else:
                print("Value is found")
            temp=None

    def updating(self,newv):
        if(self.head==None):
            print("List is empty")
        else:
            temp=self.head
            while(temp.next is not None):
                temp=temp.next
            temp.data=new

    def display(self):
        temp=self.head
        while(temp is not None):
            print(temp.data,end=" ")
            temp=temp.next

s=Queue()
print("Welcome to Queue")
while(True):
    print("Menu")
    print("Which below operations need to be performed?")
    print("1. Enque")
    print("2. Deque")
    print("3. Searching")
    print("4. Updation")
    print("5. Display")
    print("6. Exit")
    n=int(input())
    if(n is 1):
        print("Enter value to be enqued")
        val=int(input())
        s.enque(val)
    elif(n is 2):
        s.deque()
    elif(n is 3):
        print("Enter value to be searched")
        val=int(input())
        s.searching(val)
    elif(n is 4):
        print("Enter the new value")
        val1=int(input())
        s.updating(val1)
    elif(n is 5):
        s.display()
    elif(n is 6):
        exit()
    else:
        print("Invalid input")
