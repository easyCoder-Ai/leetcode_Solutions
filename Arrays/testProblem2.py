import unittest
from problem2 import ListNode, Solution

class TestAddTwoNumbers(unittest.TestCase):

    def list_to_linked_list(self, values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for value in values[1:]:
            current.next = ListNode(value)
            current = current.next
        return head

    def linked_list_to_list(self, node):
        values = []
        while node:
            values.append(node.val)
            node = node.next
        return values

    def test_add_two_numbers(self):
        sol = Solution()
        
        # Test case 1: [2, 4, 3] + [5, 6, 4] = [7, 0, 8]
        l1 = self.list_to_linked_list([2, 4, 3])
        l2 = self.list_to_linked_list([5, 6, 4])
        result = sol.addTwoNumbers(l1, l2)
        self.assertEqual(self.linked_list_to_list(result), [7, 0, 8])

        # Test case 2: [0] + [0] = [0]
        l1 = self.list_to_linked_list([0])
        l2 = self.list_to_linked_list([0])
        result = sol.addTwoNumbers(l1, l2)
        self.assertEqual(self.linked_list_to_list(result), [0])

        # Test case 3: [9, 9, 9, 9, 9, 9, 9] + [9, 9, 9, 9] = [8, 9, 9, 9, 0, 0, 0, 1]
        l1 = self.list_to_linked_list([9, 9, 9, 9, 9, 9, 9])
        l2 = self.list_to_linked_list([9, 9, 9, 9])
        result = sol.addTwoNumbers(l1, l2)
        self.assertEqual(self.linked_list_to_list(result), [8, 9, 9, 9, 0, 0, 0, 1])

        # Additional test case 4: [1, 8] + [0] = [1, 8]
        l1 = self.list_to_linked_list([1, 8])
        l2 = self.list_to_linked_list([0])
        result = sol.addTwoNumbers(l1, l2)
        self.assertEqual(self.linked_list_to_list(result), [1, 8])

        # Additional test case 5: [5] + [5] = [0, 1]
        l1 = self.list_to_linked_list([5])
        l2 = self.list_to_linked_list([5])
        result = sol.addTwoNumbers(l1, l2)
        self.assertEqual(self.linked_list_to_list(result), [0, 1])

if __name__ == '__main__':
    unittest.main()
