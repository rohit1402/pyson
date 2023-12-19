from pyson.Constant import *

class Tokenizer:
    QUOTE = '"'
    WHITESPACE = [' ', '\t', '\b', '\n', '\r']
    BOOL_TRUE = "true"
    BOOL_FALSE = "false"
    NULL = "null"
    SYMBOLS = [
        OPENING_CURLY_BRACKET,
        CLOSING_CURLY_BRACKET,
        OPENING_SQUARE_BRACKET,
        CLOSING_SQUARE_BRACKET,
        COLON,
        COMMA
    ]
    VALID_SYMBOLS = [QUOTE] + WHITESPACE + SYMBOLS + ['+', '-', '.']

    def __init__(self, string: str = "") -> None:
        self._string = string
        self._tokens = []

    def is_eof(self):
        return not self._string

    def _consume_whitespace(self):
        while self._string and self._string[0] in self.WHITESPACE:
            self._string = self._string[1:]

    def _consume_quote_string(self):
        if self._string and self._string[0] != self.QUOTE:
            return None

        self._string = self._string[1:]
        value = ""
        while self._string and self._string[0] != self.QUOTE:
            value += self._string[0]
            self._string = self._string[1:]

        if self._string and self._string[0] == self.QUOTE:
            self._string = self._string[1:]

        if value != "":
            self._tokens.append(value)

    def _consume_number(self):
        value = ""
        number_characters = set(str(d) for d in range(10)) | {'-', '+', '.'}

        while self._string and self._string[0] in number_characters:
            value += self._string[0]
            self._string = self._string[1:]

        if value == "":
            return None

        if '.' in value:
            self._tokens.append(float(value))
        else:
            self._tokens.append(int(value))

    def _consume_bool(self):
        if self._string.startswith(self.BOOL_TRUE):
            self._string = self._string[len(self.BOOL_TRUE):]
            self._tokens.append(True)
        elif self._string.startswith(self.BOOL_FALSE):
            self._string = self._string[len(self.BOOL_FALSE):]
            self._tokens.append(False)

    def _consume_null(self):
        if self._string.startswith(self.NULL):
            self._string = self._string[len(self.NULL):]
            self._tokens.append(None)

    def _consume_symbol(self):
        if self.is_eof():
            return None
        
        char = self._string[0]

        if char in self.VALID_SYMBOLS or char.isalnum():
            if char in self.SYMBOLS:
                symbol = char
                self._string = self._string[1:]
                self._tokens.append(symbol)
        else:
            raise ValueError(f"Unexpected character found: {self._string[0]}")
            

    def tokenize(self) -> list:
        while self._string:
            self._consume_quote_string()
            self._consume_number()
            self._consume_bool()
            self._consume_null()
            self._consume_whitespace()
            self._consume_symbol()

        return self._tokens
