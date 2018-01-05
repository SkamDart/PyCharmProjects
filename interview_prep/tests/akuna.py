from unittest import TestCase
from company.akuna import MapSum

s = MapSum()
s.insert("apple", 3)
assert 3 == s.sum("ap")
s.insert("app", 2)
assert 5 == s.sum("ap")

class TestAkuna(TestCase):

    def setUp(self):
        pass

    def test_constructor(self):
        pass

