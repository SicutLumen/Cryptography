"""Ceaser cipher"""


def Ceaser_cipher(input_text, shift_number):
    """Encryptes text using Caeser cipher"""
    encrypted_text=[]
    for i in input_text:
        if i.isalpha():
            if i.islower():
                if (ord(i)+shift_number) > ord('z'):
                    encrypted_text.append(chr(
                        (ord('a') - 1) + ((ord(i)+shift_number)-ord('z'))
                    ))
                    continue
            else:
                if (ord(i)+shift_number) > ord('Z'):
                    encrypted_text.append(chr(
                        (ord('A') - 1) + ((ord(i)+shift_number)-ord('Z'))
                    ))
                    continue

            encrypted_text.append(chr(ord(i) + shift_number))
            continue

        encrypted_text.append(i)

    ret_val = "".join(encrypted_text)
    return ret_val


def decryption(input_text, shift_number):
    """Decryptes text using Caeser cipher"""
    decrypted_text = []
    for i in input_text:
        if i.isalpha():
            if i.islower():
                if (ord(i) - shift_number) < ord('a'):
                    decrypted_text.append(chr(
                        (ord('z') + 1) - (ord('a') - (ord(i) - shift_number))
                    ))
                    continue
            else:
                if (ord(i) - shift_number) < ord('A'):
                    decrypted_text.append(chr(
                        (ord('Z') + 1) - (ord('A') - (ord(i) - shift_number))
                    ))
                    continue

            decrypted_text.append(chr(ord(i) - shift_number))
            continue

        decrypted_text.append(i)

    ret_val = "".join(decrypted_text)
    return ret_val


input_content = input("Please, enter your message: ")
#input_number = int(input("Please, enter shift number: "))
choice = int(input("Enter 1 for encryption or 2 for decryption: "))

if choice == 1:
    for input_number in range(1,26):
        print(f"Encrypted text: {Ceaser_cipher(input_content, input_number)}; shift number: {input_number}")
elif choice == 2:
    for input_number in range(1,26):
        print(f"Decrypted text: {decryption(input_content, input_number)}; shift number: {input_number}")

