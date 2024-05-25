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

def deleteDuplicates(head):

    node = head
    node_prev = ListNode(val=None, next=head)
    while node.next != None:
        node_next = node.next

        while node.val == node_next.val:
            node = node_prev
            node_next = node_next.next
            node_prev.next = node_next
        
        node_prev = node
        node = node_next

    return head

head = [1,1,1,2,3]
head = build_list(head)
print(deleteDuplicates(head))


head = [1,2,3,3,4,4,5]
head = build_list(head)
print(deleteDuplicates(head))