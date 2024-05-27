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


def hasPathSum(root, targetSum):
    if not root:
        return False

    if not root.left and not root.right:
        if targetSum == root.val:
            return True
        else:
            return False
    
    left = hasPathSum(root.left, targetSum - root.val)
    right = hasPathSum(root.right, targetSum - root.val)

    return left or right


root = [5,4,8,11,None,13,4,7,2,None,None,None,1]
root = build_tree(root, 0)
hasPathSum(root, targetSum = 22)
