import unittest
from main import Converter

class TestMain(unittest.TestCase):
    def test_100_7(self):
        self.assertEqual(Converter.do(100.7), 1000)
        self.assertEqual(Converter.do(200.5), 1000)
        
    def test_0_100_7(self):
        self.assertEqual(Converter.do(10.5), 10)
        self.assertEqual(Converter.do(100.6), 100)

    def test_0(self):
        with self.assertRaises(ValueError):
            Converter.do(0)

    def test_30_0(self):
        self.assertEqual(Converter.do(-1.1), -6)
        self.assertEqual(Converter.do(-30.4), -35)

    def test_under30(self):
        self.assertEqual(Converter.do(-30.5), -2000)
        
if __name__ == "__main__":
    unittest.main();
