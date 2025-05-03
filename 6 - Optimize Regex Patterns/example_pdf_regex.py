import re

text = "document.pdf"
if re.search(r"\.pdf$", text):
    print("It’s a PDF.")
