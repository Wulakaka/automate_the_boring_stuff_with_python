#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
#        py.exe mcb.pyw delete <keyword> - Deletes the keyword from the shelf.
#        py.exe mcb.pyw delete - Deletes all keywords from the shelf.


import shelve, pyperclip, sys

# print(sys.argv)
mcbShelf = shelve.open('mcb')
# print(list(mcbShelf.items()))

# Save clipboard content.
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'delete':
        for key in list(mcbShelf.keys()):
            del mcbShelf[key]
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

print(list(mcbShelf.keys()))
mcbShelf.close()

print(pyperclip.paste())