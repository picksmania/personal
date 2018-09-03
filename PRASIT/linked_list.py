class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data
        return self.data

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    def hasNext(self):
        return self.next != None



class singleLinkList(object):

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def insertAtBeginning(self, data):
        newNode = Node()
        newNode.setData(data)

        if self.listLength() == 0:
            self.head = newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode

    def insertAtEnd(self, data):
        newNode = Node()
        newNode.setData(data)

        current = self.head

        while current.getNext() != None:
            current = current.getNext()

        current.setNext(newNode)


    def listLength(self):
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.getNext()
        print "LINKED LIST Length is:",count
        return count

    def print_llist(self):
        current = self.head

        print("List Start.")
        while current != None:
            print(current.getData())
            current = current.getNext()
            # print current
        print("List End.")

    def search(self,item):
        i=1
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
                print "FOUND"
            else:
                print "PASS NUMBER %s"%i
                i+=1
                current = current.getNext()

        if found == False:
            print "NOT FOUND"

        return found


    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if found==False:
            print "You'r ITEM is not present in the LINKED LIST, SO cant DELETE"
        else:

            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())

    def remove_duplicate(self):
        current = self.head
        unique = []
        while current!= None:
            if current.getData()not in unique:
                unique.append(current.getData())
                print "Entering ",current.getData()
                current = current.getNext()
            else:
                print "%s is DUPLICATE VALUE, hence discarding...."%current.getData()
                current = current.getNext()

        print "UNIQUE LIST:::",unique

    def orderd_list(self,item):
        current = self.head
        previous = None
        stop = False

        while current!= None and not stop:
            if current.getData()> item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        newNode = Node()
        newNode.setData(item)
        if previous == None:
            newNode.setNext(self.head)
            self.head = newNode
        else:
            newNode.setNext(current)
            previous.setNext(newNode)

    # print middle of LINKED LIST
    def mid_of_linked_list(self):
        current = self.head
        second_current = self.head
        stop=False
        while current !=None and not stop:
            current = current.getNext()
            current= current.getNext()
            second_current = second_current.getNext()

            if current.getNext()==None:
                stop= True
        if stop==True:
            print "Mid of the LINK LIST is",second_current.getData()
            return second_current.getData()
            # Delete middle of linked list

    def delete_mid_of_link_list(self):
        mid_of_link_list = self.mid_of_linked_list()
        self.remove(mid_of_link_list)


    #Delete N nodes after M nodes of a linked list
    def delete_N_node_after_M_Node(self,M,N):
        curr = self.head

        # The main loop that traverses through the
        # whole list
        while(curr):
            # Skip M nodes
            for count in range(1, M):
                if curr is None:
                    return
                curr = curr.getNext()

            if curr is None :
                return

            # Start from next node and delete N nodes
            t = curr.getNext()
            for count in range(1, N+1):
                if t is None:
                    break
                t = t.getNext()

            # Link the previous list with reamining nodes
            curr.setNext(t)
            # Set Current pointer for next iteration
            curr = t



    def reverse_linkedList(self):
        curr = self.head
        prev = None
        nex = curr.getNext()
        print nex
        #looping
        while curr:
            #reversing the link
            curr.setNext(prev)

            #moving to next node
            prev = curr
            curr = nex
            if nex:
                nex = nex.getNext()

       #initializing head
        self.head = prev

    def sum_of_values_linked_list(self):
        sum_val = 0
        curr = self.head
        while curr is not None:
            data = curr.getData()
            print data
            curr = curr.getNext()
            sum_val+=data
        print sum_val


    # Delete last item from linked list
    def delete_last_item(self):
        curr = self.head
        prev = None
        while curr.getNext() != None:
            prev = curr
            curr = curr.getNext()

        prev.setNext(curr.getNext())


    # check a Linked list is PALINDROM or not

    def palindrom_check(self):
        curr = self.head
        temp =[]
        while curr != None:
            temp.append(curr.getData())
            curr = curr.getNext()

        print temp
        new_string = ''.join(temp)
        print new_string
        if new_string[::]==new_string[::-1]:
            print "LINKEDLIST is palindrom.."
        else:
            print "LINKED LIST is not Palindrom"

if __name__ == '__main__':
    # ll = singleLinkList()
    l2 = singleLinkList()
    l3 = singleLinkList()
    # #print ll.isEmpty()
    # ll.insertAtBeginning(55)
    # #print ll.isEmpty()
    # ll.insertAtEnd(56)
    # ll.insertAtBeginning(90)
    # ll.print_llist()
    # #print(ll.listLength())
    # #ll.search(56)
    # ll.remove(70)
    # ll.print_llist()
    # print "******************* LIST2 *********************"
    # l2.print_llist()
    # l2.insertAtBeginning(70)
    # l2.insertAtBeginning(80)
    # l2.insertAtEnd(100)
    # l2.insertAtEnd(90)
    # l2.insertAtEnd(50)
    # l2.insertAtBeginning(20)
    # l2.insertAtEnd(20)
    # l2.insertAtEnd(100)
    # l2.print_llist()
    # #l2.remove_duplicate()
    # print "REMOVE"
    # l2.remove(90)
    # l2.print_llist()


    print "****************** LIST3 ************************"
   #l3.print_llist()
    #l3.listLength()
    # l3.orderd_list(10)
    # l3.orderd_list(20)
    # l3.orderd_list(40)
    # #l3.print_llist()
    # l3.orderd_list(30)
    # l3.orderd_list(5)
    # l3.orderd_list(22)
    # l3.orderd_list(35)
    # l3.orderd_list(65)
    # l3.orderd_list(55)
    l3.insertAtBeginning('A')
    l3.insertAtEnd('B')
    l3.insertAtEnd('B')
    l3.insertAtEnd('A')
    l3.print_llist()
    print "*********************************************"
    #l3.mid_of_linked_list()
    #l3.delete_mid_of_link_list()
    #l3.print_llist()
    # l3.reverse_linkedList()
    #l3.delete_N_node_after_M_Node(1,1)
    #l3.delete_last_item()
    #l3.print_llist()
    l3.palindrom_check()
    #l3.sum_of_values_linked_list()
    # print "**************************************************"
    # l3.print_llist()
