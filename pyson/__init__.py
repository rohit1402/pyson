from pyson.Parser import Parser

def parse(string: str) -> dict:
    return Parser().parse(string)