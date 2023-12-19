# pyson
A simple python based JSON parser

## Features
- Parse JSON strings into Python objects
- Support for nested objects and arrays
- Error handling for malformed JSON input
- Designed for simplicity and ease of use

## Usage
```
from pyson import parse

# Parse a JSON string
json_string = '{"key": "value", "nested": {"inner": 42}, "array": [1, 2, 3]}'
parsed_result = parse(json_string)

# Use the parsed result as a Python object
print(parsed_result)
```

## Examples
```
json_object = '{"name": "JohnD", "age": 30, "city": "Delhi"}'
```
```
parsed_object = parse(json_object)
```
```
print(parsed_object)
```


## Motivation
Building a JSON parser is an easy way to learn about parsing techniques which are useful for everything from parsing simple data formats through to building a fully featured compiler for a programming language.

JSON (which stands for JavaScript Object Notation) is a lightweight data-interchange format, which is widely used for transmitting data over the Internet.

## Reference Articles
- [Writing a Parser: Getting Started](https://supunsetunga.medium.com/writing-a-parser-getting-started-44ba70bb6cc9)
- [Writing a Parser: Algorithms and Implmentation](https://supunsetunga.medium.com/writing-a-parser-algorithms-and-implementation-a7c40f46493d)


### Feel free to contribute, report issues, or suggest improvements. Happy parsing 🚀

