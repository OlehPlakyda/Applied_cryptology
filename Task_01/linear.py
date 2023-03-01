def encrypt_linear(plaintext, key):
    """
    Функція для шифрування тексту Лінійним шифром з ключем key
    """
    ciphertext = ''
    small_symbols = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    big_symbols = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
    l_a = len(big_symbols)
    for char in plaintext:
        if char.isalpha():
            # Визначаємо номер символа в алфавіті
            # Множимо номер на ключ та знаходимо символ
            if char.islower():
                symbol_number = small_symbols.find(char) + 1
                shifted_symbol = small_symbols[(symbol_number * key) % l_a]
            else:
                symbol_number = big_symbols.find(char) + 1
                shifted_symbol = big_symbols[(symbol_number * key) % l_a]
            # Додаємо символ до шифрованого тексту
            ciphertext += shifted_symbol
        else:
            # Додаємо символ без змін
            ciphertext += char
    return ciphertext


def decrypt_linear(ciphertext, key):
    """
    Функція для розшифрування тексту, зашифрованого Лінійним шифром з ключем key
    """
    plaintext = ''
    small_symbols = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    big_symbols = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
    l_a = len(big_symbols)
    special_key = key**(l_a-4) % l_a
    for char in ciphertext:
        if char.isalpha():
            # Визначаємо номер символа в алфавіті
            # Зміщуемо за допомогою спеціального ключа знайденого за формулою
            if char.islower():
                symbol_number = small_symbols.find(char)
                shifted_symbol = small_symbols[symbol_number * special_key % l_a - 1]
            else:
                symbol_number = big_symbols.find(char)
                shifted_symbol = big_symbols[symbol_number * special_key % l_a - 1]
            # Додаємо символ до розшифрованого тексту
            plaintext += shifted_symbol
        else:
            # Додаємо символ без змін
            plaintext += char
    return plaintext


def main():
    key = 5
    plaintext = 'Я, Плакида Олег Миколайович, студент університету.'
    encrypt_text = encrypt_linear(plaintext, key)
    print(encrypt_text)
    print(decrypt_linear(encrypt_text, key))


main()
