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


def rightSideView(root):


    lst = [root]
    tmp = []
    res = []

    while lst:

        if lst[0].left:
            tmp.append(lst[0].left)
        if lst[0].right:
            tmp.append(lst[0].right)

        if len(lst) == 1:
            res.append(lst[0].val)
            lst.extend(tmp)
            tmp = []
        
        lst.pop(0)

    return res


root = [1,2,3,4]
root = build_tree(root, 0)
print(rightSideView(root))


root = [1,2,3,None,5,None,4]
root = build_tree(root, 0)
print(rightSideView(root))