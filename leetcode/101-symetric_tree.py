class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self) -> str:
        return f"tree(val: {self.val}, left: {self.left}, right: {self.right})"

def build_tree(root, index):

    tree = TreeNode(root[index])
    if 2*index+1 < len(root):
        tree.left = build_tree(root, 2*index+1)
    if 2*index+2 < len(root):
        tree.right = build_tree(root, 2*index+2)

    return tree


def isSymmetric(root):

    def compare(left, right):

        if left == right == None:
            return True
        elif left == None or right == None:
            return False

        outcome = True
        outcome = outcome and (left.val == right.val)
        outcome = outcome and compare(left.left, right.right)
        outcome = outcome and compare(left.right, right.left)

        return outcome

    outcome = compare(root.left, root.right)

    return outcome

root = [1,2,2,3,4,4,3]
root = build_tree(root, 0)
print(isSymmetric(root))

root = root = [1,2,2,None,3,None,3]
root = build_tree(root, 0)
print(isSymmetric(root))