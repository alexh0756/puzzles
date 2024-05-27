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


def sumNumbers(root):

    def traverse(root):

        if not root:
            return ['']

        lst = []
        if root.left:
            lst.extend([str(root.val) + str(val) for val in traverse(root.left)])
        if root.right:
            lst.extend([str(root.val) + str(val) for val in traverse(root.right)])
        if not lst:
            lst.append(str(root.val))

        return lst
    
    lst = traverse(root)
    lst = list(map(int, lst))

    return sum(lst)

root = [4,9,0,5,1]
root = build_tree(root, 0)
print(sumNumbers(root))


root = [1,2,3]
root = build_tree(root, 0)
print(sumNumbers(root))