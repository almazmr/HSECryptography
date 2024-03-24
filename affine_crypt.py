from sympy import mod_inverse

def affine_encrypt(text, alpha, beta, m):
    encrypted_text = ""
    for char in text:
        char_lower = char.lower()  # Приводим символ к нижнему регистру
        if char_lower.isalpha():
            char_index = alphabet.index(char_lower)  # Получаем индекс символа в алфавите
            encrypted_index = (alpha * char_index + beta) % m  # Применяем аффинное преобразование
            encrypted_text += alphabet[encrypted_index]  # Добавляем зашифрованный символ к зашифрованному тексту
        else:
            encrypted_text += char
    return encrypted_text

def affine_decrypt(text, alpha, beta, m):
    decrypted_text = ""
    alpha_inverse = mod_inverse(alpha, m)  # Находим обратный элемент для alpha
    for char in text:
        char_lower = char.lower()  # Приводим символ к нижнему регистру
        if char_lower.isalpha():
            char_index = alphabet.index(char_lower)  # Получаем индекс зашифрованного символа в алфавите
            decrypted_index = (alpha_inverse * (char_index - beta)) % m  # Применяем обратное аффинное преобразование
            decrypted_text += alphabet[decrypted_index]  # Добавляем расшифрованный символ к расшифрованному тексту
        else:
            decrypted_text += char
    return decrypted_text

def main():
    text = input("Введите текст для шифрования: ")
    alpha = int(input("Введите значение alpha: "))
    beta = int(input("Введите значение beta: "))
    m = len(alphabet)  # Размер алфавита
    
    # Зашифрование
    encrypted_text = affine_encrypt(text, alpha, beta, m)
    print("Зашифрованный текст:", encrypted_text)
    
    # Расшифрование
    decrypted_text = affine_decrypt(encrypted_text, alpha, beta, m)
    print("Расшифрованный текст:", decrypted_text)

if __name__ == "__main__":
    alphabet = "abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя"  # Алфавит
    main()
