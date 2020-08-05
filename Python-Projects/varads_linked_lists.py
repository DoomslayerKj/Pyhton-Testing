
#Developed By Varad Kj on 05/08/2020    ........ Social - Instagram(@mr.y2kj)
#All functions working properly
# Reverse function needs to be Debugged , does not work when imported
#Initalize a new list by-
#              list_Example = LinkedList()
#              New_Node = Node(data,next_pointer )
#

class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        node=Node(data,self.head)
        self.head=node
    def print(self):
        if self.head == None:
            print("Empty List")
            return

        itr=self.head
        llstr = ''
        while itr:
            llstr  += str(itr.data) + '-->'
            itr=itr.next

        print(llstr)

    def insert_at_end(self,data):
        if self.head is None:
            new_node=Node(data,None)
            self.head=new_node
            return

        itr=self.head
        while itr.next:
            itr=itr.next

        itr.next=Node(data,None)

    def insert_values(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return  count


    def remove_at_index(self,index):
        pntr=self.head
        if self.head is None:
            return None
        count=0
        if index in range(self.get_length()):
            while pntr:
                count+=1
                if count == (index):
                    pntr.next=pntr.next.next
                    break
                pntr=pntr.next
        else:
            raise  Exception("Index Out Of Bounds!")


    def insert_at_index(self,data,index):
        if index > self.get_length() or index < 0:
            raise Exception("Invalid Index/Index out of bounds, Please try again!")
            return
        if index ==0 :
            self.insert_at_beginning(data)
            return

        itr=self.head
        count =0
        while itr:
            if(count == (index -1)):
               new_node=Node(data,itr.next)
               itr.next=new_node
               break
            itr=itr.next
            count+=1

    def find(self,element):
        if self.head is None:
            print("Empty List!")
            return


        itr=self.head
        count=-1
        pos=0
        while itr:
            count+=1
            if element == itr.data:
                print("Element Found at Location : ", count)
                pos=1
                break

            else:
                pos=-1
            itr=itr.next

        if pos < 0:
            print("Element Not Found!!")


    def insert_after_value(self,data,new_value):
        if self.head is None:
            raise Exception("Empty List!")

        itr=self.head
        count = 0

        found = False
        while itr:
            if itr.data == data:
                new_node=Node(new_value,itr.next)
                itr.next=new_node
                found =True
                break
            itr=itr.next

        if found==False:
            raise Exception("Element Not Found")

    def remove_by_value(self,value):
        if self.head is None:
            raise Exception("Empty List!")

        itr=self.head
        count=0
        found =False
        while(itr):
             if itr.data == value:
                 self.remove_at_index(count)
                 found=True
                 break
             count+=1
             itr=itr.next

        if found== False:
            raise Exception("Element not Found!")

    def delete_whole_list(self):
        self.head=None








if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values([11,22,33,44,55,66])

    ll.remove_by_value(66)
    ll.delete_whole_list()

    ll.print()
    print("Length : ",ll.get_length())
