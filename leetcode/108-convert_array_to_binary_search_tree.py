class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self) -> str:
        return f"node(val: {self.val}, left: {self.left}, right: {self.right})"



def sortedArrayToBST(nums):

    if not nums:
        return

    mid = len(nums) // 2

    tree = TreeNode(nums[mid])
    tree.left = sortedArrayToBST(nums[:mid])
    tree.right = sortedArrayToBST(nums[mid+1:])

    return tree
    

print(sortedArrayToBST(nums = [-10,-3,0,5,9]))
print(sortedArrayToBST(nums = [1, 3]))