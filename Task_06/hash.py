import hashlib


def encrypt_hash(plaintext):
    # Конвертуємо текст у байтовий рядок
    text_bytes = plaintext.encode('utf-8')

    # Використовуємо геш-функцію SHA1 для шифрування тексту
    hashed_text = hashlib.sha1(text_bytes).hexdigest()

    # Повертаємо результат
    return hashed_text


def main():
    # Вводимо текст
    plaintext = 'Плакида Олег Миколайович'

    encrypt_text = encrypt_hash(plaintext)
    print('Текст: ', plaintext)
    print('Зашифрований текст за допомогою геш-функції SHA1: ' + encrypt_text)


main()
