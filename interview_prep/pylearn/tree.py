from sys import maxsize
from collections import deque


class ListNode:

    def __init__(self, val, next):
        self._next = next
        self._val = val

    @property
    def next(self):
        return self._next

    @property
    def val(self):
        return self._val


class TreeNode:

    def __init__(self, x):
        self._val = x
        self._left = None
        self._right = None

    def __str__(self):
        return "{}".format(self.val)

    def __repr__(self):
        return "{}".format(self.val)

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @property
    def val(self):
        return self._val

    @left.setter
    def left(self, left):
        self._left = left

    @right.setter
    def right(self, right):
        self._right = right

    def append_valid(self, root, queue):
        """
        Assumes queue is a deque
        appends to queue iff it is not a falsey value
        :param root:
        :param queue:
        :return:
        """
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)

    def averageOfLevels(self, root):
        """
        https://leetcode.com/problems/average-of-levels-in-binary-tree/description/
        :param root:
        :return:
        """
        if root is None:
            return []

        queue = deque([root])
        level_queue = deque()
        level = []
        averages = []

        while queue or level_queue:

            while queue:
                cur = queue.popleft()
                level.append(cur.val)
                self.append_valid(cur, level_queue)

            if level:
                averages.append(sum(level) / len(level))
                level = []

            while level_queue:
                cur = level_queue.popleft()
                level.append(cur.val)
                self.append_valid(cur, queue)

            if level:
                averages.append(sum(level) / len(level))
                level = []

        return averages

    def levelOrder(self, root):
        """
        https://leetcode.com/problems/binary-tree-level-order-traversal/description/
        :param root:
        :return:
        """
        if root is None:
            return []

        q1 = deque([root])
        q2 = deque([])
        levels = []
        level = []

        while q1 or q2:

            while q1:
                node = q1.popleft()
                level.append(node.val)
                self.append_valid(node, q2)

            if level:
                levels.append(level)
                level = []

            while q2:
                node = q2.popleft()
                level.append(node.val)
                self.append_valid(node, q1)

            if level:
                levels.append(level)
                level = []

        return levels

    def zigzagLevelOrder(self, root):
        """
        https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q1 = deque([root])
        q2 = deque()
        level = []
        levels = []
        should_flip = False

        while q1 or q2:

            while q1:
                node = q1.popleft()
                level.append(node.val)
                self.append_valid(node, q2)

            if level:
                if should_flip:
                    levels.append(list(reversed(level)))
                else:
                    levels.append(level)
                should_flip = not should_flip
                level = []

            while q2:
                node = q2.popleft()
                level.append(node.val)
                self.append_valid(node, q1)

            if level:
                if should_flip:
                    levels.append(list(reversed(level)))
                else:
                    levels.append(level)
                should_flip = not should_flip
                level = []

        return levels

t = TreeNode(0)
small = TreeNode(1)
small.left = TreeNode(2)
small.right = TreeNode(3)
small.left.left = TreeNode(4)
small.left.right = TreeNode(5)
small.right.left = TreeNode(6)
small.right.right = TreeNode(7)

"""
print(t.levelOrder(small))
t.averageOfLevels(small)
t.zigzagLevelOrder(head)
t.zigzagLevelOrder(small)
"""

head = TreeNode(3)
head.left = TreeNode(9)
head.right = TreeNode(20)
head.right.left = TreeNode(15)
head.right.right = TreeNode(7)
