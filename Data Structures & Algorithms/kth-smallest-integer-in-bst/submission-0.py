# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        bag = []

        def findsmallest(root):
            if not root:
                return 


            findsmallest(root.left)
            bag.append(root.val)
            findsmallest(root.right)

            

        findsmallest(root)
        return bag[k - 1]

        
