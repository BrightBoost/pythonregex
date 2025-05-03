import re

pattern = r"\b\w+@\w+\.\w+\b"
compiled = re.compile(pattern, re.DEBUG)
