import string

class SimpleSubstitutionCipher:
    def __init__(self):
        # Создаем алфавит, который будет использоваться для шифрования
        self.alphabet = string.ascii_lowercase

    def encrypt(self, plaintext, key):
        # Функция для шифрования текста
        encrypted_text = ''
        # Проходим по каждому символу в открытом тексте
        for char in plaintext:
            # Проверяем, находится ли символ в алфавите
            if char.lower() in self.alphabet:
                # Получаем индекс символа в алфавите
                index = self.alphabet.index(char.lower())
                # Добавляем смещение, взятое из ключа
                shifted_index = (index + int(key)) % 26
                # Получаем зашифрованный символ и добавляем его к зашифрованному тексту
                encrypted_text += self.alphabet[shifted_index]
            else:
                # Если символ не из алфавита, оставляем его без изменений
                encrypted_text += char
        return encrypted_text

    def decrypt(self, ciphertext, key):
        # Функция для расшифровки текста
        decrypted_text = ''
        # Проходим по каждому символу в зашифрованном тексте
        for char in ciphertext:
            # Проверяем, находится ли символ в алфавите
            if char.lower() in self.alphabet:
                # Получаем индекс зашифрованного символа в алфавите
                index = self.alphabet.index(char.lower())
                # Вычитаем смещение, взятое из ключа
                shifted_index = (index - int(key)) % 26
                # Получаем расшифрованный символ и добавляем его к расшифрованному тексту
                decrypted_text += self.alphabet[shifted_index]
            else:
                # Если символ не из алфавита, оставляем его без изменений
                decrypted_text += char
        return decrypted_text

# Пример использования:
cipher = SimpleSubstitutionCipher()

plaintext = input("Введите текст для шифрования: ")
key = input("Введите ключ для шифрования: ")
encrypted_text = cipher.encrypt(plaintext, key)
print("Зашифрованный текст:", encrypted_text)

decrypted_text = cipher.decrypt(encrypted_text, key)
print("Расшифрованный текст:", decrypted_text)
