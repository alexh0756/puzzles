class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self) -> str:
        return f"node(val: {self.val}, next: {self.next})"


def build_list(nums):
    if not nums:
        return 
    return ListNode(nums[0], build_list(nums[1:]))


def sortList(head):

    start = head
    while start.next:

        node = start
        while node.next and node.val > node.next.val:
            node.val, node.next.val = node.next.val, node.val
            node = node.next

        while start.next and start.val < start.next.val:
            start = start.next
    
    return head



head = [4,2,1,3]
head = build_list(head)
print(sortList(head))