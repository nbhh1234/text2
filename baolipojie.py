#_*_ coding:utf8-
import crypt

def testPass(cryptPass):
    salt = cryptPass[0:2]
    dictFile = open('')
    fro word in dictFile.readlines():
             word = word.strip('\n')   # delete '\n'
        cryptWord = crypt.crypt(word,salt)
        if cryptWord == cryptPass:
            print "[+] Found Password:" +word
        else:
            print "[-] Password {} Not Found.".format(word)

def main():
    passFile = open('../../data/passwords.txt')
    for line in passFile.readlines():
        if ':' in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print "[*] Cracking Password For:" + user
            testPass(cryptPass)


if __name__ == "__main__":
    main()
