import time
import os
import getpass
from folders import Folder, File
from playsound import playsound

SUDOPASS = "ksem"
USERPASS = "1234"

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class pack:
    def __init__(self):
        self.packages = []
    def add(self, package):
        self.packages.append(package)
    def remove(self, package):
        self.packages.remove(package)
    def lista(self):
        for i in self.packages:
            print(bcolors.OKGREEN + i + bcolors.ENDC)
    def get_packages(self):
        return self.packages
    def isinstalled(self, package):
        if package in self.packages:
            return True
        else:
            return False


def cls():
    os.system('cls')

def Load():
    sleep = 0.2
    cls()
    time.sleep(sleep)
    print("Loading.")
    time.sleep(sleep)
    cls()
    print("Loading..")
    time.sleep(sleep)
    cls()
    print("Loading...")
    time.sleep(sleep)
    cls()
    print("Loading.")
    time.sleep(sleep)
    cls()
    print("Loading..")
    time.sleep(sleep)
    cls()
    print("Loading...")
    time.sleep(sleep)
    cls()
    print("Loading complete")
    time.sleep(sleep * 5)
    cls()

def login():
    playsound('Sounds/login.wav')
    user = input("Enter your username: ")
    passw = getpass.getpass("Enter your password: ")
    if user == "user1" and passw == USERPASS:
        print(bcolors.OKGREEN + "Welcome user1" + bcolors.ENDC)
        sudo = False
    elif user == "root" and passw == SUDOPASS:
        print(bcolors.OKGREEN + "Welcome root" + bcolors.ENDC)
        sudo = True
    else:
        print(bcolors.FAIL + "Wrong username or password!" + bcolors.ENDC)
        exit()
    time.sleep(1.5)
    return user, passw, sudo

def help():
    print("help - shows this message, ? - optional argument")
    print("exit - exits the program")
    print("clear - clears the screen")
    print("history - shows the history of commands")
    print("sudo - gives you root access")
    print("apt-get[operand][package] - installs packages")
    print("     operand - list, install, remove")
    print("     package - the name of the package")
    print("cypher[type][en/decode][msg][n][operand]?[folder]? - encrypts and decrypts text")
    print("ls - lists the files and folders in the current directory")
    print("cd[path] - changes the current directory")
    print("mkdir[name] - creates a new folder")
    print("touch[name] - creates a new file")
    print("rm[name] - removes a file or folder")
    print("cat[name] - shows the contents of a file")
    print("echo[operand]?[filename]?[msg] - writes text to a file")
    print("rm[name] - removes a file or folder")
        