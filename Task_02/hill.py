import numpy  as np


def matrix_mod_inv(matrix, modulus):
    """Calculate the modular inverse of a matrix"""
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = pow(det, -1, modulus)
    matrix_modulus_inv = det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    return matrix_modulus_inv


def create_hill_key(key):
    """Create the Hill cipher key matrix"""
    key = key.upper().replace(" ", "")
    key_len = len(key)
    key_size = int(key_len ** 0.5)
    if key_size ** 2 != key_len:
        raise ValueError("Invalid key length")
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key_index = [alphabet.index(letter) for letter in key]
    hill_key = np.reshape(key_index, (key_size, key_size))
    return hill_key


def hill_encrypt(plaintext, key):
    hill_key = create_hill_key(key)
    plaintext = plaintext.upper().replace(" ", "")
    plaintext_len = len(plaintext)
    plaintext_size = int(plaintext_len ** 0.5)
    if plaintext_size ** 2 != plaintext_len:
        plaintext += "X" * (plaintext_size ** 2 - plaintext_len)
        plaintext_size = plaintext_size + 1
    plaintext_index = [alphabet.index(letter) for letter in plaintext]
    plaintext_matrix = np.reshape(plaintext_index, (plaintext_size, plaintext_size))
    ciphertext_matrix = np.matmul(hill_key, plaintext_matrix) % 26
    ciphertext_index = list(ciphertext_matrix.flatten())
    ciphertext = "".join([alphabet[index] for index in ciphertext_index])
    return ciphertext


def hill_decrypt(ciphertext, key):
    """Decrypt ciphertext with the Hill cipher"""
    hill_key = create_hill_key(key)
    ciphertext = ciphertext.upper().replace(" ", "")
    ciphertext_len = len(ciphertext)
    ciphertext_size = int(ciphertext_len ** 0.5)
    if ciphertext_size ** 2 != ciphertext_len:
        raise ValueError("Invalid ciphertext length")
    ciphertext_index = [alphabet.index(letter) for letter in ciphertext]
    ciphertext_matrix = np.reshape(ciphertext_index, (ciphertext_size, ciphertext_size))
    hill_key_inv = matrix_mod_inv(hill_key, 26)
    plaintext_matrix = np.matmul(hill_key_inv, ciphertext_matrix) % 26
    plaintext_index = list(plaintext_matrix.flatten())
    plaintext = "".join([alphabet[index] for index in plaintext_index])
    return plaintext


def main():
    key = "GYBNQKURP"
    plaintext = "HELLO WORLD"
    ciphertext = hill_encrypt(plaintext, key)
    decrypted_plaintext = hill_decrypt(ciphertext, key)
    print('Текст: ', plaintext)
    print('Зашифрований текст: ', ciphertext)
    print('Розшифрований текст:', decrypted_plaintext)


main()
