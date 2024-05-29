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


def averageOfLevels(root):

    nodes = [[root]]
    i = 0
    while i < len(nodes):
        for node in nodes[i]:
            if i + 1 == len(nodes):
                nodes.append([])
            if node.left:
                nodes[i+1].append(node.left)
            if node.right:
                nodes[i+1].append(node.right)
        i += 1
    vals = [[root.val for root in l] for l in nodes]
    lst = []
    for v in vals:
        if v:
            lst.append(sum(v)/len(v))


    return lst


root = [3,9,20,None,None,15,7]
root = build_tree(root, 0)
print(averageOfLevels(root))