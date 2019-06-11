class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
def isValidBST(root):
    """
    Determines if a tree rooted at root is a valid binary search tree.
    """
    def explore(node): # return order: min, max, bool
        leftMin = node.val
        rightMax = node.val
        leftMax = node.val - 1
        rightMin = node.val + 1
        left = True
        right = True
        if node.left != None:
            leftMin, leftMax, left = explore(node.left)
        if node.right != None:
            rightMin, rightMax, right = explore(node.right)
        return min(min(leftMin, rightMin), node.val),\
                    max(max(leftMax, rightMax), node.val),\
                    left and right and leftMax < node.val and node.val < rightMin
    if root is None:
        return True
    dummy1, dummy2, result = explore(root)
    return result
