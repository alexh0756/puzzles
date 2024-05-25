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


def partition(head, x):

    refs = []
    dummy = ListNode(next=head)
    node, node_prev = dummy, dummy
    while node:
        node = node.next
        if not node or node.val >= x:
            node_prev.next = node
            node_prev = node
        elif node.val in refs:
            refs.append(node)
        else:
            refs.append(node)
    
    head = dummy.next

    dummy = ListNode()
    node_tmp = dummy
    for node in refs:
        node_tmp.next = node
        node_tmp = node_tmp.next
    node_tmp.next = head
    return dummy.next



head = [1,4,3,2,5,2]
head = build_list(head)
head = partition(head, x=3)
print(head)


head = [1,3,-1,5,2,1]
head = build_list(head)
head = partition(head, x=3)
print(head)
