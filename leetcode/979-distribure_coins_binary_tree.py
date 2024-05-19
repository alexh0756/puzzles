class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Tree(val: {self.val}, left: {self.left}, right: {self.right})"


def build_tree(root, tree=None):

    if not root or root[0] == None:
        return None

    root_left, root_right = split_root(root)
    tree = TreeNode(val=root[0])
    tree.left = build_tree(root_left)
    tree.right = build_tree(root_right)

    return tree


def split_root(root):

    root_left, root_right = [], []
    depth, i = 1, 1
    while i < len(root):
        if i > depth * 2:
            depth += 1

        if (i - 1) // depth == 0:
            root_right.append(root[i])
        elif (i - 1) // depth == 1:
            root_left.append(root[i])
        i += 1

    return root_left, root_right


def distributeCoins(root) -> int:

    count = 0
    
    if root.left:
        count += distributeCoins(root.left)
        rem_left = root.left.val - 1
        root.left.val = 1
        root.val += rem_left
        count += abs(rem_left)

    if root.right:
        count += distributeCoins(root.right)
        rem_right = root.right.val - 1
        root.right.val = 1
        root.val += rem_right
        count += abs(rem_right)

    return count

root = [1,0,0,None,3]
tree = build_tree(root)
distributeCoins(tree)


root = [3,0,0,0,0,0,0,0,4,0,0,0,0,0,8]
tree = build_tree(root)
distributeCoins(tree)


root = [0,3,0]
tree = build_tree(root)
distributeCoins(tree)