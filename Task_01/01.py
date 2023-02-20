def encrypt_caesar(plaintext, shift):
    """
    Функція для шифрування тексту шифром Цезаря з ключем shift
    """
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            # Визначаємо номер символа в алфавіті
            if char.islower():
                char_code = ord(char) - 1072
            else:
                char_code = ord(char) - 1040
            # Зсуваємо символ на shift позицій
            shifted_code = (char_code + shift) % 33
            # Перетворюємо зсунутий код у символ
            if char.islower():
                shifted_char = chr(shifted_code + 1072)
            else:
                shifted_char = chr(shifted_code + 1040)
            # Додаємо символ до шифрованого тексту
            ciphertext += shifted_char
        else:
            # Додаємо символ без змін
            ciphertext += char
    return ciphertext


def decrypt_caesar(ciphertext, shift):
    """
    Функція для розшифрування тексту, зашифрованого шифром Цезаря з ключем shift
    """
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            # Визначаємо номер символа в алфавіті
            if char.islower():
                char_code = ord(char) - 1072
            else:
                char_code = ord(char) - 1040
            # Зсуваємо символ на shift позицій в зворотному напрямку
            shifted_code = (char_code - shift) % 33
            # Перетворюємо зсунутий код у символ
            if char.islower():
                shifted_char = chr(shifted_code + 1072)
            else:
                shifted_char = chr(shifted_code + 1040)
            # Додаємо символ до розшифрованого тексту
            plaintext += shifted_char
        else:
            # Додаємо символ без змін
            plaintext += char
    return plaintext


def main():
    encrypt_text = encrypt_caesar('Я, Плакида Олег Миколайович, студент університету.', 4)
    print(encrypt_text)
    print(decrypt_caesar(encrypt_text, 4))


main()
