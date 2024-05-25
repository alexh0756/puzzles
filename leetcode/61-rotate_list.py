class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return f"Node(val: {self.val}, next: {self.next})"

def build_list(head):
    if not head:
        return None
    return ListNode(head[0], build_list(head[1:]))


def rotateRight(head, k):

    refs = []
    node = head
    while node:
        refs.append(node)
        node = node.next

    length = len(refs)
    refs[length-1].next = refs[0]
    refs[(length - k) % length]
    refs[(length - k - 1) % length].next = None

    head = refs[(length - k) % length]

    return head

head = [1,2,3,4,5]
head = build_list(head)
head = rotateRight(head, k = 2)
print(head)
