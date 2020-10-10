'''
22 Pythonic Tricks for Working with Strings
https://medium.com/python-in-plain-english/22-pythonic-tricks-for-working-with-strings-8b893776743c
'''

'''
Is a Substring in a String?
'''

def sub_00(haystack: str="", needle:str="") -> bool:
    return needle in haystack

# assert sub_00("the quick brown fox jumped over the lazy dog", "lazy") == True
# assert sub_00("the quick brown fox jumped over the lazy dog", "lazys") == False

'''
Reverse a String
'''
def string_reverse(forward: str = "") -> str:
    return forward[::-1]

# assert string_reverse("hello") == "olleh"
# assert string_reverse("goodbye") != "goodbye"

'''
Compare Two Strings for Equality
'''
def are_equal(first_comparator: str = "", second_comparator: str = "") -> bool:
    return first_comparator == second_comparator


# assert are_equal("thing one", "thing two") is False
# assert are_equal("a thing", "a " + "thing") is True

'''
Lowercase, Uppercase, Sentence Case and Title Case of a String
'''
def to_uppercase(input_string:str) -> str:
    return input_string.upper()

def to_lowercase(input_string:str) -> str:
    return input_string.lower()

def to_sentencecase(input_string:str) -> str:
    return input_string.capitalize()

def to_titlecase(input_string:str) -> str:
    return input_string.title()

def to_swapcase(input_string:str) -> str:
    return input_string.swapcase()

# assert to_uppercase("the end of time") == "THE END OF TIME"
# assert to_lowercase("The End Of Time") == "the end of time"
# assert to_sentencecase("The End of Time") == "The end of time"
# assert to_titlecase("the end of time") == "The End Of Time"
# assert to_swapcase("The End Of Time") == "tHE eND oF tIME"

'''
Concatenate Strings Efficiently
'''
def concatenate(*argv)->str:
    return ''.join(argv)

# assert concatenate("a", "b", "c") == "abc"

'''
Is the String Empty or None?
'''
def is_null_or_blank(input_string: str = "") -> bool:
    if input_string: 
        if input_string.strip():
            return False
    return True

# assert is_null_or_blank(None) == True
# assert is_null_or_blank("") == True
# assert is_null_or_blank("  ") == True
# assert is_null_or_blank(" d ") == False

'''
Trim Leading and Trailing Whitespace
'''
def strip_it(input_string: str) -> tuple:
    return (input_string.lstrip(), input_string.rstrip(), input_string.strip())

# left, right, full = strip_it("  A padded  string   ")
# assert left == "A padded  string   "
# assert right == "  A padded  string"
# assert full == "A padded  string"

'''
Generate a String of Random Characters
'''

import string
import secrets

def generate_random_string(length: int = 0) -> str:
    result = "".join(
        secrets.choice(string.ascii_letters + string.digits)
        for _ in range(length))
    return result

# assert len(generate_random_string(20)) == 20

'''
Read the Lines in a File to a List
'''
def file_to_list(filename: str = "") -> list:
    with open(filename, "r") as f:
        lines = list(f)
    return lines

# assert len(file_to_list("<PATH TO FILE>")) == LINE_COUNT

'''
Tokenize a Sentence Fully
'''
import nltk

def tokenize_text(input_str: str = "") -> list:
    return nltk.wordpunct_tokenize(input_str)

# assert tokenize_text("Good muffins cost $3.88\nin New York.") == [
#     "Good",
#     "muffins",
#     "cost",
#     "$",
#     "3",
#     ".",
#     "88",
#     "in",
#     "New",
#     "York",
#     ".",
# ]

'''
Execute Python Code Found Inside a String
'''
import subprocess
import ast

def exec_string(input_string: str = "") -> str:
    result = subprocess.getoutput(input_string)
    return result

def eval_string(input_string: str = "") -> str:
    result = ast.literal_eval(input_string)
    return str(result)

# assert exec_string("ls -l")
# assert eval_string("{ 'key':'value' }") == "{'key': 'value'}"

'''
Find the Substring Between Two Markers
'''
import re

def between(first: str = "", second: str = "", input_string="") -> str: 
    m = re.search(f"{first}(.+?){second}", input_string)
    if m:
        return m.group(1)
    else:
        return ""

# assert between(input_string="adCCCTHETEXTZZZdfhewihu", first="CCC", second="ZZZ") == "THETEXT"

'''
Remove all Punctuation from a String
'''
import string

def remove_punctuation(input_string: str = "") -> str:
    return input_string.translate(str.maketrans("", "", string.punctuation))

# assert remove_punctuation("Hello!") == "Hello"
# assert remove_punctuation("He. Saw! Me?") == "He Saw Me"

'''
Encode and Decode UTF-8 URLs
'''
import urllib.parse

def encode_url(url: str = "") -> str:
    return urllib.parse.quote(url)

def decode_url(url: str = "") -> str:
    return urllib.parse.unquote(url)

# assert (encode_url("example.com?title=¨ˆπœ˚∑π") ==
#         "example.com%3Ftitle%3D%C2%A8%CB%86%CF%80%C5%93%CB%9A%E2%88%91%CF%80")
# assert decode_url("example.com?title=%a0%f7%b1") == "example.com?title=���"


'''
Use Base64 Encoding on Strings
'''
import base64

def encode_b64(input_string: str = "") -> object:
    return base64.b64encode(input_string.encode("utf-8"))


def decode_b64(input_string: str = "") -> object:
    return base64.b64decode(input_string).decode("utf-8")

# assert encode_b64("Hello") == b"SGVsbG8="
# assert decode_b64(b"SGVsbG8=") == "Hello"

'''
Calculate the Similarity of Two Strings
'''
import difflib

def similarity(left: str = "", right: str = "") -> float:

    seq = difflib.SequenceMatcher(None, left, right)
    return seq.ratio()

# assert similarity("I like bananas", "I like bananarama") >= 0.80
# assert similarity("I like bananas", "The quick brown fox") <= 0.25

'''
Remove a Character at a Specific Index
'''
def remove_by_index(original: str = "", index: int = -1) -> tuple:
    if len(original) >= index and index >= 0:
        return (original[:index] + original[index + 1:], original[index])
    else:
        return (original, "")

# assert remove_by_index("0123456789", 5) == ("012346789", "5")

'''
Convert Between CSV and List
'''
def from_csv_line(line: str = "") -> list:
    return line.split(",")

# assert from_csv_line("a,b,c") == ["a", "b", "c"]

def from_list(line: list = []) -> str:
    ret = ", ".join(e for e in line)
    return ret

# assert from_list(["a", "b", "c"]) == "a, b, c"
# assert from_list(["one", "two", "three"]) == "one, two, three"

'''
Weave Two Strings
'''
import itertools

def interleave(left: str = "", right: str = "") -> str:

    return "".join(
        [i + j for i, j in itertools.zip_longest(left, right, fillvalue="")])

# assert interleave("ABCD", "01") == "A0B1CD"

'''
Remove Unwanted Characters from a String
'''

def remove_unwanted(original: str = "",
                    unwanted: str = "",
                    replacement: str = "") -> str:                 
    return original.replace(unwanted, replacement)


# assert remove_unwanted(original="M'The Real String'",
#                        unwanted="M") == "'The Real String'"

'''
Find the Index Locations of a Character in a String
'''
def find_char_locations(original: str = "", character: str = "") -> list:

    return [index for index, char in enumerate(original) if char == character]


# assert find_char_locations("The jolly green giant.", "e") == [2, 12, 13]

'''
Translate a String to Leetspeak
'''
def to_leetspeak(normal_speak:str="") -> str:

    leet_mapping = str.maketrans("iseoau", "1530^Ü")
    return normal_speak.translate(leet_mapping).title().swapcase()

# assert to_leetspeak("the quick brown fox jumped over the lazy dogs") == \
#     "tH3 qÜ1cK bR0wN f0x jÜMP3d 0v3r tH3 l^zY d0g5"

