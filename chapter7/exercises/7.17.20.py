import re
regex = re.compile(r'^\d{1,3}(,\d{3})*$')

print(regex.match('42') is not None)
print(regex.match('1,234') is not None)
print(regex.match('9,368,745') is not None)
print(regex.match('12,34,5') is None)
print(regex.match('1234') is None)
