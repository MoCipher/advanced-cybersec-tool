import unittest
from src.core.scanner import Scanner

class TestScanner(unittest.TestCase):

    def setUp(self):
        self.scanner = Scanner()

    def test_scan_network(self):
        result = self.scanner.scan_network('192.168.1.0/24')
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

    def test_scan_vulnerabilities(self):
        result = self.scanner.scan_vulnerabilities('192.168.1.1')
        self.assertIsInstance(result, dict)
        self.assertIn('vulnerabilities', result)

if __name__ == '__main__':
    unittest.main()