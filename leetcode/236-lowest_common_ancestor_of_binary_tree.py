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


def lowestCommonAncestor(root, p, q):
    if not root:
        return False

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if ((left == True) + (right == True) + (root.val in (p, q))) == 2:
        return root.val
    elif root.val in (p, q):
        return True
    elif left:
        return left
    elif right:
        return right
    else:
        False

root = [3,5,1,6,2,0,8,None,None,7,4]
root = build_tree(root, 0)
print(lowestCommonAncestor(root, p = 5, q = 4))

root = [3,5,1,6,2,0,8,None,None,7,4,None,None,None,None]
root = build_tree(root, 0)
print(lowestCommonAncestor(root, p = 5, q = 1))
