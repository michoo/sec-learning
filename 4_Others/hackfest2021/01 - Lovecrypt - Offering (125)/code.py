#!/usr/bin/env python3

# Ph’nglui mglw’nafh Cthulhu R’lyeh wgah’nagl fhtagn.
# --  HANDS OFF IF YOU'RE NOT A CULTIST --

import argparse
import base64

def main():
        parser =  argparse.ArgumentParser()
        parser.add_argument("offering", help="Present your offering to the Old Ones, cultist!")
        args = parser.parse_args()
        offering = args.offering

        print("\nIä! Shub-Niggurath!\n")
        print("---------------------------------")
        encrypt(offering)
        print("---------------------------------")
        print("\nCthulhu fhtagn! ^(;,;)^\n")

def encrypt(payload):
        cipher = ""
        secret = "nyarlathotep"
        key = "r'lyeh" * 13
        key = key[:len(payload)]
        forbidden_chars = []
        for letter in secret:
                if letter not in forbidden_chars:
                        forbidden_chars.append(letter)
        for letter in payload:
                if letter in forbidden_chars:
                        char_code = ord(letter) - 13
                        letter = chr(char_code)
                char_code = ord(letter) << 2
                letter = chr(char_code)
                cipher += letter
        cipher = cipher[::-1]
        xored_cipher = ''.join(chr(ord(x) ^ ord(y)) for x,y in zip(cipher,key))
        print(xored_cipher.encode('utf-8'))
        cipher = (base64.b64encode(xored_cipher.encode('utf-8'))).decode('utf-8')
        print("Here's your encrypted offering :\n")
        print(cipher)


def decrypt(payload):
        message = base64.b64decode(payload)
        print("Here's your decrypted offering :\n")
        print(message)

if __name__ == "__main__":
        main()