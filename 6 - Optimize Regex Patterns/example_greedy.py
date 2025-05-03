import re

text = "<p>Hello</p><p>Pluralsight</p>"
pattern = r"<.*>"
matches = re.findall(pattern, text)
print(matches)
