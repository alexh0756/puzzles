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


def reverseKGroup(head, k):

    refs = []
    i = 0
    tmp = []
    dummy = ListNode(next=head)
    node = dummy.next
    while node:
        tmp.append(node)
        node = node.next
        i += 1
        if i == k:
            a, b = 0, k - 1
            while a < b:
                tmp[b].val, tmp[a].val = tmp[a].val, tmp[b].val
                a += 1
                b -= 1
            i = 0
            tmp = []
    
    return dummy.next



# head = [1,2,3,4,5]
# head = build_list(head)
# head = reverseKGroup(head, k=2)
# print(head)


head = [1,2]
head = build_list(head)
head = reverseKGroup(head, k=2)
print(head)
