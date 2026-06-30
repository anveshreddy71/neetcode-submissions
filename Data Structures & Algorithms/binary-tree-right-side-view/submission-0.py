# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque()
        if root:
            queue.append(root)
        level = 0
        res = []
        while len(queue)>0:
            level_list = []
            for i in range(len(queue)):
                curr = queue.popleft()
                level_list.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            level+=1
            res.append(level_list)
        return [x[-1] for x in res]
        