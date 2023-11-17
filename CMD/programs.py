from functs import bcolors, pack
from sys import path
import time
import getpass
import pickle

path.insert(0, 'FAOS')

#valid packages
valid_packages=[
    "cypher"
    "mail"
]

class BankAccounts:
    def __init__(self):
        self.accounts = []
    def add(self, account):
        self.accounts.append(account)
    def remove(self, account):
        self.accounts.remove(account)
    def login(self, user, passwd):
        for i in self.accounts:
            if i.get_user() == user and i.get_passwd() == passwd:
                return True, i
        return False, None
    def save (self):
        with open("bankaccounts.pkl", "wb") as file:
            pickle.dump(self, file)
    def load(self):
        try:
            with open("bankaccounts.pkl", "rb") as file:
                bankaccounts = pickle.load(file)
            return bankaccounts
        except FileNotFoundError:
            print("No bankaccounts file found. Creating a new bankaccounts.")
            account = BankAccount("BobbyResnik", "B00byr3sn1ck", 1000)
            self.add(account)
            return BankAccounts()

class BankAccount:
    def __init__(self, user,passwd ,balance):
        self.user = user
        self.balance = balance
        self.passwd = passwd
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def get_balance(self):
        return self.balance
    def get_user(self):
        return self.user
    def get_passwd(self):
        return self.passwd

class Mail:
    def __init__(self, sender, to, subject, body):
        self.sender = sender
        self.to = to
        self.subject = subject
        self.body = body

class Mailbox:
    def __init__(self):
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)

    def load(self):
        try:
            with open("mailbox.pkl", "rb") as file:
                mailbox = pickle.load(file)
            return mailbox
        except FileNotFoundError:
            print("No mailbox file found. Creating a new mailbox.")
            m = Mail("bank@cocoon.com", "bresnick57@cocoon.com", "Welcome to Cocoon Bank!", "Welcome to Cocoon Bank! Your user is BobbyResnik. You have $1000 in your account.")
            self.add_message(m)
            return Mailbox()

    def save(self):
        with open("mailbox.pkl", "wb") as file:
            pickle.dump(self, file)

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
    def main():
        print("Welcome to FAOS Cypher!")
        print("What do you want to do?")
        print(" -Encode -Decode -Exit")
        command = input(">>> ")
        if command == "Encode" or command == "encode":
            print("What do you want to encode?")
            string = input(">>> ")
            print("What is the key?")
            key = int(input(">>> "))
            print("Encoding...")
            time.sleep(0.2)
            print("Encoded string: " + cypher.caesar_encode(string, key))
        elif command == "Decode" or command == "decode":
            print("What do you want to decode?")
            string = input(">>> ")
            print("What is the key?")
            key = int(input(">>> "))
            print("Decoding...")
            time.sleep(0.2)
            print("Decoded string: " + cypher.caesar_decode(string, key))
        elif command == "Exit" or command == "exit":
            print("Goodbye!")
            time.sleep(0.2)
        else:
            print("Invalid command")

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
    
class MailProgram:
    @staticmethod
    def main():
        print("Welcome to FAOS Mail!")
        logged_in = False
        tries = 0
        print("To access your mail, please log in.")
        user = input("User: ")
        password = input("Password: ")
        while not logged_in:
            logged_in = MailProgram.login(user, password)
            tries += 1
            if tries == 3 and not logged_in:
                print("Too many attempts.")
                time.sleep(0.2)
                break

        if logged_in:
            mailbox = Mailbox()
            while True:
                print("Welcome " + user)
                print("What do you want to do?")
                print("- Read mail - Exit")
                command = input(">>> ")

                if command.lower() == "read mail":
                    MailProgram.read_mail(mailbox)
                elif command.lower() == "exit":
                    print("Goodbye!")
                    time.sleep(0.2)
                    mailbox.save()
                    break
                else:
                    print("Invalid command")

    @staticmethod
    def read_mail(mailbox):
        if not mailbox.messages:
            print("You have no mail.")
        else:
            print("Your Messages:")
            for i, message in enumerate(mailbox.messages, 1):
                print(f"\nMessage {i}:")
                print(f"From: {message.sender}")
                print(f"To: {message.to}")
                print(f"Subject: {message.subject}")
                print(f"Body: {message.body}")

    @staticmethod
    def login(user, password):
        if user == "bresnick57@cocoon.com" and password == "B00byr3sn1ck":
            print("Logged in as Booby Resnick")
            return True
        else:
            print("Invalid user or password")
            return False

    @staticmethod
    def send_mail(user, to, subject, body, logged_in, mailbox):
        if not logged_in:
            print("You are not logged in.")
            return False
        else:
            new_mail = Mail(user, to, subject, body)
            mailbox.add_message(new_mail)
            print("Sending mail...")
            time.sleep(0.2)
            print(f"From: {user}")
            print(f"To: {to}")
            print(f"Subject: {subject}")
            print(f"Body: {body}")
            time.sleep(0.4)
            print("Mail sent!")

class BankCocoon:
    def main():
        bankacounts = BankAccounts.load()
        print("Welcome to Cocoon Bank!")
        logged_in = False
        tries = 0
        print("To access your account, please log in.")
        user = input("User: ")
        password = input("Password: ")
        while not logged_in:
            logged_in, account = bankacounts.login(user, password)
            tries += 1
            if tries == 3 and not logged_in:
                print("Too many attempts.")
                time.sleep(0.2)
                break
        if logged_in:
            while True:
                print("Welcome " + user)
                print("What do you want to do?")
                print("- Deposit - Withdraw - Check balance - Exit")
                command = input(">>> ")
                if command.lower() == "deposit":
                    BankCocoon.deposit(user, account)
                elif command.lower() == "withdraw":
                    BankCocoon.withdraw(user, account)
                elif command.lower() == "check balance":
                    BankCocoon.check_balance(user)
                elif command.lower() == "exit":
                    print("Goodbye!")
                    time.sleep(0.2)
                    bankacounts.save()
                    break
                else:
                    print("Invalid command")

    @staticmethod
    def check_balance(user):
        print("Checking balance...")
        time.sleep(0.2)
        print("Your balance is: $1000")
