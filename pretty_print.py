from colorama import init, Fore, Back, Style
init(convert=True)
# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')

def pprint_headings(text):
    print(Fore.CYAN+text)
    print(Style.RESET_ALL)

def pprint_text(text):
    print(Fore.GREEN+text)
    print(Style.RESET_ALL)

def pprint_red(text):
    print(Fore.RED+text)
    print(Style.RESET_ALL)

def pprint_blue(text):
    print(Fore.BLUE+text)
    print(Style.RESET_ALL)
