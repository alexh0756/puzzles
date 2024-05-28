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


def maxPathSum(root):

    def traverse(root):
        if not root:
            return 0, -1000

        left_cont, left_max = traverse(root.left)
        right_cont, right_max = traverse(root.right)
        
        running_max = max(
            root.val,
            left_cont + root.val,
            right_cont + root.val,
        )
        cur_max = max(
            running_max,
            left_max,
            right_max,
            root.val,
            left_cont + right_cont + root.val
            )

        return running_max, cur_max

    _, path_max = traverse(root)

    return path_max


root = [-10]
root = build_tree(root, 0)
print(maxPathSum(root))


root = [-10,9,20,None,None,15,7]
root = build_tree(root, 0)
print(maxPathSum(root))