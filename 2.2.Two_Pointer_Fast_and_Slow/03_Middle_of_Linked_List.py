"""
Problem:
Middle of a Linked List

Pattern:
Two Pointer (Fast and Slow)

Difficulty:
Easy

--------------------------------------------------

My First Thought:
After understanding the Floyds Algorithm, we can use two pointer Fast and Slow where slow takes
one step and Fast takes two step. By this approach by the time fast reached the end of the list,
slow will be at the middle of the list.

--------------------------------------------------

Observation:
The observation is same as my first though, we will return the middle node of the Linked List

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
O(n) for traversing the entire linkedd list .

Space Complexity:
O(1) for variable declaration

--------------------------------------------------

Learnings:
Learned how to implement custome linked list using Node Class.

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

    def middleNode(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow



my_lst = LinkedList()

my_lst.append(10)
my_lst.append(20)
my_lst.append(30)
my_lst.insertAtBeginning(5)

print(f"Middle of a Linked List : {my_lst.middleNode()}")