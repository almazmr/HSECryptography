from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def pad(data):
    # Функция для дополнения данных до размера блока AES
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()
    return padded_data

def unpad(data):
    # Функция для удаления дополнения после расшифрования
    unpadder = padding.PKCS7(128).unpadder()
    unpadded_data = unpadder.update(data) + unpadder.finalize()
    return unpadded_data

def encrypt_file(input_file, output_file, key, mode):
    # Функция для шифрования файла
    iv = os.urandom(16)  # Генерируем случайный вектор инициализации
    cipher = Cipher(algorithms.AES(key), mode, backend=default_backend())  # Создаем объект шифра AES с выбранным режимом
    encryptor = cipher.encryptor()
    with open(input_file, 'rb') as f:
        plaintext = f.read()  # Читаем открытый текст из файла
    padded_plaintext = pad(plaintext)  # Добавляем дополнение к открытому тексту
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()  # Шифруем открытый текст
    with open(output_file, 'wb') as f:
        f.write(iv + ciphertext)  # Записываем вектор инициализации и зашифрованные данные в файл
    print(f"Содержимое зашифрованного файла {output_file}:")
    print(ciphertext.hex())  # Используем метод hex() для вывода в шестнадцатеричном формате

def decrypt_file(input_file, output_file, key, mode):
    # Функция для расшифрования файла
    with open(input_file, 'rb') as f:
        iv = f.read(16)  # Считываем вектор инициализации
        ciphertext = f.read()  # Считываем зашифрованные данные
    cipher = Cipher(algorithms.AES(key), mode, backend=default_backend())  # Создаем объект шифра AES с выбранным режимом
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()  # Расшифровываем данные
    unpadded_data = unpad(decrypted_data)  # Удаляем дополнение
    with open(output_file, 'wb') as f:
        f.write(unpadded_data)  # Записываем расшифрованные данные в файл
    print(f"Содержимое расшифрованного файла {output_file}:")
    print(unpadded_data.decode())

def get_cipher_mode():
    # Функция для получения выбранного пользователем режима блочного шифра
    print("Выберите режим блочного шифра:")
    print("1. ECB (Electronic Codebook)")
    print("2. CBC (Cipher Block Chaining)")
    mode_choice = input("Введите номер выбранного режима: ")
    if mode_choice == "1":
        return modes.ECB()
    elif mode_choice == "2":
        return modes.CBC(os.urandom(16))  # Генерируем случайный вектор инициализации для режима CBC
    else:
        print("Некорректный ввод. Повторите попытку.")
        return get_cipher_mode()

def get_secret_key():
    # Функция для получения секретного ключа от пользователя
    key = input("Введите секретный ключ (16 байт): ")
    if len(key) != 16:
        print("Неверная длина ключа. Ключ должен состоять из 16 символов.")
        return get_secret_key()
    return key.encode()

if __name__ == "__main__":
    input_file = "simpletext.txt"
    output_file_encrypted = "encrypted_file.enc"
    output_file_decrypted = "decrypted_file.txt"
    key = get_secret_key()  # Получаем секретный ключ от пользователя
    mode = get_cipher_mode()  # Получаем выбранный пользователем режим блочного шифра

    print("_____Шифруем..._____")
    encrypt_file(input_file, output_file_encrypted, key, mode)
    print("_____Файл успешно зашифрован._____")

    print("_____Расшифровываем..._____")
    decrypt_file(output_file_encrypted, output_file_decrypted, key, mode)
    print("_____Файл успешно расшифрован._____")
