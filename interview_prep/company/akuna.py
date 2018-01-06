class TrieNode(object):
    def __init__(self, value=0):
        self.value = value
        self.children = {}

    def find(self, prefix):
        node = self
        for char in prefix:
            if char not in node.children:
                return TrieNode()
            node = node.children[char]
        return node

    def insert(self, key, value):
        node = self
        delta = value - self.find(key).value
        node.value += value

        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]
            node.value += value

        node.value += delta

    def sum(self, prefix):
        node = self.find(prefix)
        print("{} - >{}".format(prefix, node.value))
        return self.find(prefix).value

class MapSum(object):

    def __init__(self):
        self.head = TrieNode()

    def get_value(self, key):
        node = self.head
        for char in key:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.value

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        node = self.head
        delta = val - self.get_value(key)

        node.value += delta
        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]
            node.value += delta

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        node = self.head
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.value

class NaieveMapSum(object):

    def __init__(self):
        self.data = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.data[key] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        return sum([self.data[k] for k in self.data if k.startswith(prefix)])