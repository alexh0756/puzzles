class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"Node(vel: {self.val}, next: {self.next})"


def build_list(head):
    if not head:
        return None
    return ListNode(val=head[0], next=build_list(head[1:]))

def removeNthFromEnd(head, n):

    refs = []
    node = head
    while node != None:
        refs.append(node)
        node = node.next
    
    remove_node = len(refs)-n
    if remove_node + 1 < len(refs):
        next_node = refs[remove_node+1]
    else:
        next_node = None
    if remove_node-1 >= 0:

        refs[remove_node-1].next = next_node
    else:
        head = next_node

    return head

head = build_list(head = [1, 2])
print(removeNthFromEnd(head=head, n=2))

head = build_list(head = [1,2,3,4,5])
print(removeNthFromEnd(head=head, n=1))

head = build_list(head = [1, 2])
print(removeNthFromEnd(head=head, n=1))

head = build_list(head = [1])
print(removeNthFromEnd(head=head, n=1))

