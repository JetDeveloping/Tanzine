#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
from colorama import Fore

def incorrect_first(text):
    print(Fore.RED + '\nERROR: No Definitive Statement')
    print(Fore.BLUE + 'Message: This error may have been caused by using an incorrect first character!')
    print(Fore.YELLOW + str(text))
    print(Fore.GREEN + '^^^')

    print(Fore.RESET)

    exit()

def incorrect_value(text, _type, was, obj):
    print(Fore.RED + f'\nERROR: Incorrect Value: {str(obj)} should have been {_type}, but was {was}')
    print(Fore.BLUE + 'Message: This error may have been caused by an incorrect definitive')
    print(Fore.YELLOW + str(text))
    print(Fore.GREEN + '^'*len(text))

    print(Fore.RESET)
    exit()


def incorrect_import(text, module):
    print(Fore.RED + f'\nError: Incorrect Value, No MODULE named {module}.')
    print(Fore.BLUE + 'Message: This error may have been caused by an incorrect module in a @FUNC@ argument')
    print(Fore.YELLOW + text)
    print(Fore.GREEN + '^'*len(text))
    
    print(Fore.RESET)
    exit()

def incorrect_args(text, function):
    print(Fore.RED + '\nIncorrect Function Arguments')
    print(Fore.YELLOW + text)
    print(Fore.GREEN + '^'*len(text))

    print(Fore.RESET)
    exit()

def syntax_error(text):
    print(Fore.RED + '\nError: Incorrect Syntax')
    print(Fore.BLUE + 'Message: This may have been caused by an incorrect definitive')
    print(Fore.YELLOW + text)
    print(Fore.GREEN + '^'*len(text))

    print(Fore.RESET)
    exit()

def function_error(text):
    print(Fore.RED + '\nError: Incorrect Function')
    print(Fore.BLUE + 'Message: This may have been caused by no "/"')
    print(Fore.YELLOW + text)
    print(Fore.GREEN + '^'*len(text))

    print(Fore.RESET)
    exit()

def eof_error(text, current):
    print(Fore.RED + '\nError: Unexpected EOF during parsing with text' + current)
    print(Fore.BLUE + f'Message: This error may have been caused by a missing {current[0]} at the end of {current}')    
    print(Fore.YELLOW + text)
    print(Fore.GREEN + '^'*len(text))
    print(Fore.RESET)

    exit()

def incorrect_filename(text, filename):
    print(Fore.RED + '\nError: Could not open ' + Fore.BLUE +  filename + Fore.RED + '.')
    print(Fore.BLUE + 'Message: This error may have been caused by an incorrect filename')
    print(Fore.YELLOW + text)
    print(Fore.GREEN + '^'*len(text))

    print(Fore.RESET)