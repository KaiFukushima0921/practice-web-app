import unittest
import sample

class TestStringMethods(unittest.TestCase):
    def test_add_num(self):
        self.assertEqual(7,sample.add_num(3,4))

    def test_is_positive(self):
        self.assertTrue(sample.is_positive(3))
        self.assertTrue(sample.is_positive(0))
        self.assertFalse(sample.is_positive(-1))