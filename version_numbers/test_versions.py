from versions import versionCompare
import unittest

class TestDivide(unittest.TestCase):

    def test_0(self):
        self.assertEqual(versionCompare("0.1", "1.1"), -1)

    def test_neg_1(self):
        self.assertEqual(versionCompare("1.0.1", "1"), 1)

    def test_neg_2(self):
        self.assertEqual(versionCompare("7.5.2.4", "7.5.3"), -1)

    def test_3(self):
        self.assertEqual(versionCompare("1.01", "1.001"), 0)

if __name__ == '__main__':
    unittest.main()
