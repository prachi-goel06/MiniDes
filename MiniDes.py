# Mini Des algorith with mode of operation cbc
# python version 3.3.0
# referances
# http://stackoverflow.com/
# https://www.cs.uri.edu/cryptography/dessimplified.htm
# skeleton ModesOfOperation.py
# coded by student Name: Prachi Goel
# student ID: 1001234789
#!/usr/bin/env python

import subprocess
import EncryptionMiniDes
import DecryptionMiniDes
import os
import sys

def hangon():
    YN=input("Do you want to continue Y/N: ")
    if YN=='Y' or YN=='y':
        option()
    elif YN=='N' or YN=='n':
        sys.exit()
    else:
        print("Invalid command")

def option():
    Option= input("Please choose between Encryption/Decrypyion \n\n\n Enter E for Encryption or D for Decyption: ")
    if Option=='E':
        EncryptionMiniDes.Encryption()
        hangon()
    elif Option=='D':
        DecryptionMiniDes.Decryption()
        hangon()
    else:
        print("User entered invalid input")

if __name__ == '__main__':
    print("        'Mini DES Ecryption with CTR'      ")
    print(' Coded by: \n student Name: Prachi Goel \n student ID: 1001234789')
    option()
    
