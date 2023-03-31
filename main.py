# import random
import string
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = ['-', 'K', '<', 'n', '&', 'y', 'Q', 'l', '=', 'J', 'C', ']', 'g', 'b', '>', '8', '$', 'N', '5', 'F', '+', '{', 'q', 'A', ' ', '~', 'Y', '`', 't', 'T', '|', 'j', '!', '%', '9', 'w', 'G', 'O', '/', '.', 'W', 'c', 'I', '2', 'f', 'p', 'u', 'S', 'z', 'H', ':', 'r', '0', 'R', '\\', 'x', ';', '7', 'o', '_', 'X', 'D', 'M', 'k', '?', '*', '@', '#', 'Z', 'i', 'E', '4', 'P', '[', 'a', '(', '"', 'B', "'", 'h', 'm', '3', 's', 'v', 'L', 'U', ')', 'V', 'e', '^', '}', '1', 'd', ',', '6'] 
runningEnc = True
runningDec = True
# print(f'Chars = {chars}')
# print(f'Key   = {key}')

# Encryption
while runningEnc:
    print(f'---------------------{Fore.LIGHTGREEN_EX}Encryption{Fore.RESET}---------------------')
    plain_text = input('Enter a message to encrypt: ')
    cipher_text = ''

    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += key[index]

    print(f'{Fore.YELLOW}Original message: {plain_text} {Fore.RESET}')
    print(f'{Fore.LIGHTGREEN_EX}Encrypted message: {cipher_text} {Fore.RESET}')

    if not input(f"Want to continue \"Encryption\"? (y/n) ").lower() == "y":
        runningEnc = False

while runningDec:                                                                                                
    # Decrypt
    print(f'---------------------{Fore.YELLOW}Decryption{Fore.RESET}---------------------')                     
    cipher_text = input('Enter a message to decrypt: ')
    plain_text = ''

    for letter in cipher_text:
        index = key.index(letter)
        plain_text += chars[index]

    print(f'{Fore.LIGHTGREEN_EX}Encrypted message: {cipher_text}{Fore.RESET}')
    print(f'{Fore.YELLOW}Original message: {plain_text}{Fore.RESET}')
    if not input(f"Want to continue \"Decryption\"? (y/n) ").lower() == "y":
        runningDec = False
