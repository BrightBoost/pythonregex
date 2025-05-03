import re

text = 'He said "hi" and then "bye"'
pattern = r'".*?"'
matches = re.findall(pattern, text)
print(matches)
