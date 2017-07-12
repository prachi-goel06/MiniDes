# Mini Des algorith with mode of operation cbc
# python version 3.3.0
# referances
# http://stackoverflow.com/
# https://www.cs.uri.edu/cryptography/dessimplified.htm
# skeleton ModesOfOperation.py
# coded by student Name: Prachi Goel
# student ID: 1001234789
#!/usr/bin/env python
import sys
import datetime


class MiniDes:
    def __init__(self):
        print("        'Mini DES Ecryption'      ")
        print(' Coded by: \n student Name: Prachi Goel \n student ID: 1001234789')

    # Taking the input from the users
    def user_input(self):
    # taking user input for Student Name
        self.student_name = input("'Please enter your name, Note that name should be 10 letters longs': ")
    # check for the length: student name to be equal to 10, if less than 10 exit the program
        name_length = len(self.student_name)
        if name_length != 10:
            print("'The name entered is not 10 digits, closing the program'")
            sys.exit()
        elif self.student_name.isalpha():
            print("'Input accepted: '")
        else:
            print("'The name entered contains characters other than alphabets'")
            sys.exit()
            # check for the length: student id should be equal to 10, if less than 10 exit the program
        self.student_ID = input("'Please enter your student ID, Note that student id should have 10 digit': ")
        id_length = len(self.student_ID)
        if id_length != 10:
            print("'The student id entered is not 10 digits, closing the program'")
            sys.exit()
        elif self.student_ID.isdigit():
            print("'Input accepted'")
        else:
            print("'ID should be only digits'")
            sys.exit()
        return self.student_name, self.student_ID

    def date_of_birth(self):
        dob = input("'Please enter the date of birth in YYYY.MM.dd': ")
        date_format = '%Y.%m.%d'
        try:
            date_input = datetime.datetime.strptime(dob, date_format)
            time_tuple = date_input.timetuple()
            return (time_tuple.tm_yday)
        except ValueError:
            print('date of birth is not valid')
            sys.exit()

#Converting the input into binary
    def letters_to_binary(self, alphabets):
        # letter conversion to 6 bit
        name_binary = ""
        for i in range(0, len(alphabets)):
            name_binary += format((ord(alphabets[i]) - ord('a') + 1), '06b')
        return name_binary

    def id_to_binary(self, student_id):
        # number conversion to 6 bit
        id_binary = ""
        for i in range(0, len(student_id)):
            id_binary += format((ord(student_id[i]) - ord('0') + 27), '06b')
        return id_binary

    def dot_space_to_binary(self):
        # dot conversion to bit
        dot_binary = format(ord('.') - 9, '06b')
        # space conversion to bit
        space_binary = format(ord(' ') + 6, '06b')
        return dot_binary, space_binary


    def date_to_binary(self, Jdate):
        date_binary = ""
        date_binary = bin(Jdate)[2:].zfill(9)
        return date_binary

# Message to encrypt
    def message_to_encrypt(self, binary_name, binary_space, binary_id, binary_dot):
        message_to_encrypt = (binary_name + binary_space + binary_id + binary_dot)
        return message_to_encrypt

#Dividing the message into blocks
    def dividing_message_to_block(self, message):
        n = 12
        block = [message[i:i + n] for i in range(0, len(message), n)]
        return block

#taking the value of L0 for the block
    def encryp_step1_L0(self, blocki):
        L0 = (blocki[:6])
        print('L: ',L0)
        return L0

#taking the value of R0 for the block
    def encryp_step1_R0(self, blocks):
        R0= (blocks[6:])
        print('R: ',R0)
        return R0

#key for round 1
    def key_round1(self, binary_date):
        key1 = binary_date[0:8]
        return key1

#key for round 2
    def key_round2(self, binary_date):
        key2 = binary_date[1:9]
        return key2


#Expansion of R0
    def R0_expansion(self, R0):
        eR0 = ""
        eR0 += R0[0]
        eR0 += R0[1]
        eR0 += R0[3]
        eR0 += R0[2]
        eR0 += R0[3]
        eR0 += R0[2]
        eR0 += R0[4]
        eR0 += R0[5]
        print('E(R):',eR0)
        return (eR0)



# Xoring the key with R0
    def XOR_R0_Key(self, R0, key):
        FRK = int(R0, 2) ^ int(key, 2)
        # padding values for func
        func = format(FRK, '08b')
        print ('Result of R0 XOR KEY1: ',func)
        return func

#getting the values from S boxes
    def Checking_Sbox(self, func):
# intialising the Sbox1.
        s1_row0 = ['101', '010', '001', '110', '011', '100', '111', '000']
        s1_row1 = ['001', '011', '110', '010', '000', '111', '101', '011']

        # Getting the value from Sbox1
        S1 = func[:4]
        if S1[0] == '0':
            b = int(S1[1] + S1[2] + S1[3], 2)
            S1_value = s1_row0[b]
        else:
            b = int(S1[1] + S1[2] + S1[3], 2)
            S1_value = s1_row1[b]

# intialising the Sbox2.
        s2_row0 = ['100', '000', '110', '101', '111', '001', '011', '010']
        s2_row1 = ['101', '011', '000', '111', '110', '010', '001', '100']

        # Getting the value from Sbox2
        S2 = func[4:]
        if S2[0] == '0':
            b = int(S2[1] + S2[2] + S2[3], 2)
            S2_value = s2_row0[b]
        else:
            b = int(S2[1] + S2[2] + S2[3], 2)
            S2_value = s2_row1[b]
# computing f(R0,K1)
        Value_after_Sbox = S1_value + S2_value
        print('Value after Sbox is: ',Value_after_Sbox)
        return Value_after_Sbox

# computing (f(R0,K1) XOR L0)
    def XOR_Sbox_L_to_find_R(self, Sbox, L0):
        R_value = int(Sbox, 2) ^ int(L0, 2)
        # encrypted block as R0L0-value
        Ri = format(R_value, '06b')
        print('New value of R: ',Ri,'\n')
        return Ri

def Encryption():
    encryption = MiniDes()
    user_SName_SID = encryption.user_input()
    Jdate = (encryption.date_of_birth())
    # unpacking user_Sname_SID to get Name and ID
    user_Name = (user_SName_SID[0])
    user_ID = (user_SName_SID[1])
    # binary conversion of string,number,date,dot and space
    binary_name = encryption.letters_to_binary(user_Name)
    binary_id = encryption.id_to_binary(user_ID)
    binary_dot_space = encryption.dot_space_to_binary()
    binary_dot = binary_dot_space[0]
    binary_space = binary_dot_space[1]
    binary_date = encryption.date_to_binary(Jdate)
# Initialising the key
    key=[]
    key.append(encryption.key_round1(binary_date))
    key.append(encryption.key_round2(binary_date))

# Stream of data to be encrypted
    message = encryption.message_to_encrypt(binary_name, binary_space, binary_id, binary_dot)
    Result_Round=""
    blocks = encryption.dividing_message_to_block(message)
    print ("Message is divided into following blocks: \n", blocks)
    ciphertext=""
    Encrypted_Block=""
    for i in range(0, len(blocks)):
        print("Block is ",i+1,": '", blocks[i])
        for j in range(0, len(key)):
            #2 round encryption for each block of plaintextprint('Round ',j+1)
            print('Key for round',j+1,'is: ',key[j])
            L = encryption.encryp_step1_L0(blocks[i])
            R = encryption.encryp_step1_R0(blocks[i])
            Expanded_R = encryption.R0_expansion(R)
            Func_R_K = encryption.XOR_R0_Key(Expanded_R, key[j])
            Sbox = encryption.Checking_Sbox(Func_R_K)
            print('New value of L: ', R)
            Encrypted_message_Ri = encryption.XOR_Sbox_L_to_find_R(Sbox, L)
            Result_Round = (R + Encrypted_message_Ri)
            blocks[i]=Result_Round
        Encrypted_Block =(Encrypted_message_Ri + R)
        print("'Encryption of block ",i+1," at the end of 2 round of encryption given by RiLi: '", Encrypted_Block, '\n\n\n')
        ciphertext+=Encrypted_Block
    print('Ciphertext: ', ciphertext, '\n')


