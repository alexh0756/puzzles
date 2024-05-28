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


class BSTIterator:

    def __init__(self, root):
        self.root = self.connect(self.inorder_traversal(root))
        self.node = self.root[0]



    def inorder_traversal(self, root):
    
        if root == None:
            return []

        lst = []
        lst.extend(self.inorder_traversal(root.left))
        lst.append(root)
        lst.extend(self.inorder_traversal(root.right))

        return lst
    
    def connect(self, root):
        i = 0
        while i < len(root) - 1:
            root[i].next = root[i+1]
            i += 1
        root[-1].next = None
        return root

    def next(self):
        val = self.node.val
        self.node = self.node.next
        return val

        

    def hasNext(self):
        if self.node:
            return True
        else:
            return False


  
root = [7, 3, 15, None, None, 9, 20]
root = build_tree(root, 0)
bSTIterator = BSTIterator(root)

print(bSTIterator.next())
print(bSTIterator.next())
print(bSTIterator.hasNext())
print(bSTIterator.next())
print(bSTIterator.hasNext())
print(bSTIterator.next())
print(bSTIterator.hasNext())
print(bSTIterator.next())
print(bSTIterator.hasNext())

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()