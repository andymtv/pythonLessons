import re
# Email validation checker
email_pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
s = 'andy.mtv12@gmail.com'


email = email_pattern.search(s).group() if email_pattern.search(s) else 'incorrect email'
print(email)

# at least 8 characters length, lowercase and uppercase, symbols $%#@
password_pattern = re.compile(r"(^[a-zA-Z0-9$%#@]{8,}$)")

p = 'aasdas31'

password = password_pattern.search(p).group() if password_pattern.search(p) else 'incorrect password'
print(password)