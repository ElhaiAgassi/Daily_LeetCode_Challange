
# Runtime: 70 ms, faster than 87.27% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 13.9 MB, less than 43.15% of Python3 online submissions for Add Two Numbers.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __repr__(self) -> str:
        mylinkedlist = self
        mylist = []
        while mylinkedlist is not None:
            mylist.append(mylinkedlist.val)
            mylinkedlist = mylinkedlist.next
        return ','.join(str(x) for x in mylist)

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    reminder = 0
    l3 = temp = ListNode()
    while l1 is not None or l2 is not None:
        if l1:
            reminder += l1.val
            l1 = l1.next
        if l2:
            reminder += l2.val
            l2 = l2.next
        reminder, sum, = divmod(reminder, 10)
        temp.next = ListNode(sum, None)
        temp = temp.next
    return l3.next


ls3 = ListNode(3, None)
ls2 = ListNode(2, ls3)
ls1 = ListNode(1, ls2)

lis3 = ListNode(3, None)
lis2 = ListNode(2, lis3)
lis1 = ListNode(1, lis2)

print(addTwoNumbers(ls1, lis1))
