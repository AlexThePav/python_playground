from typing import Optional

# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]



# Definition for singly-linked list.
class ListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
    def __add__(self, other) -> int:
        if isinstance(other, int):
            return ListNode(self.data + other)
        return ListNode(self.data + other.data)
    
    def __repr__(self):
        return f"{self.data}"


class LinkedList:
    def __init__(self, nodes: list=None):
        self.head = None
        if nodes is not None:
            node = ListNode(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = ListNode(data=elem)
                node = node.next
    
    def __iter__(self) -> None:
        node: ListNode = self.head
        while node is not None:
            yield node
            node = node.next
    
    def __repr__(self) -> str:
        node: ListNode = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ...


if __name__ == "__main__":
    l1 = LinkedList([2,4,3])
    l2 = LinkedList([5,6,4])
    
    l1_list = [item for item in l1]
    l2_list = [item for item in l2]

    grand_total = ""
    carryover = 0
    for item1, item2 in zip(l1_list, l2_list):
        item_total = item1 + item2 + carryover
        print(f"item1: {type(item1)}")
        if len(str(item_total)) > 1:
            carryover = int(str(item_total)[:-1])
            print(f"carryover: {carryover}")
        print(f"item_total: {item_total}")
        grand_total += str(item_total)[-1:]

    print(grand_total)
    