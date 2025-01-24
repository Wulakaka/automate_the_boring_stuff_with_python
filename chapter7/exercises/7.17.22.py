import re
regex = re.compile(r'^(Alice|Bob|Carol) (eats|pets|throws) (apples|cats|baseballs)\.$', re.I)

print(regex.match('Alice eats apples.') is not None)
print(regex.match('Bob pets cats.') is not None)
print(regex.match('Carol throws Apples.') is not None)
print(regex.match('BOB EATS CATS.') is not None)
print(regex.match('RoboCop eats apples.') is None)
print(regex.match('ALICE THROWS FOOTBALLS.') is None)
print(regex.match('Carol eats 7 cats.') is None)
