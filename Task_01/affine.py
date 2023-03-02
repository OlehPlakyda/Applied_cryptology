def encrypt_affine(plaintext, key, multiplier):
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
                shifted_symbol = small_symbols[(symbol_number * multiplier + key) % l_a]
            else:
                symbol_number = big_symbols.find(char) + 1
                shifted_symbol = big_symbols[(symbol_number * multiplier + key) % l_a]
            # Додаємо символ до шифрованого тексту
            ciphertext += shifted_symbol
        else:
            # Додаємо символ без змін
            ciphertext += char
    return ciphertext


def decrypt_affine(ciphertext, key, multiplier):
    """
    Функція для розшифрування тексту, зашифрованого Лінійним шифром з ключем key
    """
    plaintext = ''
    small_symbols = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    big_symbols = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
    l_a = len(big_symbols)
    special_multiplier = multiplier**(l_a-4) % l_a
    special_key = (special_multiplier * key * (-1)) % l_a
    for char in ciphertext:
        if char.isalpha():
            # Визначаємо номер символа в алфавіті
            # Зміщуемо за допомогою спеціального ключа знайденого за формулою
            if char.islower():
                symbol_number = small_symbols.find(char)
                shifted_symbol = small_symbols[(symbol_number * special_multiplier + special_key) % l_a - 1]
            else:
                symbol_number = big_symbols.find(char)
                shifted_symbol = big_symbols[(symbol_number * special_multiplier + special_key) % l_a - 1]
            # Додаємо символ до розшифрованого тексту
            plaintext += shifted_symbol
        else:
            # Додаємо символ без змін
            plaintext += char
    return plaintext


def main():
    key = 3
    multiplier = 5
    plaintext = 'Я, Плакида Олег Миколайович, студент університету.'
    encrypt_text = encrypt_affine(plaintext, key, multiplier)
    print('Текст: ', plaintext)
    print('Зашифрований текст: ', encrypt_text)
    print('Розшифрований текст:', decrypt_affine(encrypt_text, key, multiplier))


main()
