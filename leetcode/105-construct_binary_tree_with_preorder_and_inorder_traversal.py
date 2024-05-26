class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self) -> str:
        return f"tree(val: {self.val}, left: {self.left}, right: {self.right})"


def buildTree(preorder, inorder):

    if inorder:
        idx = inorder.index(preorder.pop(0))
        node = TreeNode(inorder[idx])

        node.left = buildTree(preorder, inorder[:idx])
        node.right = buildTree(preorder, inorder[idx+1:])

        return node


buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7])
# buildTree(preorder = [1,2,4,5,3,6], inorder = [4,2,5,1,3,6])
# buildTree(preorder = [3,9,4,1,11,20,15,6,2,7,6], inorder = [1,4,11,9,3,6,15,2,20,8,7])
