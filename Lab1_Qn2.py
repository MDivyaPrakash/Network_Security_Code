#!/usr/bin/env python3
# Press the green button in the gutter to run the script.
# This file contains the brut-force approach to decrypt the caesar's cipher text
# The ASCII values are arranged in an order, so the below approach is exploiting the values and using it to get the shift.
# The difference of each character is derived and the mode of the whole derived difference is given as the key
# This code can take input in both UPPER and LOWER cases.
# Taking mode will give a better estimation of the key because , there are chances that some differences may not match the keys.
# An alternative solution would be frequency analysis, wherein each character's frequency is matched with the general sequence of english alphabets

txt = 'SECURITY IS IMPORTANT'
ciph_txt = 'FRPHEVGL VF VZCBEGNAG'
#Defining the function with two strings
def caesar_function(txt_inp,ciph_txt_inp):
        print('Orginal Text is ==> {}'.format(txt_inp))
        print('Cipher Text is  ==> {}'.format(ciph_txt_inp))
        txt_inp = txt_inp.upper()
        ciph_txt_inp = ciph_txt_inp.upper()
        lnth = len(txt_inp)
        i=0
        key_opt= [0]*lnth
        while ((i < lnth-1)):
            key_opt[i] = abs(ord((txt_inp[i])) - ord(ciph_txt_inp[i]))
            i=i+1
        return(max(set(key_opt), key = key_opt.count))
#Calling the function to get the value of key and printing the value.
ans = caesar_function(txt,ciph_txt)
print("The Key is: {}".format(ans))





