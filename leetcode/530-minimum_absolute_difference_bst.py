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


def getMinimumDifference(root):

    if not root:
        return None
    if not root.left and not root.right:
        return None

    left = getMinimumDifference(root.left)
    right = getMinimumDifference(root.right)

    min_val = 1000000
    if left:
        min_val = min(min_val, left)
    if right:
        min_val = min(min_val, right)

    if root.left:
        min_val = min(min_val, abs(root.val - root.left.val))
    if root.right:
        min_val = min(min_val, abs(root.val - root.right.val))

    return min_val


def getMinimumDifference(root):

    def walk(root, prev):
        if not root:
            return prev, 10**6
        if not root.left and not root.right:
            if prev != None:
                min_cur = root.val - prev
            else:
                min_cur = 10**6
            return root.val, min_cur

        prev, min_cur = walk(root.left, prev)
        if prev:
            min_cur = min(root.val - prev, min_cur)
            
        prev, min_left = walk(root.right, root.val)
        if prev:
            min_cur = min(min_cur, min_left)

        return prev, min_cur

    _, min_val = walk(root, None)
    return min_val


root = [0,None,2236,None,None,1277,2776,None,None,None,None,519]
root = build_tree(root, 0)
print(getMinimumDifference(root))


root = [4,2,6,1,3]
root = build_tree(root, 0)
print(getMinimumDifference(root))


root = [1,None,3,None,None,2,None]
root = build_tree(root, 0)
print(getMinimumDifference(root))


root = [236,104,701,None,227,None,911]
root = build_tree(root, 0)
print(getMinimumDifference(root))


root = [4,2,6,1,3]
root = build_tree(root, 0)
print(getMinimumDifference(root))