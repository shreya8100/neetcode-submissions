# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        currentNode = root
        result = TreeNode()

        while currentNode:
            if p.val > currentNode.val and q.val > currentNode.val:
                currentNode = currentNode.right
            elif p.val < currentNode.val and q.val < currentNode.val:
                currentNode = currentNode.left
            elif (p.val < currentNode.val and q.val > currentNode.val) or (p.val > currentNode.val and q.val < currentNode.val) or p.val == currentNode.val or q.val == currentNode.val:
                result = currentNode
                break
        
        return result