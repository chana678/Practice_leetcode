"""
Problem:
Linked List Cycle II

Pattern:
Two Pointer (Fast and Slow)

Difficulty:
Medium

--------------------------------------------------

My First Thought:
After understanding the Floyds Algorithm, we can use two pointer Fast and Slow where slow takes
one step and Fast takes two step, and because there relative speed is 2-1 = 1, if a cycle exists
then the distance between the two pointer will be 0, hence they meet. If no cycle exists we will
return None, otherwise we will reset one pointer to the start and increment both pointer one step
at a time, and we will return the node where the slow and fast pointer meet(starting node of the 
cycle) 
let x  = distance from head to the start of the cycle
y = distance from start of the cycle to the meeting point of the cycle
L = total lenght of the cycle
Then L-y is the distance from meeting point to the start of the cycle.
Now slow = x + y, then fast = 2(x + y)
Also from  geometry fast = x + y + kL, wher k is some complete loops fast went through before
meeting slow.
Now equating the two equations of fast and rearranging the variables we get
x = (k - 1)L + L-y 
So this equation tells us that distance from the head of the linked list to the start of the cycle
is equal to some k complete loops around the cycle and the remaining distance from the meeting
point to the start of the cycle. 
so if we reset the fast pointer back to the start and keep slow in the meeting point and
increment both of them by one then by the time fast reach the start of cycle, the slow would have 
covered the remaing L-y distance


--------------------------------------------------

Observation:
The observation is same as my first though, we will return the cycle start node if cycle
exists otherwise None

--------------------------------------------------

Data Structure Chosen:
Custome Implementation of Linked List using class, as no predefined data structure for Linked List,
there is deque which under the hood is a doubly linked list implementation in python, but I think 
custom implementaion of Linked List will give us more grip in understanding the workings of a
linked list.

Reason:
Custome implementaion of linked list give more control over the program.

--------------------------------------------------

Time Complexity:
O(n) for traversing the entire linkedd list and if a cycle exist, then few more k nodes inside 
the cycle before two pointers meet. So time time complexity comes out to be O(n)

Space Complexity:
O(1) for variable declaration

--------------------------------------------------

Learnings:
Learned how to implement custome linked list using Node Class . Also we are putting condition
fast and fast.next in the whileloop because if a cycle doesn't exists fast will eventually become
none, we are checking fast.next because if we are at the last node and inside the while loop
we are doing fast = fast.next.next, not this will become fast.None.next, this will give us 
Attribute Error - None type object has not attribute next, hence in the while loop we are 
checking fast.next
Then for returning the index we will check where slow and fast meet and return the index

Mistakes:
None, Floyds Algorithm helped a lot
"""

# Custom Implementaion of Linked List

# Node Class for Singly Linked List
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def createCycle(self,index):
        current = self.head
        target_cycle_node = None
        count = 0

        while current.next:
            if count == index:
                target_cycle_node = current
            current = current.next
            count += 1

        # Checking if the tail node is the target node to create the cycle
        if count == index:
            target_cycle_node = current

        # Creating a cycle
        if target_cycle_node:
            current.next = target_cycle_node

    def detectCycle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        if fast is None or fast.next is None:
            return None

        fast = self.head
        while fast != slow:
            fast = fast.next
            slow = slow.next

        return slow



my_lst = LinkedList()

my_lst.append(10)
my_lst.append(20)
my_lst.append(30)
my_lst.insertAtBeginning(5)

my_lst.createCycle(2)

print(f"Node Index of Cycle Entry Point : {my_lst.detectCycle()}")