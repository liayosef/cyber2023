"""
Author: lia yosef
program name: rome
Description: rome and julliate
date : 26/10/2023
"""
import sys

FIRST_WORD = 1
TRANSLATING_DICTIONARY = {"A": "56", "B": "57", "C": "58", "D": "59", "E": "40", "F": "41", "G": "42", "H": "43",
                          "I": "44", "J": "45", "K": "46", "L": "47", "M": "48", "N": "49", "O": "60", "P": "61",
                          "Q": "62", "R": "63",
                          "S": "64", "T": "65", "U": "66", "V": "67", "W": "68", "X": "69", "Y": "10", "Z": "11",
                          "a": "12", "b": "13",
                          "c": "14", "d": "15", "e": "16", "f": "17", "g": "18", "h": "19", "i": "30", "j": "31",
                          "k": "32", "l": "33",
                          "m": "34", "n": "35", "o": "36", "p": "37", "q": "38", "r": "39", "s": "90", "t": "91",
                          "u": "92", "v": "93",
                          "w": "94", "x": "95", "y": "96", "z": "97", " ": "98", ",": "99", ".": "100", "101": ";",
                          "'": "102", "?": "103",
                          "!": "104", ":": "105"}


def putting_in_file(return_encrypted_msg):
    """
    the fanction puts the encrypted message in the file
    :param return_encrypted_msg: the encrypted version of the message
    :return: none
    """
    file_handle = open("encrypted_msg.txt", 'w')
    file_handle.write(return_encrypted_msg)
    file_handle.close()


def pulling_from_file():
    """
    the fanction reads the file and return the message which it read from the file
    :return:encrypted_msg: the encrypted message from the file
    """
    file_handle = open("encrypted_msg.txt", 'r')
    encrypted_msg = file_handle.read()
    file_handle.close()
    return encrypted_msg


def encrypted(message):
    """
    this fanction takes the massage and returns an encrypted version of it
    :param message: the message that the user inputted
    :return: message_encrypted: the message but encrypted
    """
    message_encrypted = ""
    if message == " ":
        message_encrypted = ""
    else:
        for char in message:
            for key in TRANSLATING_DICTIONARY.keys():
                if char == key:
                    value = TRANSLATING_DICTIONARY[key]
                    message_encrypted = message_encrypted + value + ","
    message_encrypted = message_encrypted[:-1]
    return message_encrypted


def decrypted(encrypted_msg):
    """
    the fanction gets and encrypted message decrypt it and return the original message
    :param encrypted_msg: the encrypted meesage
    :return: message_decrypted: the message decrypted
    """
    message_decrypted = ""
    enc_msg = encrypted_msg.split(',')
    if enc_msg == "":
        message_decrypted = ""
    else:
        for letter in enc_msg:
            message_decrypted = message_decrypted + list(TRANSLATING_DICTIONARY.keys())[list(TRANSLATING_DICTIONARY.values()).index(letter)]
    return message_decrypted


def main():
    if sys.argv[FIRST_WORD] == 'encrypt':
        message = input("pls enter your message: ")
        return_encrypted_msg = encrypted(message)
        putting_in_file(return_encrypted_msg)
    elif sys.argv[FIRST_WORD] == 'decrypt':
        encrypted_msg = pulling_from_file()
        decrypt_msg = decrypted(encrypted_msg)
        print(decrypt_msg)
    else:
        print('wrong')


if __name__ == '__main__':
    assert encrypted("love")
    assert decrypted("33,36,93,16")
    main()
