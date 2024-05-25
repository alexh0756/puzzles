class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"tree(val: {self.val}, left: {self.left}, right: {self.right})"


def build_tree(root):

    tree = TreeNode(val=root[0])
    tree.left
    tree.right

    return tree

def build_binary_tree(values, index):
    if len(values) == 0:
        raise Exception('Node list is empty')

    if index > len(values) - 1:
        raise Exception('Index out of range')

    root = TreeNode(values[index])
    if 2*index+1 < len(values):
        root.left = build_binary_tree(values, 2*index+1)
    if 2*index+2 < len(values):
        root.right = build_binary_tree(values, 2*index+2)

    return root


def invertTree(root):

    if not root:
        return root

    root.left, root.right = invertTree(root.right), invertTree(root.left)

    return root

root = [4,2,7,1,3,6,9]
root = build_binary_tree(root, 0)
print(invertTree(root))
