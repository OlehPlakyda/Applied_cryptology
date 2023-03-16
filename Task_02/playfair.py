def create_playfair_key(key):
    """Створює ключ шифру Playfair"""
    key = key.replace(" ", "").upper()
    key = key.replace("J", "I")
    key_set = set(key)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_list = list(key_set)
    for letter in alphabet:
        if letter not in key_set:
            key_list.append(letter)
    playfair_key = "".join(key_list)
    return playfair_key


def playfair_encrypt(plaintext, key):
    """Шифрує відкритий текст за допомогою шифру Playfair"""
    playfair_key = create_playfair_key(key)
    plaintext = plaintext.replace(" ", "").upper()
    plaintext = plaintext.replace("J", "I")
    if len(plaintext) % 2 == 1:
        plaintext += "X"
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        a = plaintext[i]
        b = plaintext[i+1]
        if a == b:
            b = "X"
        a_row, a_col = divmod(playfair_key.index(a), 5)
        b_row, b_col = divmod(playfair_key.index(b), 5)
        if a_row == b_row:
            a_col = (a_col + 1) % 5
            b_col = (b_col + 1) % 5
        elif a_col == b_col:
            a_row = (a_row + 1) % 5
            b_row = (b_row + 1) % 5
        else:
            a_col, b_col = b_col, a_col
        ciphertext += playfair_key[a_row*5+a_col]
        ciphertext += playfair_key[b_row*5+b_col]
    return ciphertext


def playfair_decrypt(ciphertext, key):
    """Розшифровує зашифрований текст за допомогою шифру Playfair"""
    playfair_key = create_playfair_key(key)
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        a = ciphertext[i]
        b = ciphertext[i+1]
        a_row, a_col = divmod(playfair_key.index(a), 5)
        b_row, b_col = divmod(playfair_key.index(b), 5)
        if a_row == b_row:
            a_col = (a_col - 1) % 5
            b_col = (b_col - 1) % 5
        elif a_col == b_col:
            a_row = (a_row - 1) % 5
            b_row = (b_row - 1) % 5
        else:
            a_col, b_col = b_col, a_col
        plaintext += playfair_key[a_row*5+a_col]
        plaintext += playfair_key[b_row*5+b_col]
    plaintext = plaintext.replace("X", "")
    return plaintext


def main():
    key = "SECRETKEY"
    plaintext = "Plakyda Oleh Mykolayovych"
    ciphertext = playfair_encrypt(plaintext, key)
    decrypted_plaintext = playfair_decrypt(ciphertext, key)
    print('Текст: ', plaintext)
    print('Зашифрований текст: ', ciphertext)
    print('Розшифрований текст:', decrypted_plaintext)
    print(create_playfair_key(key))


main()
