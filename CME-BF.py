########################################################################
#                                                                      #
#   A Windows password bruter using CrackMapExec by ThoughtfulDev      #
#   Using https://github.com/byt3bl33d3r/CrackMapExec by byt3bl33d3r   #
#                                                                      #
########################################################################

import os
import subprocess


def banner():
    "Gives the beautiful Banner <3"
    print("   _____                _    __  __             ______                 ____             _            ")
    print("  / ____|              | |  |  \/  |           |  ____|               |  _ \           | |           ")
    print(" | |     _ __ __ _  ___| | _| \  / | __ _ _ __ | |__  __  _____  ___  | |_) |_ __ _   _| |_ ___ _ __ ")
    print(" | |    | '__/ _` |/ __| |/ | |\/| |/ _` | '_ \|  __| \ \/ / _ \/ __| |  _ <| '__| | | | __/ _ | '__|")
    print(" | |____| | | (_| | (__|   <| |  | | (_| | |_) | |____ >  |  __| (__  | |_) | |  | |_| | ||  __| |   ")
    print("  \_____|_|  \__,_|\___|_|\_|_|  |_|\__,_| .__/|______/_/\_\___|\___| |____/|_|   \__,_|\__\___|_|   ")
    print("                                         | |                                  ")
    print("                                         | |                                  ")
    print("")
    print(" ########################################################################")
    print(" #                                                                      #")
    print(" #   A Windows password bruter using CrackMapExec by ThoughtfulDev      #")
    print(" #   Using https://github.com/byt3bl33d3r/CrackMapExec by byt3bl33d3r   #")
    print(" #                                                                      #")
    print(" ########################################################################")
    grab_version = "1.0"
    strversion = """        		  """ + bcolors.BLUE + \
        """You are using Version: %s""" % (grab_version) + bcolors.ENDC + "\n"
    print(strversion)


def cls():
    os.system('clear')

class bcolors:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERL = '\033[4m'
    ENDC = '\033[0m'
    backBlack = '\033[40m'
    backRed = '\033[41m'
    backGreen = '\033[42m'
    backYellow = '\033[43m'
    backBlue = '\033[44m'
    backMagenta = '\033[45m'
    backCyan = '\033[46m'
    backWhite = '\033[47m'

# main status calls for print functions
def print_status(message):
    print((bcolors.GREEN) + (bcolors.BOLD) + \
        ("[*] ") + (bcolors.ENDC) + (str(message)))

def print_status_indent(message):
    print((bcolors.GREEN) + (bcolors.BOLD) + \
        ("  [*] ") + (bcolors.ENDC) + (str(message)))

def print_info(message):
    print((bcolors.BLUE) + (bcolors.BOLD) + \
        ("[-] ") + (bcolors.ENDC) + (str(message)))


def print_info_indent(message):
    print((bcolors.BLUE) + (bcolors.BOLD) + \
        ("  [-] ") + (bcolors.ENDC) + (str(message)))


def print_warning(message):
    print((bcolors.YELLOW) + (bcolors.BOLD) + \
        ("[!] ") + (bcolors.ENDC) + (str(message)))

def print_warning_indent(message):
    print((bcolors.YELLOW) + (bcolors.BOLD) + \
        ("  [!] ") + (bcolors.ENDC) + (str(message)))

def print_error(message):
    print((bcolors.RED) + (bcolors.BOLD) + \
        ("[!] ") + (bcolors.ENDC) + (bcolors.RED) + \
        (str(message)) + (bcolors.ENDC))

#end apperenace


def dependencycheck():
    "Checks whether all dependencies where met"

    print_info("Checking dependencies...")
    crackmapexec_inst = os.path.exists("/usr/local/bin/crackmapexec")

    if crackmapexec_inst:
        print_status_indent("CrackMapExec is installed")
        print_info_indent("Moving on...")
    else:
        print_warning("CrackMapExec could not be found in /usr/local/bin/crackmapexec")
        print_info_indent("Installing it now...")
        cmd_install = "sudo pip install crackmapexec"
        subprocess.Popen(cmd_install, stdout=subprocess.PIPE, shell=True)
        dependencycheck()
    return

def main():
    cls()
    banner()
    dependencycheck()
    return


if __name__ == "__main__":
    main()