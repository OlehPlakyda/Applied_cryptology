import hashlib

def feistel_network_encrypt(plaintext, key):
    block_size = 16  # Розмір блока (в байтах)
    rounds = 16  # Кількість раундів мережі Фейстеля

    # Використовуємо хеш-функцію SHA256 для отримання ключа шифрування/дешифрування
    hashed_key = hashlib.sha256(key.encode()).digest()

    # Розбиваємо вхідний текст на блоки
    plaintext_blocks = [plaintext[i:i + block_size] for i in range(0, len(plaintext), block_size)]

    # Переконайтесь, що розмір ключа відповідає розміру блоку
    if len(hashed_key) < block_size:
        raise ValueError("Розмір ключа менше розміру блоку")
    # Ініціалізуємо раундові ключі на основі основного ключа
    round_keys = [hashed_key[i:i + block_size] for i in range(0, block_size * rounds, block_size)]

    # Зашифровуємо кожен блок
    ciphertext_blocks = []
    for block in plaintext_blocks:
        # Застосовуємо мережу Фейстеля
        left_block, right_block = block[:block_size // 2], block[block_size // 2:]
        for _ in range(rounds):
            new_right_block = bytes([a ^ b for a, b in zip(left_block, round_keys[_])])
            new_right_block += right_block
            left_block, right_block = right_block, new_right_block

        # Об'єднуємо ліву та праву частини блоку
        ciphertext_blocks.append(left_block + right_block)

    # Повертаємо шифрований текст
    return b"".join(ciphertext_blocks)


def feistel_network_decrypt(ciphertext, key):
    block_size = 16  # Розмір блока (в байтах)
    rounds = 16  # Кількість раундів мережі Фейстеля

    # Використовуємо хеш-функцію SHA256 для отримання ключа шифрування/дешифрування
    hashed_key = hashlib.sha256(key.encode()).digest()

    # Розбиваємо шифрований текст на блоки
    ciphertext_blocks = [ciphertext[i:i + block_size] for i in range(0, len(ciphertext), block_size)]

    # Переконайтесь, що розмір ключа відповідає розміру блоку
    if len(hashed_key) < block_size:
        raise ValueError("Розмір ключа менше розміру блоку")
    # Ініціалізуємо раундові ключі на основі основного ключа
    round_keys = [hashed_key[i:i + block_size] for i in range(0, block_size * rounds, block_size)]

    # Дешифруємо кожен блок
    plaintext_blocks = []
    for block in ciphertext_blocks:
        # Застосовуємо мережу Фейстеля в зворотному порядку
        left_block, right_block = block[:block_size // 2], block[block_size // 2:]
        for _ in range(rounds - 1, -1, -1):
            new_right_block = bytes([a ^ b for a, b in zip(left_block, round_keys[_])])
            new_right_block += right_block
            left_block, right_block = right_block, new_right_block

        # Об'єднуємо ліву та праву частини блоку
        plaintext_blocks.append(left_block + right_block)

    # Повертаємо розшифрований текст
    return b"".join(plaintext_blocks)


def main():
    plaintext = input("Введіть текст для шифрування: ")
    key = input("Введіть ключ шифрування: ")

    # Шифруємо текст
    ciphertext = feistel_network_encrypt(plaintext.encode(), key)

    print("Зашифрований текст:", ciphertext.hex())

    # Дешифруємо текст
    decrypted_text = feistel_network_decrypt(ciphertext, key).decode("latin-1")

    print("Розшифрований текст:", decrypted_text)


if __name__ == "__main__":
    main()
