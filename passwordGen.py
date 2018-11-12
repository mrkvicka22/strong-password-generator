import random
import hashlib

class randomPass():
    action = ''
    def __init__(self):
        # SETUP
        self.passdic = {}

        self.num_lines = sum(1 for line in open('passwords.txt'))
        with open('passwords.txt', 'r') as rf:
            for i in range(self.num_lines):
                self.content = rf.readline()
                self.content = list(self.content.split())
                self.passdic[self.content[0]] = self.content[1]

        self.leng = 14
        self.action = ''
        self.gPass = ''
        # work as i want to
        self.myPass = ''

        print('perform one of the actions')
        while self.action != 'break':
            print('new action please')
            self.action = input()
            if self.action == 'generate':
                print('determine your generated password length, We recommend above 14 characters')
                self.leng = int(input())
                self.gPass = self.generateRandomPassWord(self.leng)
                print('generated')
            elif self.action == 'read':
                self.passRead()
            elif self.action == 'save':
                    self.savePass(self.gPass)
            else:
                print(self.action + 'is not a valid action')



    def generateRandomPassWord(self, lengthOfPassword=14):
        znaky = ['"', "'", '!', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3',
                 '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
                 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[',
                 ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']

        pword = ''.join([znaky[random.randint(0, len(znaky) - 1)] for i in range(lengthOfPassword)])
        return pword

    def savePass(self, generatedPassword):
        print('to save the generated pass word type your key password')
        self.myPass = hashlib.md5((input().encode('utf-8'))).hexdigest()
        if self.myPass in self.passdic:
            print('your key password already exists!')
        else:
            with open('passwords.txt', 'a') as af:

                af.write(self.myPass + ' ' + generatedPassword + '\n')

            self.passdic[self.myPass] = generatedPassword
            print('password stored')

    def passRead(self):
        print('to read the generated pass word type your key password')
        self.myPass = hashlib.md5((input().encode('utf-8'))).hexdigest()
        if self.myPass in self.passdic:
            print(self.passdic[self.myPass])
        else:
            print('we are sorry your password is non existant')

a = randomPass()
print('fin')


