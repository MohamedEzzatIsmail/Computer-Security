import customtkinter
import numpy as np

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root=customtkinter.CTk()
root.title("Cipher")
root.geometry('1200x600')


lable=customtkinter.CTkLabel(master=root, text='Cipher', text_color='#095783', font=('', 40))
lable.pack(pady=10, padx=20)
"""
tabview = customtkinter.CTkTabview(master=root, width=250)
tabview.pack(pady=20, padx=60, fill="both", expand=True)
tabview.add("Encryption")
tabview.add("Decryption")
tabview.tab("Encryption").grid_columnconfigure(0, weight=1)
tabview.tab("Decryption").grid_columnconfigure(0, weight=1)
"""
tabview = customtkinter.CTkTabview(master=root, width=250)
tabview.pack(pady=20, padx=60, fill="both", expand=True)
tabview.add("Ceaser")
tabview.add("Playfair")
tabview.add("Polyalphabetic")
tabview.tab("Ceaser").grid_columnconfigure(0, weight=1)
tabview.tab("Playfair").grid_columnconfigure(0, weight=1)
tabview.tab("Polyalphabetic").grid_columnconfigure(0, weight=1)

tabview2 = customtkinter.CTkTabview(master=tabview.tab("Ceaser"), width=250)
tabview2.pack(pady=10, padx=10, fill="both", expand=True)
tabview2.add("Encryption")
tabview2.add("Decryption")
tabview2.tab("Encryption").grid_columnconfigure(0, weight=1)
tabview2.tab("Decryption").grid_columnconfigure(0, weight=1)


tabview3 = customtkinter.CTkTabview(master=tabview.tab("Playfair"), width=250)
tabview3.pack(pady=10, padx=10, fill="both", expand=True)
tabview3.add("Encryption")
tabview3.add("Decryption")
tabview3.tab("Encryption").grid_columnconfigure(0, weight=1)
tabview3.tab("Decryption").grid_columnconfigure(0, weight=1)


tabview4 = customtkinter.CTkTabview(master=tabview.tab("Polyalphabetic"), width=250)
tabview4.pack(pady=10, padx=10, fill="both", expand=True)
tabview4.add("Encryption")
tabview4.add("Decryption")
tabview4.tab("Encryption").grid_columnconfigure(0, weight=1)
tabview4.tab("Decryption").grid_columnconfigure(0, weight=1)


# main fuctions
def encrypt_Ceaser(text, s):
	result = ""
	# traverse text
	for i in range(len(text)):
		char = text[i]
		# Encrypt uppercase characters
		if (char.isupper()):
			result += chr((ord(char) + s-65) % 26 + 65)
		# Encrypt lowercase characters
		else:
			result += chr((ord(char) + s - 97) % 26 + 97)
	return result


def decrypt_Ceaser(key, message):
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alpha: #if the letter is actually a letter
            #find the corresponding ciphertext letter in the alphabet
            letter_index = (alpha.find(letter) - key) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result


def actceaser():
    text = entry11.get()
    key = int(entry12.get())
    result = encrypt_Ceaser(text, key)
    lable1.configure(text=f'Cipher Text: {result}')

def actceaser1():
    text = entry113.get()
    key = int(entry123.get())
    result = decrypt_Ceaser(key, text)
    lable13.configure(text=f'Plane Text: {result}')


# poly
def vigenere_encrypt(plaintext, key):
    # Convert plaintext and key to uppercase
    plaintext = plaintext.upper()
    key = key.upper()

    # Generate repeating key
    key_len = len(key)
    repeat_factor = len(plaintext) // key_len + 1
    repeat_key = (key * repeat_factor)[:len(plaintext)]

    # Encrypt plaintext using Vigenère cipher
    ciphertext = ''
    for i in range(len(plaintext)):
        p = ord(plaintext[i]) - ord('A')
        k = ord(repeat_key[i]) - ord('A')
        c = chr((p + k) % 26 + ord('A'))
        ciphertext += c

    return ciphertext


def vigenere_decrypt(ciphertext, key):
    # Convert ciphertext and key to uppercase
    ciphertext = ciphertext.upper()
    key = key.upper()

    # Generate repeating key
    key_len = len(key)
    repeat_factor = len(ciphertext) // key_len + 1
    repeat_key = (key * repeat_factor)[:len(ciphertext)]

    # Decrypt ciphertext using Vigenère cipher
    plaintext = ''
    for i in range(len(ciphertext)):
        c = ord(ciphertext[i]) - ord('A')
        k = ord(repeat_key[i]) - ord('A')
        p = chr((c - k) % 26 + ord('A'))
        plaintext += p

    return plaintext


def actpoly():
    plaintext = entry31.get()
    key = entry32.get()
    ciphertext = vigenere_encrypt(plaintext, key)
    lable3.configure(text=f'Cipher Text: {ciphertext}')


def actpoly1():
    plaintext = entry313.get()
    key = entry323.get()
    ciphertext = vigenere_decrypt(plaintext, key)
    lable33.configure(text=f'Plane Text: {ciphertext}')


# playfair
def matrix(x, y, initial):
    return [[initial for i in range(x)] for j in range(y)]


def set(text):
    key = text
    key = key.replace(" ", "")
    key = key.upper()
    result = list()
    for c in key:  # storing key
        if c not in result:
            if c == 'J':
                result.append('I')
            else:
                result.append(c)
    flag = 0
    for i in range(65, 91):  # storing other character
        if chr(i) not in result:
            if i == 73 and chr(74) not in result:
                result.append("I")
                flag = 1
            elif flag == 0 and i == 73 or i == 74:
                pass
            else:
                result.append(chr(i))
    k = 0
    global my_matrix
    my_matrix = matrix(5, 5, 0)  # initialize matrix
    for i in range(0, 5):  # making matrix
        for j in range(0, 5):
            my_matrix[i][j] = result[k]
            k += 1

def locindex(c):  # get location of each character
    loc = list()
    if c == 'J':
        c = 'I'
    for i, j in enumerate(my_matrix):
        for k, l in enumerate(j):
            if c == l:
                loc.append(i)
                loc.append(k)
                return loc


def encryptplay():  # Encryption
    ms1=ms2=ms3=""
    x = []
    msg = entry21.get()
    msg = msg.upper()
    msg = msg.replace(" ", "")
    i = 0
    for s in range(0, len(msg) + 1, 2):
        if s < len(msg) - 1:
            if msg[s] == msg[s + 1]:
                msg = msg[:s + 1] + 'X' + msg[s + 1:]
    if len(msg) % 2 != 0:
        msg = msg[:] + 'X'
    while i < len(msg):
        loc = list()
        loc = locindex(msg[i])
        loc1 = list()
        loc1 = locindex(msg[i + 1])
        ms1 = ("{}{}".format(my_matrix[(loc[0] + 1) % 5][loc[1]], my_matrix[(loc1[0] + 1) % 5][loc1[1]]))
        if loc[1] == loc1[1]:
            x.append(ms1)
        elif loc[0] == loc1[0]:
            ms2 = ("{}{}".format(my_matrix[loc[0]][(loc[1] + 1) % 5], my_matrix[loc1[0]][(loc1[1] + 1) % 5]))
            x.append(ms2)
        else:
            ms3 = ("{}{}".format(my_matrix[loc[0]][loc1[1]], my_matrix[loc1[0]][loc[1]]))
            x.append(ms3)
        i = i + 2
    return x

def decryptplay():  # decryption
    ms1 = ms2 = ms3 = ""
    x = []
    msg = entry233.get()
    msg = msg.upper()
    msg = msg.replace(" ", "")
    i = 0
    while i < len(msg):
        loc = list()
        loc = locindex(msg[i])
        loc1 = list()
        loc1 = locindex(msg[i + 1])
        if loc[1] == loc1[1]:
            ms1 = ("{}{}".format(my_matrix[(loc[0] - 1) % 5][loc[1]], my_matrix[(loc1[0] - 1) % 5][loc1[1]]))
            x.append(ms1)
        elif loc[0] == loc1[0]:
            ms2 = ("{}{}".format(my_matrix[loc[0]][(loc[1] - 1) % 5], my_matrix[loc1[0]][(loc1[1] - 1) % 5]))
            x.append(ms2)
        else:
            ms3 = ("{}{}".format(my_matrix[loc[0]][loc1[1]], my_matrix[loc1[0]][loc[1]]))
            x.append(ms3)
        i = i + 2
    return x

# Function to generate the 5x5 key square matrix
def generateKeyTable(word, list1):
    key_letters = []
    for i in word:
        if i not in key_letters:
            key_letters.append(i)

    compElements = []
    for i in key_letters:
        if i not in compElements:
            compElements.append(i)
    for i in list1:
        if i not in compElements:
            compElements.append(i)

    matrix = []
    while compElements != []:
        matrix.append(compElements[:5])
        compElements = compElements[5:]

    return matrix



def actplay():
    key = entry22.get()
    set(key)
    list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    mat = generateKeyTable(key, list1)
    result = encryptplay()
    lable2.configure(text=f'Cipher Text: {result}')
    lable21.configure(text=f'Key Matrix: {mat}')


def actplaydec():
    key = entry223.get()
    set(key)
    list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    mat = generateKeyTable(key, list1)
    result = decryptplay()
    lable2333.configure(text=f'Plane Text: {result}')
    lable2133.configure(text=f'Key Matrix: {mat}')



# body
entry11 = customtkinter.CTkEntry(master=tabview2.tab("Encryption"), placeholder_text='Plain Text')
entry11.pack(pady=10)
entry12 = customtkinter.CTkEntry(master=tabview2.tab("Encryption"), placeholder_text='Key')
entry12.pack(pady=10)
btn1 = customtkinter.CTkButton(master=tabview2.tab("Encryption"), text="encrypt", command=actceaser)
btn1.pack(pady=10)
lable1 = customtkinter.CTkLabel(master=tabview2.tab("Encryption"), text='', text_color='#095783', font=('', 20))
lable1.pack(pady=10, padx=20)

entry21 = customtkinter.CTkEntry(master=tabview3.tab("Encryption"), placeholder_text='Plain Text')
entry21.pack(pady=10)
entry22 = customtkinter.CTkEntry(master=tabview3.tab("Encryption"), placeholder_text='Key')
entry22.pack(pady=10)
btn11 = customtkinter.CTkButton(master=tabview3.tab("Encryption"), text="encrypt", command=actplay)
btn11.pack(pady=10)
lable21 = customtkinter.CTkLabel(master=tabview3.tab("Encryption"), text='', text_color='#095783', font=('', 15))
lable21.pack(pady=10, padx=20)
lable2 = customtkinter.CTkLabel(master=tabview3.tab("Encryption"), text='', text_color='#095783', font=('', 20))
lable2.pack(pady=10, padx=20)

entry31 = customtkinter.CTkEntry(master=tabview4.tab("Encryption"), placeholder_text='Plain Text')
entry31.pack(pady=10)
entry32 = customtkinter.CTkEntry(master=tabview4.tab("Encryption"), placeholder_text='Key')
entry32.pack(pady=10)
btn1 = customtkinter.CTkButton(master=tabview4.tab("Encryption"), text="encrypt",command=actpoly)
btn1.pack(pady=10)
lable3 = customtkinter.CTkLabel(master=tabview4.tab("Encryption"), text='', text_color='#095783', font=('', 20))
lable3.pack(pady=10, padx=20)

entry233 = customtkinter.CTkEntry(master=tabview3.tab("Decryption"), placeholder_text='Cipher Text')
entry233.pack(pady=10)
entry223 = customtkinter.CTkEntry(master=tabview3.tab("Decryption"), placeholder_text='Key')
entry223.pack(pady=10)
btn1 = customtkinter.CTkButton(master=tabview3.tab("Decryption"), text="encrypt", command=actplaydec)
btn1.pack(pady=10)
lable2133 = customtkinter.CTkLabel(master=tabview3.tab("Decryption"), text='', text_color='#095783', font=('', 15))
lable2133.pack(pady=10, padx=20)
lable2333 = customtkinter.CTkLabel(master=tabview3.tab("Decryption"), text='', text_color='#095783', font=('', 20))
lable2333.pack(pady=10, padx=20)

entry113 = customtkinter.CTkEntry(master=tabview2.tab("Decryption"), placeholder_text='Cipher Text')
entry113.pack(pady=10)
entry123 = customtkinter.CTkEntry(master=tabview2.tab("Decryption"), placeholder_text='Key')
entry123.pack(pady=10)
btn1 = customtkinter.CTkButton(master=tabview2.tab("Decryption"), text="encrypt", command=actceaser1)
btn1.pack(pady=10)
lable13 = customtkinter.CTkLabel(master=tabview2.tab("Decryption"), text='', text_color='#095783', font=('', 20))
lable13.pack(pady=10, padx=20)

entry313 = customtkinter.CTkEntry(master=tabview4.tab("Decryption"), placeholder_text='Cipher Text')
entry313.pack(pady=10)
entry323 = customtkinter.CTkEntry(master=tabview4.tab("Decryption"), placeholder_text='Key')
entry323.pack(pady=10)
btn1 = customtkinter.CTkButton(master=tabview4.tab("Decryption"), text="encrypt",command=actpoly1)
btn1.pack(pady=10)
lable33 = customtkinter.CTkLabel(master=tabview4.tab("Decryption"), text='', text_color='#095783', font=('', 20))
lable33.pack(pady=10, padx=20)

def change_appearance_mode_event( new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)


appearance_mode_label = customtkinter.CTkLabel(root, text="Appearance Mode:", anchor="w")
appearance_mode_label.pack()
appearance_mode_optionemenu = customtkinter.CTkOptionMenu(root, values=["Light", "Dark"]
                                                          , command=change_appearance_mode_event)
appearance_mode_optionemenu.pack(pady=10)

appearance_mode_optionemenu.set("Dark")

root.mainloop()

