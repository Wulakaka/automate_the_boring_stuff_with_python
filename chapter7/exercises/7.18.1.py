import re

# passwordRegex = re.compile(r'^[a-zA-Z0-9]{8,}$')
# (?=.*[a-z])
# (?=...)：正向前瞻断言，表示在当前位置后面的内容必须匹配括号内的模式，但不消耗字符。
# .*：匹配任意字符（除换行符外）任意次。
# [a-z]：匹配一个小写字母。
passwordRegex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$')

while True:
    print('Input your password:')
    text = input()
    result = passwordRegex.match(text)
    if result is None:
        print('invalid')
    else:
        print('valid')
