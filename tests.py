import unittest
import answer

class TestReadLogs(unittest.TestCase):
    def test_read_logs_valid_input(self):
        input_file = "valid_input.txt"
        expected_output = [
            (1, 'P', 1, 1),
            (2, 'S', 100, 2),
            (3, 'T', 98, 3)
        ]
        self.assertEqual(answer.read_logs(input_file), expected_output)

    def test_read_logs_empty_input(self):
        input_file = "empty_input.txt"
        expected_output = []
        self.assertEqual(answer.read_logs(input_file), expected_output)
    
class TestCalculateResults(unittest.TestCase):
    def test_calculate_results_valid_input(self):
        logs = [(1, 'P', 100, 1), (1, 'S', 6, 2), (1, 'T', 98, 3)]
        expected_output = {'507': (1000, 1000, 6)}
        self.assertEqual(answer.calculate_results(logs), expected_output)

    def test_calculate_results_empty_input(self):
        logs = []
        expected_output = {}
        self.assertEqual(answer.calculate_results(logs), expected_output)

class TestPrintResults(unittest.TestCase):
    def test_print_results_valid_input(self):
        results = {'507': (1000, 1000, 6)}
        expected_output = '507 1000 1000 6\n'
        self.assertEqual(answer.print_results(results), expected_output)

    def test_print_results_empty_input(self):
        results = {}
        expected_output = ''
        self.assertEqual(answer.print_results(results), expected_output)

if __name__ == '__main__':
    unittest.main()