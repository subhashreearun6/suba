class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class Stack:
    def __init__(self):
        self.top=None
    def insert(self,value):
        if(self.top==None):
            self.top=self.tail=Node(value)
        else:
            newnode=Node(value)
            newnode.next=self.top
            self.top=newnode

    def rem(self):
        if(self.top==None):
            print("List is empty")
        else:
            temp=self.top
            self.top=temp.next
            temp=None

    def last(self):
        if(self.top==None):
            print("List is empty")
        else:
            temp=self.top
            print("Top pointer points to the value:")
            print(temp.data)

    def display(self):
        temp=self.top
        while(temp is not None):
            print(temp.data,end=" ")
            temp=temp.next

s=Stack()
print("Welcome to Stack")
while(True):
    print("Menu")
    print("Which below operations need to be performed?")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    n=int(input())
    if(n is 1):
        print("Enter value to be pushed")
        val=int(input())
        s.insert(val)
    elif(n is 2):
        s.rem()
    elif(n is 3):
        s.last()
    elif(n is 4):
        s.display()
    elif(n is 5):
        exit()
    else:
        print("Invalid input")
