import unittest
from pyson.Parser import Parser

class TestParser(unittest.TestCase):
    def test_parse_object(self):
        parser = Parser()
        result = parser.parse('{"key": "value", "nested": {"inner": 42}, "array": [1, 2, 3]}')
        expected = {"key": "value", "nested": {"inner": 42}, "array": [1, 2, 3]}
        self.assertEqual(result, expected)

    # def test_parse_array(self):
    #     parser = Parser()
    #     result = parser.parse('[1, "two", {"three": 3}, [4, 5]]')
    #     expected = [1, "two", {"three": 3}, [4, 5]]
    #     self.assertEqual(result, expected)

    def test_parse_malformed_json(self):
        parser = Parser()
        with self.assertRaises(Exception):
            parser.parse('{"key": "value", "missing_colon" 42}')

if __name__ == '__main__':
    unittest.main()
