import os
import webbrowser
import subprocess
from colorama import Fore

commands = {
    'help' : 'Get List Of All Commands',
    'exit' : 'Exit the terminal',
    'echo' : 'Print a string from the terminal',
    'mkdir' : 'Make a directory/folder',
    'rmdir' : 'Remove a directory',
    'ls' : 'Get the list of all files and folders in current directory',
    'browser' : 'Open your default browser',
    'code' : 'Open visual studio code in current directory'
}

print(Fore.CYAN + """

██╗░░██╗████████╗███████╗██████╗░███╗░░░███╗██╗███╗░░██╗░█████╗░██╗░░░░░
╚██╗██╔╝╚══██╔══╝██╔════╝██╔══██╗████╗░████║██║████╗░██║██╔══██╗██║░░░░░
░╚███╔╝░░░░██║░░░█████╗░░██████╔╝██╔████╔██║██║██╔██╗██║███████║██║░░░░░
░██╔██╗░░░░██║░░░██╔══╝░░██╔══██╗██║╚██╔╝██║██║██║╚████║██╔══██║██║░░░░░
██╔╝╚██╗░░░██║░░░███████╗██║░░██║██║░╚═╝░██║██║██║░╚███║██║░░██║███████╗
╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝
""")


print(Fore.GREEN+"[+] Welcome To XTerminal\nType 'help' To Get Started\n")


exit_terminal = False
current_directory = os.getcwd()

while exit_terminal==False:

    user_input = input(Fore.RED + f"{current_directory}>")

    if user_input=="help":
        print(Fore.MAGENTA + f"[+] {commands}\n")

    elif user_input=="exit":
        exit_terminal = True

    elif user_input=="echo":
        user_input = input(Fore.GREEN + "[+] Enter the string:\n")
        print(Fore.BLUE + f"[+] {user_input}\n")

    elif user_input=="mkdir":
        user_input = input(Fore.GREEN + "[+] Enter the name of the folder:\n")
        os.mkdir(user_input)
        print(Fore.BLUE + "[+] Folder created successfully\n")

    elif user_input=="rmdir":
        user_input = input(Fore.GREEN + "[+] Enter the name of the folder:\n")
        os.rmdir(user_input)
        print(Fore.BLUE + "[+] Folder removed successfully\n")

    elif user_input=="browser":
        print(Fore.LIGHTYELLOW_EX + "[+] Opening Browser...")
        webbrowser.open("https://www.google.com")
        print(Fore.BLUE + "[+] Browser opened successfully\n")

    elif user_input=="ls":
        print(Fore.GREEN + f"[+] {print(os.listdir())}\n")

    elif user_input=="code":
        print(Fore.BLUE + f"[+] Opening Visual Studio Code\n")
        subprocess.run("code .",shell=True)

exit()