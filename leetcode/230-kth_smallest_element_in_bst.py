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



def kthSmallest(root, k):

    def walk(root, k):

        if not root:
            return root, k
        if not root.left and not root.right:
            return root.val, k - 1
        
        val, k = walk(root.left, k)
        if k == 0:
            return val, k
        
        val = root.val
        k -= 1

        if k == 0:
            return val, k
        
        val, k = walk(root.right, k)
        if k == 0:
            return val, k

        return val, k

    return walk(root, k)[0]

root = [3,1,4,None,2]
root = build_tree(root, 0)
print(kthSmallest(root,k=1))


root = [3,9,20,None,None,15,7]
root = build_tree(root, 0)
print(kthSmallest(root,k=1))