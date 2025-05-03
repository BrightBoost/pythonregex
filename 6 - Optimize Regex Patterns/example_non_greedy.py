import re

text = "<p>Hello</p><p>Pluralsight</p>"
pattern = r"<.*?>" # extra ?
matches = re.findall(pattern, text)
print(matches)
