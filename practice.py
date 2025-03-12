class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prv=None

class ddl:
    def __init__(self):
        self.head=None
        self.c=None
    def insert_at_begin(self,data):
        n=node(data)
        if self.head is not None:
            self.head.prv=n
            n.next=self.head
        self.head=n
        
    def insert_at_the_end(self,data):
        temp=self.head
        n=node(data)
        while temp.next is not None:
            temp=temp.next
        temp.next=n
        n.prv=temp
       
    def specfied_ps(self,ps,data):
        temp=self.head
        n=node(data)
        for i in range(1,ps-1):
            temp=temp.next
        n.prv=temp
        n.next=temp.next
        temp.next.prv=n
        temp.next=n
                 
    def travarsal(self):
        temp=self.head
        print("none")
        while temp is not None:
            print(temp.data,end="  <==>  ")   
            temp=temp.next
        print("none")
    def deleting_at_start(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        self.head.prv=None
       
    def deleting_at_end(self):
        temp=self.head.next
        bef=self.head
        while temp.next is not None:
            temp=temp.next
            bef=bef.next
        bef.next=None
        temp.prv=None
        
    def deleting_at_the_spf(self,ps):
        temp=self.head.next
        bef=self.head
        for i in range(1,ps-1):
            temp=temp.next
            bef=bef.next
        bef.next=temp.next
        temp.next.prv=bef.next
        temp.prv=None
        temp.next=None
       


f=ddl()
print("chose 1 for display ")
print("2 to insert at begin ")
print("3 to insert at the end ")
print("4 to insert at specified ps")
print("5 to delete value at start")
print("6 to delete at end ")
print("7 to delete at specified ")
print("8 to count node ")
print("enter the choice")
while True:
    ch=int(input("value : > "))
    if ch==1:
        f.travarsal()
    elif ch==2:
        a=int(input("enter the element at start"))
        f.insert_at_begin(a)
    elif ch==3:
        a=int(input("enter the elements at end :"))
        f.insert_at_the_end(a)
    elif ch==4:
        a=int(input("enter the elements at specifed : "))
        b=int(input("enter the postion : "))
        f.specfied_ps(b,a)
    elif ch==5:
        print("the element is deleted at start")
        f.deleting_at_start()
    elif ch==6:
        print("the element is deleting at the end")
        f.deleting_at_end()
    elif ch==7:
        a=int(input("enter the ps ypu want to delete"))
        f.deleting_at_the_spf(a)
    elif ch==8:
        print("the elements count is ",f.c)
    elif ch==0:
        print("quit")
        break

print("hellow")
