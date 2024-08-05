from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"ListNode({self.val})"

class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], \
                      l2: Optional[ListNode]) -> Optional[ListNode]:

        remind = 0
        result = ListNode(val=0, next=None)
        tail = result

        while l1 != None or l2 != None or remind != 0:
            
            ################ check if the values are not equal to None #############
            firstDigit = l1.val if l1 != None else 0
            secondDigit = l2. val if l2 != None else 0

            ################ calculate sum of digist ##############################
            calculatedSum = firstDigit + secondDigit + remind

            ################ implementing new nod according to new sum ############ 
            newNode = ListNode(calculatedSum % 10) # According to sum rule

            ################ add new sum to Result ############################
            tail.next = newNode

            tail = tail.next
            
            
            remind = calculatedSum // 10 # According to sume rule


            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        

        outPut = result.next
        result.next = None

        return(outPut)

        

        



    

# # Example usage:
# node1 = ListNode(1)
# node2 = ListNode(2)
# node3 = ListNode(3)
# node1.next = node2
# node2.next = node3



# # print(node1)  # Output: ListNode(1)
# # print(node1.next)  # Output: ListNode(2)


# Solution(l1=node1, l2=node1)



