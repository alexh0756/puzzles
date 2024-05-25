def maxDepth(root, depth=0):
    if not root:
        return depth
    return max(
        depth, 
        maxDepth(root.left, depth=depth+1), 
        maxDepth(root.right, depth=depth+1)
        )