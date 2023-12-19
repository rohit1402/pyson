from pyson.Constant import *
from pyson.Tokenizer import Tokenizer

class Parser:
    def __init__(self):
        self.tokens = []
        self.skip_bracket_check = False

    def parse(self, string: str):
        self.tokens = Tokenizer(string).tokenize()
        return self._parse_token()

    def _parse_token(self):
        if not self.tokens:
            return {}

        current_token = self.tokens[0]
        if not self.skip_bracket_check and current_token not in [OPENING_CURLY_BRACKET, OPENING_SQUARE_BRACKET]:
            raise Exception(f'Valid JSON should start with {OPENING_CURLY_BRACKET} or {OPENING_SQUARE_BRACKET}')

        self._consume()
        if current_token == OPENING_CURLY_BRACKET:
            return self._parse_object()
        elif current_token == OPENING_SQUARE_BRACKET:
            return self._parse_array()
        else:
            return current_token
        
    def _consume(self, count:int = 1):
        self.tokens = self.tokens[count:]
        return self.tokens

    def _parse_object(self):
        obj = {}

        if self.tokens[0] == CLOSING_CURLY_BRACKET:
            self._consume()
            return obj

        while self.tokens:
            key = self.tokens[0]
            if isinstance(key, str):
                self._consume()
            else:
                raise Exception(f'Expected string key, got: {key}')

            if self.tokens[0] == COLON:
                self._consume()
            else:
                raise Exception(f'Expected colon after key in object, got: {self.tokens[0]}')

            self.skip_bracket_check = True
            val = self._parse_token()
            obj[key] = val

            next_token = self.tokens[0]
            if next_token == CLOSING_CURLY_BRACKET:
                self._consume()
                return obj
            elif next_token != COMMA:
                raise Exception(f'Expected comma after pair in object, got: {next_token}')

            self._consume()

        raise Exception('Expected end-of-object bracket')

    def _parse_array(self):
        arr = []

        current_token = self.tokens[0]
        if current_token == CLOSING_SQUARE_BRACKET:
            self._consume()
            return arr

        while self.tokens:
            self.skip_bracket_check = True
            token = self._parse_token()
            arr.append(token)

            next_token = self.tokens[0]
            if next_token == CLOSING_SQUARE_BRACKET:
                self._consume()
                return arr
            elif next_token != COMMA:
                raise Exception('Expected comma after object in array')
            else:
                self._consume()

        raise Exception('Expected end-of-array bracket')
