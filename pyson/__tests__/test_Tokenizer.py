import unittest
from pyson.Constant import *
from pyson.Tokenizer import Tokenizer

class TestTokenizer(unittest.TestCase):
    def setUp(self):
        self.tokenizer = Tokenizer()

    def test_tokenize_whitespace(self):
        self.tokenizer._string = "  \t\r\n"
        self.tokenizer.tokenize()
        self.assertEqual(self.tokenizer._tokens, [])

    def test_tokenize_quote_string(self):
        self.tokenizer._string = '"Hello, World!"'
        self.tokenizer.tokenize()
        self.assertEqual(self.tokenizer._tokens, ['Hello, World!'])

    def test_tokenize_number(self):
        self.tokenizer._string = "123.45"
        self.tokenizer.tokenize()
        self.assertEqual(self.tokenizer._tokens, [123.45])

    def test_tokenize_bool(self):
        self.tokenizer._string = "true false"
        self.tokenizer.tokenize()
        self.assertEqual(self.tokenizer._tokens, [True, False])

    def test_tokenize_null(self):
        self.tokenizer._string = "null"
        self.tokenizer.tokenize()
        self.assertEqual(self.tokenizer._tokens, [None])

    def test_tokenize_symbol(self):
        self.tokenizer._string = "{}[],:"
        self.tokenizer.tokenize()
        self.assertEqual(self.tokenizer._tokens, [
            OPENING_CURLY_BRACKET,
            CLOSING_CURLY_BRACKET,
            OPENING_SQUARE_BRACKET,
            CLOSING_SQUARE_BRACKET,
            COMMA,
            COLON,
        ])

    def test_tokenize_invalid_character(self):
        self.tokenizer._string = "@"
        with self.assertRaises(ValueError):
            self.tokenizer.tokenize()

if __name__ == "__main__":
    unittest.main()
