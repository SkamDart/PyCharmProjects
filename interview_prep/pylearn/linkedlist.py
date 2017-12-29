class ListNode:

    def __init__(self, val):
        self._val = val

    def __str__(self):
        """
        __str__ is mean to be readable
        :return:
        """
        return ""

    @staticmethod
    def print(head):
        nodes = []
        while True:
            if head is None:
                break
            nodes.append(str(head.val))
            head = head.next

        print('->'.join(nodes))

    @staticmethod
    def get_str(head):
        nodes = []
        while True:
            if head is None:
                break
            nodes.append(head.val)
            head = head.next

        return ''.join(nodes)

    @property
    def val(self):
        return self._val

