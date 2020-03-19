from pip._vendor.colorama import init, Fore


def display(message, is_warning=False):
    if is_warning:
        print(Fore.BLUE + message)
    else:
        print(Fore.GREEN + message)
