import unittest
import answer
from answer import print_results

class TestLast(unittest.TestCase):
    def tests_assign_function(self):
        actual = answer.print_results(["2", "507 P 1000 1", "1 S 6 2", "1 T 98 3"])
        self.assertEqual(actual, ('507 1000 1000 6'))

    

if __name__ == '__main__':
    unittest.main()