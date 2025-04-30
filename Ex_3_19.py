import re

def extract_username(email):
  username = re.search(r'([^@]+)@', email)
  if username:
    return username.group(1)
  else:
    return None

email_address = "alice@company.com"
username = extract_username(email_address)
print(username)