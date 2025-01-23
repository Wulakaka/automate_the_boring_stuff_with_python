spam = ['apples','bananas','tofu','cats']

def main(list):
    text = ''
    length = len(list)
    for i in range(length):
        if not i:
            text += list[i]
        elif i == length - 1:
            text += ' and'+ ' ' +  list[i]
        else:
            text += ', ' + list[i]

    return text

print(main(spam))

print(main([]))

print(main(['apples']))
