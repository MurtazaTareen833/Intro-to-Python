import re

# Example text
text = "Hello, my email address is example@example.com."

# Regular expression pattern to match an email address
pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

# Find all email addresses in the text
matches = re.findall(pattern, text)

# Print the matches
for match in matches:
    print(match)
