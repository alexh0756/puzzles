# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode(val: {self.val}, left: {self.left}, right: {self.right})"

def build_tree(root, tree=None):

    if not root or root[0] == None:
        return None

    tree = TreeNode(val=root[0])

    node = extract_branch(root, side='left')
    tree.left = build_tree(node, tree=tree)

    node = extract_branch(root, side='right')
    tree.right = build_tree(node, tree=tree)

    return tree


def extract_branch(root, side):

    lst = []

    max_depth = 0
    tmp_val = 1
    while tmp_val < len(root):
        tmp_val *= 2
        max_depth += 1

    for depth in range(max_depth):
        start = (depth * 2) - 1
        if side == 'right':
            start += depth

        node = 0
        while node < depth and start + node < len(root):
            lst.append(root[start+node])
            node += 1

    return lst

class Solution:
    def removeLeafNodes(self, root, target):
        
        if root.left:
            root.left = self.removeLeafNodes(root.left, target)
        if root.right:
            root.right = self.removeLeafNodes(root.right, target)

        if not root.left and not root.right and root.val == target:
            root = None

        return root

solution = Solution()

root = [1,2,3,2,None,2,4]
tree = build_tree(root)
tree = solution.removeLeafNodes(tree, target=2)
print