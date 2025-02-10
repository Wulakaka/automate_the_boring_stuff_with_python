print('input eggs:')
eggs = input()
print('input bacon:')
bacon = input()

assert eggs.lower() != bacon.lower(), 'The eggs and bacon are the same.'