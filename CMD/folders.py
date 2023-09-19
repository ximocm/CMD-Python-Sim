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

class File:
    def __init__(self, filename, parent):
        self.filename = filename
        self.parent = parent
        self.text = None
    def text(self):
        return self.text
    def change_name(self, newname):
        self.filename=newname
    def get_name(self):
        return self.filename
    def get_parent(self):
        return self.parent
    def get_path(self):
        return self.parent.path + '/' + self.filename
    def write(self, text):
        self.text = text
    def read(self):
        return self.text
    def rm(self):
        self.parent.rm(self.filename)
    def append(self, text):
        self.text += text
    
class Folder:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.files = []
        self.folders = []
        if parent == None:
            self.path = name
        else:
            self.path = parent.get_path() + '/' + name
    def change_name(self, newname):
        self.name=newname
    def get_name(self):
        return self.name
    def get_parent(self):
        return self.parent
    def get_path(self):
        return self.path
    
    def go_to_parent(self):
        if self.parent == None:
            print('You are already in the root folder')
            return self
        else:
            return self.parent
        
    def change_path(self, newpath):
        self.path = newpath + '/' + self.name
    
    def add_file(self, file):
        self.files.append(file)

    def add_folder(self, folder):
        self.folders.append(folder)

    def touch(self, filename):
        file = File(filename, self)
        self.files.append(file)
        return file
    
    def mkdir(self, dirname):
        folder = Folder(dirname, self)
        self.folders.append(folder)
        return folder
    
    def ls(self):
        for file in self.files:
            print(file.get_name())
        for folder in self.folders:
            print(folder.get_name())

    def cd(self, dirname):
        if dirname == '..':
            if self.parent == None:
                print('You are already in the root folder')
                return self
            else:
                return self.parent
        if dirname == '.': return self
        for folder in self.folders:
            if folder.name == dirname:
                return folder
        print('No file or directory in this folder')
        return self
    
    def rm(self, filename):
        for file in self.files:
            if file.filename == filename:
                self.files.remove(file)
                return
        for folder in self.folders:
            if folder.name == filename:
                self.folders.remove(folder)
                return
        print('No such file in this folder')
    
    def mv(self, filename, destination):
        for file in self.files:
            if file.get_name() == filename:
                destination.add_file(file)
                file.change_path(destination.get_path())
                self.files.remove(file)
                return
        for folder in self.folders:
            if folder.name == filename:
                destination.add_folder(folder)
                folder.change_path(destination.get_path())
                self.folders.remove(folder)
                return
        print('No such file in this folder')

    def get_file(self, filename):
        for file in self.files:
            if file.get_name() == filename:
                return file
        print('No such file in this folder')
        return None
    
    def cp(self, filename, destination):
        for file in self.files:
            if file.get_name() == filename:
                destination.add_file(file)
                return
        for folder in self.folders:
            if folder.name == filename:
                destination.add_folder(folder)
                return
        print('No such file in this folder')
    
    def check_folder(self, name):
        target = check_folder_recursive(self, name)
        return target

def check_folder_recursive(folder, name):
    if folder.get_name() == name:
        return folder
    else:
        for subfolder in folder.folders:
            result = check_folder_recursive(subfolder, name)
            if result:
                return result
        return None