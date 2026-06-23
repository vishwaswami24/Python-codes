import re

# Define token patterns using regular expressions
token_patterns = [
    ("LITERAL_STRING", r'"[^"]*"|\'[^\']*\''),
    ("LITERAL_FLOAT", r'\b\d+\.\d+\b'),
    ("LITERAL_INTEGER", r'\b\d+\b'),
    ("IDENTIFIER", r'\b[a-zA-Z_][a-zA-Z_0-9]*\b'),
    ("DELIMITER", r'[\[\]\(\)\{\},;]'),
    ("UNKNOWN", r'.'),  # Matches any single character (used as a fallback)
]

# Compile regex patterns
token_regex = [(name, re.compile(pattern)) for name, pattern in token_patterns]

def tokenize(code):
    tokens = []
    index = 0
    while index < len(code):
        match = None
        for token_name, regex in token_regex:
            match = regex.match(code, index)
            if match:
                token_text = match.group(0)
                if token_name != "UNKNOWN" or token_text.strip():  # Ignore pure whitespace
                    tokens.append((token_name, token_text))
                index = match.end()
                break
        if not match:  # Should not happen, but just in case
            tokens.append(("UNKNOWN", code[index]))
            index += 1
    return tokens

code = 'x = 42; y = 3.14; print("hello"); z = a_b1'
tokens = tokenize(code)

for token in tokens:
    print(token)