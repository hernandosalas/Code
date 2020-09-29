'''
RegEx Cheat Sheet — Python - https://towardsdatascience.com/regex-cheat-sheet-python-3dd0c4b5b4c6
Regular Express in Python - https://medium.com/techtofreedom/regular-express-in-python-cbecba6d57c0
 
\d               matches a single digit character [0-9]
\w               matches any alphabet, digit, or underscore
\s               matches a white space character (space, tab, enter)

Negation

\D               matches a single non-digit character

RegEx Meta Characters
.                matches any character(except for newline character)
^                the string starts with a character
$                the string ends with a character
*                zero or more occurrences 
+                one or more occurrences
?                one or no occurrence 
{}               exactly the specified number of occurrences
|                either or

Examples
"c.t"            will match anything like "cat", "c*t", "c1t", etc
"^a"             will match "a" from "a cat" but not "eat a cake"
"cat$"           will match "a cat" but not "cat party"
"a*b"            will match "b", "ab", "aab", "aaab", ...
"a+b"            will match "ab", "aab", "aaab", ...
"a?b"            will match "b" or "ab"
"a{1}b"          will match "ab"
"a{1,3}b"        will match "ab", "aab", or "aaab"
"cat|dog"        will match "cat" or "dog"

RegEx Sets
[abcd]           matches either a, b, c or d
[a-z0-9]         matches one of the characters from a-z or 0-9
[\w]             matches an alphabet, digit, or underscore
The caret character(^) stands for except
[^\d]            matches a character that is not a digit [0-9]

RegEx Function
findall()        Returns a list that contains all matches       
search()         Returns a 'match object' if there is a match in the string
split()          Returns a list of string that has been split at each match
sub()            Replaces the matches with a string     


The re.match() method is to check whether a regex matches a string or not, if it matches successfully, return a match object, else return None .
The re.split() method could split a string by any characters and any number of characters.

re.group() In addition to simply judging whether a string matches or not, regular expressions also have the power of extracting sub strings!
On a regex, we can use () to indicate the group which needed to be extracted.



Thirdly, there are some more tools to do a more precise match:
- Use [] to indicate a range. For example, [0-9a-z] can match a number between 0 and 9 or a letter between a and z.
- A|B can match A or B, so (P|python) can match ‘Python’ or ‘python’.
- ^ indicates the beginning of the line. For example, ^\d indicates that the string must start with a number.
- $ indicates the end of the line. For example, \d$ indicates that the string must end with a number.
- Use \ to escapes special characters (permitting us to match characters like '*', '?', and so forth).

'''



import re 

# phone_numbers = [] 
# pattern = r"\(([\d\-+]+)\)"

# with open("log.txt", "r") as file: 
#     for line in file: 
#         result = re.search(pattern, line)
#         phone_numbers.append(result.group(1))

# print(phone_numbers)


# print(re.split(r'\s+', 'a b   c')) # ['a', 'b', 'c']
# print(re.split(r'[\s\,]+', 'a,b, c  d')) # ['a', 'b', 'c', 'd']
# print(re.split(r'[\s\,\;]+', 'a,b;; c  d')) # ['a', 'b', 'c', 'd']



time='18:05'
matched = re.match(r'^(0[0-9]|1[0-9]|2[0-3])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])$', time)
print(matched.groups()) # ('18', '05')
print(matched.group()) # '18:05' 
print(matched.group(0)) # '18:05' group(0) returns the original string
print(matched.group(1)) # '18'
print(matched.group(2)) # '05'