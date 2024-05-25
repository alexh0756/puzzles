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

# def isSymmetric(root):

#     if root.left == root.right == None:
#         return True

#     vals = root.left.val == root.right.val
#     exists_left = (root.left.left != None) == (root.right.right != None)
#     exists_right = (root.left.right != None) == (root.right.left != None)

#     vals_left = True
#     if root.left.left and root.right.right:
#         vals_left = root.left.left.val != root.right.right.val
#     vals_right = True
#     if root.left.right and root.right.left:
#         vals_right = root.left.right.val != root.right.left.val if exists_left else True

#     outcome = vals and exists_left and exists_right and vals_left and vals_right and isSymmetric(root.left) and isSymmetric(root.right)

#     return outcome


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