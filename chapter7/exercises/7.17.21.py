import re
regex = re.compile(r'^([A-Z][a-z]+)+ Nakamoto$')

print(regex.match('SatoShi Nakamoto') is not None)
print(regex.match('Alice Nakamoto') is not None)
print(regex.match('RoboCop Nakamoto') is not None)
print(regex.match('satoShi Nakamoto') is None)
print(regex.match('Mr. Nakamoto') is None)
print(regex.match('Nakamoto') is None)
print(regex.match('SatoShi nakamoto') is None)
