from sympy import FiniteField, symbols

def affine_recurrent_cipher(text, key, p, n, operation):
    # Создание поля Галуа F_(p^n)
    F = FiniteField(p, n)  # Создание объекта поля Галуа
    x = symbols('x')  # Создание символа для использования в выражениях

    # Проверка на соответствие длины ключа необходимому условию
    if len(key) != 2:
        raise ValueError("Ключ должен быть длины 2")

    a, b = key  # Разделение ключа на параметры a и b

    result_text = ""  # Переменная для хранения зашифрованного/расшифрованного текста
    for char in text:
        if char.isalpha():  # Проверка, является ли символ буквой
            char_code = ord(char) - ord('a')  # Получение числового кода символа
            if operation == 'encrypt':
                # Зашифрование символа с помощью аффинного преобразования
                encrypted_char_code = (a * char_code + b) % (p**n)
                result_text += chr(encrypted_char_code + ord('a'))  # Добавление зашифрованного символа к результату
            elif operation == 'decrypt':
                # Расшифрование символа с помощью обратного аффинного преобразования
                decrypted_char_code = ((char_code - b) * pow(a, -1, p**n)) % (p**n)
                result_text += chr(decrypted_char_code + ord('a'))  # Добавление расшифрованного символа к результату
        else:
            result_text += char  # Простое добавление символа, если это не буква

    return result_text  # Возвращение зашифрованного/расшифрованного текста

def main():
    p = 26  # Размер алфавита
    n = 1   # Поле Галуа F_p
    key = (3, 7)  # Ключ (a, b)

    plaintext = input("Введите открытый текст: ").lower()  # Получение открытого текста от пользователя

    # Зашифрование
    ciphertext = affine_recurrent_cipher(plaintext, key, p, n, 'encrypt')
    print("Зашифрованный текст:", ciphertext)

    # Расшифрование
    decrypted_text = affine_recurrent_cipher(ciphertext, key, p, n, 'decrypt')
    print("Расшифрованный текст:", decrypted_text)

if __name__ == "__main__":
    main()
