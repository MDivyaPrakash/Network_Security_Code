#!/usr/bin/env python3
#This code implements the encryption based on the Fibonacci Series

def fibonacci_function(n):
   if n == 0:
       return 0
   elif n == 1:
       return 1
   else:
       n1 = 0
       n2 = 1
       i = 2
       while ( i <= n ):
           n3 = n1 + n2
           n1 = n2
           n2 = n3
           i = i +1
       return n3

def encrypt_function(inp_txt,inp_key):
    print("hello1")
    lnth = len(inp_txt)
    i = 0
    j = 0
    enc_txt = ''
    inp_txt = inp_txt.upper()
    while ((i < lnth)):
        print(inp_txt[i])
        if (inp_txt[i] != ' '):
            shift_key = fibonacci_function(inp_key+j)%26
            org_posn = ord(inp_txt[i])
            if org_posn + shift_key > 90:
                enc_txt = enc_txt + chr(shift_key + org_posn - 26)
            else:
                enc_txt = enc_txt + chr(shift_key + org_posn)
            i = i + 1
            j = j + 1
        else:
            enc_txt = enc_txt + ' '
            j = 0
            i = i + 1
    return enc_txt

def decrypt_function(inp_txt,inp_key):
    print("hello2")
    lnth = len(inp_txt)
    i = 0
    j = 0
    dec_txt = ''
    inp_txt = inp_txt.upper()
    while ((i < lnth)):
        print(inp_txt[i])
        if (inp_txt[i] != ' '):
            shift_key = fibonacci_function(inp_key + j) % 26
            org_posn = ord(inp_txt[i])
            if org_posn - shift_key < 65:
                dec_txt = dec_txt + chr(org_posn + 26 - shift_key)
            else:
                dec_txt = dec_txt + chr(org_posn - shift_key)
            i = i + 1
            j = j + 1
        else:
            dec_txt = dec_txt + ' '
            j = 0
            i = i + 1
    return dec_txt

print("========CONTINUOS FIBONACCI ENCRYPTION ALGORITHM==========")
print("Type 1 for Encryption")
print("Type 2 for Decryption")
val = input("Please enter the value: ")
print((ord('A')))
print(ord('Z'))
if val == '1':
    txt = input("Enter the value for text to encrypted :")
    print(txt)
    inpt_key =  input("Enter the value for secret key :")
    cipher_text = encrypt_function(txt,int(inpt_key))
    print('The encrypted text according to key provided is : {}'.format(cipher_text))
    #shift_function
elif val == '2':
    txt = input("Enter the value for text to decrypted :")
    print(txt)
    inpt_key =  input("Enter the value for secret key :")
    decrypted_text = decrypt_function(txt,int(inpt_key))
    print('The decrypted text according to key provided is : {}'.format(decrypted_text))
else:
    print("Input provided by the user is not valid")

print("Thanks for using the program")