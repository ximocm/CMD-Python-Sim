from functs import cls, Load, bcolors, login, SUDOPASS, USERPASS, pack, help
from folders import Folder, File
from programs import aptget, cypher
import getpass
import pickle

class history:
    def __init__(self):
        self.history = []
    def add(self, command):
        self.history.append(command)
    def print(self):
        for i in self.history:
            print(*i)


hist = history()
cache = pack()
root = Folder('root', None)

#load
while True:
    inp = input("Do you want to load the last session? (y/n): ")
    if inp == 'y':
        root = pickle.load(open("root.p", "rb"))
        cache = pickle.load(open("cache.p", "rb"))
        break
    elif inp == 'n':
        root.mkdir('home')
        root.touch('README.txt')
        root.folders[0].touch('test.txt')
        root.folders[0].mkdir('user1')
        root.folders[0].folders[0].touch('passwd.txt')
        root.folders[0].folders[0].files[0].write('root: nvhp')
        break
    else:
        print(bcolors.WARNING + "Invalid input" + bcolors.ENDC)


#DosEmulator
current_folder = root
cls()
print(bcolors.OKGREEN + "---------Welcome to FaOS---------" + bcolors.ENDC)
print(bcolors.OKGREEN + "-----------Version 1.1-----------" + bcolors.ENDC)
print("---------------------------------")


#user selection
user, passw, sudo = login()
#user = "user1"

Load()
#command line
while True:
    instruction = input(user + ":" + bcolors.OKBLUE + current_folder.get_path() +bcolors.ENDC+ "-𝄢 ").split(" ")
    hist.add(instruction)
    if instruction[0] == 'exit':
        pickle.dump(cache, open("cache.p", "wb"))
        pickle.dump(root, open("root.p", "wb"))
        print ("Exiting...")
        break
    elif instruction[0] == '':
        pass
    elif instruction[0] == 'help':
        help()
    elif instruction[0] == 'history':
        hist.print()
    elif instruction[0] == 'clear':
        cls()
    elif instruction[0] == 'sudo':
        if len(instruction) < 2:
            if sudo:
                print(bcolors.OKGREEN + "You are root" + bcolors.ENDC)
            else:
                print(bcolors.FAIL + "You are not root" + bcolors.ENDC)
                passw2 = getpass.getpass("Enter sudo password: ")
                if passw2 == SUDOPASS:
                    print(bcolors.OKGREEN + "You are now root" + bcolors.ENDC)
                    sudo = True
                    user = "root"
                else:
                    print(bcolors.FAIL + "Wrong password!" + bcolors.ENDC)
    elif instruction [0] == 'apt-get':
        if not sudo:
            print (bcolors.FAIL + "You are not root" + bcolors.ENDC)
        else:
            if instruction[1] == 'install':
                if len(instruction) < 2:
                    print(bcolors.WARNING + 'apt-get: missing operand' + bcolors.ENDC)
                else:
                    aptget.install(instruction[2],cache)
            elif instruction[1] == 'remove':
                if len(instruction) < 2:
                    print(bcolors.WARNING + 'apt-get: missing operand' + bcolors.ENDC)
                else:
                    aptget.remove(instruction[2],cache)
            elif instruction[1] == 'list':
                aptget.list(cache)
            else:
                print(bcolors.WARNING + 'apt-get: unknown command' + bcolors.ENDC)
    elif instruction[0] == 'ls':
        if len(instruction) > 1:
            print (bcolors.WARNING + 'ls: too many arguments' + bcolors.ENDC)
        else:
            current_folder.ls()
    elif instruction[0] == 'cd':
        if len(instruction) < 2:
            print(bcolors.WARNING + 'cd: missing operand' + bcolors.ENDC)
        else:
            folder_name = instruction[1].split("/")
            for i in folder_name:
                current_folder = current_folder.cd(i)
    elif instruction[0] == 'mkdir':
        if len(instruction) < 2:
            print(bcolors.WARNING + 'mkdir: missing operand' + bcolors.ENDC)
        else:
            folder_name = instruction[1].split("/")
            obj = folder_name.pop()
            origin = current_folder
            for i in folder_name:
                current_folder = current_folder.cd(i)
            current_folder.mkdir(obj)
            #go back to origin folder
            while(current_folder != origin):
                current_folder = current_folder.go_to_parent()

    elif instruction[0] == 'rm':
        if len(instruction) < 2:
            print(bcolors.WARNING + 'rm: missing operand' + bcolors.ENDC)
        else:
            folder_name = instruction[1].split("/")
            obj = folder_name.pop()
            origin = current_folder
            for i in folder_name:
                current_folder = current_folder.cd(i)
            current_folder.rm(obj)
            #go back to origin folder
            while(current_folder != origin):
                current_folder = current_folder.go_to_parent()

    elif instruction[0] == 'touch':
        if len(instruction) < 2:
            print(bcolors.WARNING + 'touch: missing operand' + bcolors.ENDC)
        else:
            folder_name = instruction[1].split("/")
            obj = folder_name.pop()
            origin = current_folder
            for i in folder_name:
                current_folder = current_folder.cd(i)
            current_folder.touch(obj)
            #go back to origin folder
            while(current_folder != origin):
                current_folder = current_folder.go_to_parent()

    elif instruction[0] == 'cat':
        if len(instruction) < 2:
            print(bcolors.WARNING + 'cat: missing operand' + bcolors.ENDC)
        else:
            file_name = instruction[1]
            file = current_folder.get_file(file_name)
            print(file.read())

    elif instruction[0] == 'mv':
        if len(instruction) < 3:
            print(bcolors.WARNING + 'mv: missing operand' + bcolors.ENDC)
        else:
            #check all folders from root
            target_folder = root.check_folder(instruction[2])
            if target_folder == None:
                print(bcolors.WARNING + 'mv: target folder not found' + bcolors.ENDC)
            else:
                current_folder.mv(instruction[1], target_folder)

    elif instruction[0] == 'path':
        print(current_folder.get_path())

    elif instruction[0] == 'cp':
        if len(instruction) < 3:
            print(bcolors.WARNING + 'cp: missing operand' + bcolors.ENDC)
        else:
            #check all folders from root
            target_folder = root.check_folder(instruction[2])
            if target_folder == None:
                print(bcolors.WARNING + 'cp: target folder not found' + bcolors.ENDC)
            else:
                current_folder.cp(instruction[1], target_folder)

    elif instruction[0] == 'echo':
        if instruction[1] == '>':
            filename = instruction[2]
            text = instruction[3]
            file = current_folder.get_file(filename)
            if file == None:
                print('New file created')
                file = current_folder.touch(filename)
            file.write(text)
        elif instruction[1] == '>>':
            filename = instruction[2]
            text = instruction[3]
            file = current_folder.get_file(filename)
            if file == None:
                print('New file created')
                file = current_folder.touch(filename)
            file.append(text)
        else:
            print(instruction[1])

    elif instruction[0] == 'cypher':
        if cache.isinstalled('cypher'):
            if len(instruction) < 4:
                print(bcolors.WARNING + 'cypher: missing operand' + bcolors.ENDC)
            else:
                if instruction[1] == '-c':
                    if instruction[2] == 'encode':
                        final = cypher.caesar_encode(instruction[3], int(instruction[4]))
                        if len(instruction) > 5:
                            if instruction[5] == '>':
                                current_folder.touch(instruction[6])
                                file = current_folder.get_file(instruction[6])
                                file.write(final)
                        else:
                            print(final)
                        
                    elif instruction[2] == 'decode':
                        final = cypher.caesar_decode(instruction[3], int(instruction[4]))
                        if len(instruction) > 5:
                            if instruction[5] == '>':
                                current_folder.touch(instruction[6])
                                file = current_folder.get_file(instruction[6])
                                file.write(final)
                        else:
                            print(final)
        else:
            print(bcolors.WARNING + 'cypher: command not found' + bcolors.ENDC)
            print(bcolors.WARNING + 'Install cypher with apt-get install cypher' + bcolors.ENDC)

    else:
        print(bcolors.WARNING + 'Command not found' + bcolors.ENDC)
    
    