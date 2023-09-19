from functs import bcolors, pack

#valid packages
valid_packages=[
    "cypher"
]


class aptget:
    def install(package,cache):
        if package in cache.get_packages():
            print(bcolors.OKGREEN + "Package " + package + " is already installed" + bcolors.ENDC)
        else:
            print(bcolors.OKGREEN + "Installing " + package + bcolors.ENDC)
            cache.add(package)
    def remove(package, cache):
        if package in cache.get_packages():
            print(bcolors.OKGREEN + "Removing " + package + bcolors.ENDC)
            cache.remove(package)
        else:
            print(bcolors.OKGREEN + "Package " + package + " is not installed" + bcolors.ENDC)
    def list(cache):
        cache.lista()

class cypher:
    def caesar_encode(string, key):
        result = ""
        for i in string:
            result += chr(ord(i) + key)
        return result
    def caesar_decode(string, key):
        result = ""
        for i in string:
            result += chr(ord(i) - key)
        return result
    