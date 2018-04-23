# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root_right, root_left=None):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root_right is None:
            return True
        if root_left is None and root_right is None:
            if root_left.val == root_right.val:
                return True
            else:
                return False
        if root_right is None and root_left is None:
            if root_right.val == root_left.val:
                return True
            else:
                return False
        else:
            return self.isSymmetric(root_right.left, root_right.right) and self.isSymmetric(root_right.right,
                                                                                            root_right.left)


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = lines.__next__()
            root = stringToTreeNode(line);

            ret = Solution().isSymmetric(root)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()