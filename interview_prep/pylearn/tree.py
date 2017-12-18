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
                #print(level)
                averages.append(sum(level) / len(level))
                level = []

            while level_queue:
                cur = level_queue.popleft()
                level.append(cur.val)
                self.append_valid(cur, queue)

            if level:
                averages.append(sum(level) / len(level))
                #print(level)
                level = []

        return averages


"""
t = TreeNode(0)
small = TreeNode(1)
small.left = TreeNode(2)
small.right = TreeNode(3)
small.left.left = TreeNode(4)
small.left.right = TreeNode(5)
small.right.left = TreeNode(6)
small.right.right = TreeNode(7)

t.averageOfLevels(small)
"""


