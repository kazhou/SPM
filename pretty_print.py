from colorama import init, Fore, Back, Style
init(convert=True)

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

def pprint_magenta(text):
    print(Fore.MAGENTA+text)
    print(Style.RESET_ALL)
