import re

text = "The quick brown fox jumps over the lazy dog."

shortword = re.compile(r'\W*\b\w{1,4}\b')

print(shortword.sub('',text))