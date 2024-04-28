# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next

# Function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Function to print a linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Getting input from the user
input1 = list(map(int, input("Enter values for the first linked list separated by space: ").split()))
input2 = list(map(int, input("Enter values for the second linked list separated by space: ").split()))

# Creating linked lists
l1 = create_linked_list(input1)
l2 = create_linked_list(input2)

# Creating solution object
sol = Solution()

# Adding two numbers
result = sol.addTwoNumbers(l1, l2)

# Printing the result
print("Result:")
print_linked_list(result)
