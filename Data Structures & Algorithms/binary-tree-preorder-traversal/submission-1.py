# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                ans.append(curr.val)
                curr = curr.left
                
            curr = stack.pop()
            curr = curr.right
            
        return ans
        # while curr or stack:
        #     while curr:
        #         stack.append(curr)
        #         curr = curr.left
        #     curr = stack.pop()
        #     res.append(curr.val)
        #     curr = curr.right
        # return res

        # def preorder(root):
        #     while not root:
        #         return
            
        #     ans.append(root.val)
        #     preorder(root.left)
        #     preorder(root.right)
        # preorder(root)
        # return ans
    
