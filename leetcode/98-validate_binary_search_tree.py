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




def isValidBST(root):

    def walk(root, prev=None):

        if not root:
            return True, prev
        if not root.left and not root.right:
            if not prev != None:
                return True, root.val
            elif prev >= root.val:
                return False, prev
            else:
                return True, root.val
            
        valid, prev = walk(root.left, prev)
        if not valid:
            return valid, prev

        if prev != None and prev >= root.val:
            valid = False
        prev = root.val
        if not valid:
            return valid, prev
        
        valid, prev = walk(root.right, prev)
        if not valid:
            return valid, prev

        return valid, prev

    return walk(root)[0]

root = [-1,0,1]
root = build_tree(root, 0)
print(isValidBST(root))


root = [0,None,-1]
root = build_tree(root, 0)
print(isValidBST(root))


root = [0,None,1]
root = build_tree(root, 0)
print(isValidBST(root))

root = [0,-1]
root = build_tree(root, 0)
print(isValidBST(root))

root = [5,1,4,None,None,3,6]
root = build_tree(root, 0)
print(isValidBST(root))


root = [2,1,3]
root = build_tree(root, 0)
print(isValidBST(root))