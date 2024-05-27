class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self) -> str:
        return f"tree(val: {self.val}, left: {self.left}, right: {self.right})"


def build_tree(root, index):
    if root[index] == None:
        return None

    tree = TreeNode(root[index])
    if 2*index+1 < len(root):
        tree.left = build_tree(root, 2*index+1)
    if 2*index+2 < len(root):
        tree.right = build_tree(root, 2*index+2)

    return tree

def preorder_traversal(root):
    lst = [root]
    i = 0
    while i < len(lst):
        loc = i + 1
        node = lst[i]
        if node.left:
            lst.insert(loc, node.left)
            loc += 1
        if node.right:
            lst.insert(loc, node.right)
        i += 1

    return lst


def iterativePreorder(root):
    
    # Base CAse 
    if root is None:
        return 

    # create an empty stack and push root to it
    nodeStack = []
    nodeStack.append(root)

    # Pop all items one by one. Do following for every popped item
    # a) print it
    # b) push its right child
    # c) push its left child
    # Note that right child is pushed first so that left
    # is processed first */
    while(len(nodeStack) > 0):
        
        # Pop the top item from stack and print it
        node = nodeStack.pop()
        print (node.val, end=" ")
        
        # Push right and left children of the popped node
        # to stack
        if node.right is not None:
            nodeStack.append(node.right)
        if node.left is not None:
            nodeStack.append(node.left)
        

def flatten(root):

    def preorder_traversal(root):

        if root == None:
            return [None]

        lst = [root]
        if root.left:
            lst.extend(preorder_traversal(root.left))
        if root.right:
            lst.extend(preorder_traversal(root.right))

        return lst
    
    lst = preorder_traversal(root)

    for i in range(len(lst)-1):
        lst[i].left = None
        lst[i].right = lst[i+1]

    return root


root = [3,1,4,None,2,None,None]
root = build_tree(root, 0)
preorder = preorder_traversal(root)



root = [1,2,5,3,4,None,6]
root = build_tree(root, 0)
preorder = preorder_traversal(root)
preorder = iterativePreorder(root)
inorder = flatten(root)