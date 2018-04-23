# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = []
        out_list=[]
        if root is not None:
            queue.append(root)
            level_count = 1
            current_count = 0
            while len(queue) > 0:
                temp_list = []
                while level_count > 0:
                    current = queue.pop(0)
                    print (current.val)
                    temp_list.append(current.val)
                    level_count-=1
                    if current.left is not None:
                        queue.append(current.left)
                        current_count+=1
                    if current.right is not None:
                        queue.append(current.right)
                        current_count+=1
                    if level_count == 0:
                        print ('\n')
                        out_list.append(temp_list)

                level_count = current_count
                current_count = 0
            print (out_list)


Node = TreeNode(3)
Node.left = TreeNode(9)
Node.right = TreeNode(20)
Node.right.left = TreeNode(15)
Node.right.right = TreeNode(7)
sol = Solution()
sol.levelOrder(Node)