import unittest
import functions

class test_function_F(unittest.TestCase):

    def test_F_Neg(self):
        with self.assertRaises(AssertionError):
            functions.F(-1)

    def test_F_0(self):
        self.assertEqual(functions.F(0), [0])

    def test_F_1(self):
        self.assertEqual(functions.F(1), [0,1])

    def test_F_15(self):
        self.assertEqual(functions.F(15), [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610])

if __name__ == '__main__':
    unittest.main(verbosity=2)
