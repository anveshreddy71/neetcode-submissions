# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        '''
        1. when there are no child, just make prev connection to none
        2. when one child is there, just make prev connection to next one
        3. when two childs are there, find minimum on right side, replace that
        with node value and delete that node
        '''
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            min_node = self.findminimum(root.right)
            root.val = min_node.val
            root.right = self.deleteNode(root.right, min_node.val)
        
        return root


    def findminimum(self, root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr
    

    

        

