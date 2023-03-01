def encrypt_caesar(plaintext, shift):
    """
    Функція для шифрування тексту шифром Цезаря з ключем shift
    """
    ciphertext = ''
    small_symbols = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    big_symbols = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
    for char in plaintext:
        if char.isalpha():
            # Визначаємо номер символа в алфавіті
            # Зсуваємо символ на shift позицій
            if char.islower():
                symbol_number = small_symbols.find(char)
                shifted_symbol = small_symbols[(symbol_number + shift) % 33]
            else:
                symbol_number = big_symbols.find(char)
                shifted_symbol = big_symbols[(symbol_number + shift) % 33]
            # Додаємо символ до шифрованого тексту
            ciphertext += shifted_symbol
        else:
            # Додаємо символ без змін
            ciphertext += char
    return ciphertext


def decrypt_caesar(ciphertext, shift):
    """
    Функція для розшифрування тексту, зашифрованого шифром Цезаря з ключем shift
    """
    plaintext = ''
    small_symbols = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    big_symbols = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
    for char in ciphertext:
        if char.isalpha():
            # Визначаємо номер символа в алфавіті
            # Зсуваємо символ на shift позицій
            if char.islower():
                symbol_number = small_symbols.find(char)
                shifted_symbol = small_symbols[(symbol_number - shift) % 33]
            else:
                symbol_number = big_symbols.find(char)
                shifted_symbol = big_symbols[(symbol_number - shift) % 33]
            # Додаємо символ до шифрованого тексту
            plaintext += shifted_symbol
        else:
            # Додаємо символ без змін
            plaintext += char
    return plaintext


def main():
    shift = 4
    plaintext = 'Я, Плакида Олег Миколайович, студент університету.'
    encrypt_text = encrypt_caesar(plaintext, shift)
    print(encrypt_text)
    print(decrypt_caesar(encrypt_text, shift))


main()
