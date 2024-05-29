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

    if not root:
        return root

    nodes = [[root]]
    i = 0
    dir = 1
    while i < len(nodes):
        j = 0
        while j < len(nodes[i]):
            node = nodes[i][j]
            if (i+1) == len(nodes):
                nodes.append([])
            # if dir == 0 and node.left:
            if node.left:
                nodes[i+1].append(node.left)
            if node.right:
                nodes[i+1].append(node.right)
            # if dir == 1 and node.left:
            #     nodes[i+1].append(node.left)
            j += 1
        dir = (dir + 1) % 1
        i += 1

    vals = [[root.val for root in l] for l in nodes if l]
    for i in range(len(vals)):
        if (i % 2) == 1:
            a, b = 0, len(vals[i]) - 1
            while a < b:
                vals[i][a], vals[i][b] = vals[i][b], vals[i][a]
                a += 1
                b -= 1

    return vals


root = [0,2,4,1,None,3,-1,5,1,None,None,6,None,None,8] # [[0],[4,2],[1,3,-1],[8,6,1,5]]
root = build_tree(root, 0)
print(averageOfLevels(root))


root = [3,9,20,None,None,15,7]
root = build_tree(root, 0)
print(averageOfLevels(root))