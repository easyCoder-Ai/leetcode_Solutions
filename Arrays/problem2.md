# Add Two Numbers - LeetCode Problem

## Problem Description

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Difficulty Level**: Medium

## Explanation

In this problem, the main focus is understanding the concept of linked lists and their advantages and disadvantages. A linked list is a linear data structure where each element is a separate object, called a node. Each node contains data and a reference (or link) to the next node in the sequence.

### Advantages of Linked Lists

1. **Dynamic Size**: Unlike arrays, linked lists do not have a fixed size. They can grow and shrink in size as needed.
2. **Ease of Insertion/Deletion**: Inserting or deleting nodes in a linked list is simpler compared to arrays, especially when dealing with large amounts of data.

### Disadvantages of Linked Lists

1. **Memory Usage**: Each element in a linked list requires extra memory to store references.
2. **Access Time**: Linked lists have slower access time compared to arrays, as elements are not stored contiguously in memory.

## Solution

To solve this problem, we need to iterate through the two linked lists, adding the corresponding digits along with any carry-over from the previous iteration. The sum of these digits will form a new node in the result linked list. Below is the Python implementation of the solution:

```python
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
    
#     def __repr__(self):
#         return f"ListNode({self.val})"

# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         remind = 0
#         result = ListNode(val=0, next=None)
#         tail = result

#         while l1 is not None or l2 is not None or remind != 0:
#             # Check if the values are not equal to None
#             firstDigit = l1.val if l1 is not None else 0
#             secondDigit = l2.val if l2 is not None else 0

#             # Calculate sum of digits
#             calculatedSum = firstDigit + secondDigit + remind

#             # Implementing new node according to new sum
#             newNode = ListNode(calculatedSum % 10)  # According to sum rule

#             # Add new sum to result
#             tail.next = newNode
#             tail = tail.next
            
#             # Update carry for next iteration
#             remind = calculatedSum // 10  # According to sum rule

#             # Move to the next nodes in the lists
#             l1 = l1.next if l1 is not None else None
#             l2 = l2.next if l2 is not None else None

#         outPut = result.next
#         result.next = None

#         return outPut
