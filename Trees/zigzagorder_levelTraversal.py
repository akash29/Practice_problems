# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root):
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
            level = 0
            while len(queue) > 0:
                temp_list = []
                level+=1
                while level_count > 0:
                    if level % 2 ==0:
                        current = queue.pop()
                    else:
                        current = queue.pop(0)
                    #current = queue.pop(0)
                    print (current.val)
                    temp_list.append(current.val)
                    level_count-=1
                    if level % 2 == 0:
                        if current.right is not None:
                            queue.insert(0,current.right)
                            current_count += 1
                        if current.left is not None:
                            queue.insert(0,current.left)
                            current_count += 1
                    else:

                        if current.left is not None:
                            queue.append(current.left)
                            current_count+=1
                        if current.right is not None:
                            queue.append(current.right)
                            current_count+=1
                    if level_count == 0:
                        print ("level:",level)
                        print ('\n')
                        out_list.append(temp_list)

                level_count = current_count
                current_count = 0
            return out_list
        else:
            return out_list

Node = TreeNode(1)
Node.left = TreeNode(2)
Node.right = TreeNode(3)
Node.left.left = TreeNode(4)
Node.right.right = TreeNode(5)
sol = Solution()
sol.zigzagLevelOrder(Node)