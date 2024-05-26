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

def inorder_traversal(root):
    
    if root == None:
        return [None]

    lst = []
    lst.extend(inorder_traversal(root.left))
    lst.append(root.val)
    lst.extend(inorder_traversal(root.right))

    return lst

def preorder_traversal(root):

    if root == None:
        return [None]

    lst = [root.val]
    lst.extend(preorder_traversal(root.left))
    lst.extend(preorder_traversal(root.right))

    return lst


def postorder_traversal(root):

    if root == None:
        return [None]

    lst = []
    lst.extend(postorder_traversal(root.left))
    lst.extend(postorder_traversal(root.right))
    lst.append(root.val)

    return lst

root = [3, 9, 20, 4, None, 15, 7, 1, 11, None, None, 6, 2, 8, None]
root = build_tree(root, 0)
inorder = inorder_traversal(root)
print(inorder)
preorder = preorder_traversal(root)
print(preorder)
postorder = postorder_traversal(root)
print(postorder)

root = [1, 2, 3, 4, 5, None,6]
root = build_tree(root, 0)
inorder = inorder_traversal(root)
print(inorder)
preorder = preorder_traversal(root)
print(preorder)
postorder = postorder_traversal(root)
print(postorder)