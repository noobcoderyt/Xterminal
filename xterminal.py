import os
import webbrowser
import subprocess
from colorama import Fore

print(Fore.CYAN + """

██╗░░██╗████████╗███████╗██████╗░███╗░░░███╗██╗███╗░░██╗░█████╗░██╗░░░░░
╚██╗██╔╝╚══██╔══╝██╔════╝██╔══██╗████╗░████║██║████╗░██║██╔══██╗██║░░░░░
░╚███╔╝░░░░██║░░░█████╗░░██████╔╝██╔████╔██║██║██╔██╗██║███████║██║░░░░░
░██╔██╗░░░░██║░░░██╔══╝░░██╔══██╗██║╚██╔╝██║██║██║╚████║██╔══██║██║░░░░░
██╔╝╚██╗░░░██║░░░███████╗██║░░██║██║░╚═╝░██║██║██║░╚███║██║░░██║███████╗
╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝
""")


print(Fore.GREEN+"[+] Welcome To XTerminal\n")


exit_terminal = False
current_directory = os.getcwd()

while exit_terminal==False:

    user_input = input(Fore.RED + f"{current_directory}>")

    subprocess.run(user_input, shell=True)

    if user_input.startswith("cd "):
        directory = user_input[3:]
        try:
            os.chdir(directory)
            current_directory = os.getcwd()
        except FileNotFoundError:
            print(f"Directory not found: {directory}")

    elif user_input.lower() == "exit":
        break
    else:
        try:
            os.system(user_input)
        except Exception as e:
            print(f"Error: {e}")

exit()