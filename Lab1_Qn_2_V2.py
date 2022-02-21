#!/usr/bin/env python3
# This code uses the brute force method to retrieve the key of the Caesar's cipher
# This code goes through all possible shift combinations .
# The key shift with which both the cipher texts matched, is returned at end.

txt = 'SECURITY IS IMPORTANT'
ciph_txt = 'FRPHEVGL VF VZCBEGNAG'


def caesar_function(txt_inp,ciph_txt_inp):
        print('Orginal Text is ==> {}'.format(txt_inp))
        print('Cipher Text is  ==> {}'.format(ciph_txt_inp))
        txt_inp = txt_inp.upper()
        ciph_txt_inp = ciph_txt_inp.upper()
        enc_txt = ''
        lnth = len(txt_inp)
        i = 0
        j = 0
        while j <= 25:
            while i < lnth:
                if txt_inp[i] != ' ':
                    org_posn = ord(txt_inp[i])
                    if org_posn + j > 90:
                        enc_txt = enc_txt + chr(j + org_posn - 26)
                    else:
                        enc_txt = enc_txt + chr(j + org_posn)
                    i = i + 1
                else:
                    enc_txt = enc_txt + ' '
                    i = i + 1
            print('The encrypted text for key {} is {}'.format(j, enc_txt))
            if enc_txt == ciph_txt_inp:
                print('Cipher text match found')
                return j
                break
            else:
                j = j + 1
                i = 0
                enc_txt = ''


ans = caesar_function(txt, ciph_txt)
print("The Key is: {}".format(ans))
