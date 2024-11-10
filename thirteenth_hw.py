class CaesarsCipher:
    def __init__(self):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."
        self.alphabet_length = len(self.alphabet)

    def decrypt(self, message: str, key: int) -> str:
        """Расшифровать сообщение с заданным ключом."""
        decrypted_message = ""
        for char in message:
            if char in self.alphabet:
                index = (self.alphabet.index(char) - key) % self.alphabet_length
                decrypted_message += self.alphabet[index]
            else:
                decrypted_message += char
        return decrypted_message

    def encrypt(self, message: str, key: int) -> str:
        """Зашифровать сообщение с заданным ключом."""
        encrypted_message = ""
        for char in message:
            if char in self.alphabet:
                index = (self.alphabet.index(char) + key) % self.alphabet_length
                encrypted_message += self.alphabet[index]
            else:
                encrypted_message += char
        return encrypted_message


def find_key(encrypted_message: str) -> None:
    """Подобрать ключ для расшифровки сообщения."""
    cipher = CaesarsCipher()
    results = []
    for key in range(1, 95):
        decrypted_message = cipher.decrypt(encrypted_message, key)
        results.append(f'Ключ: {key}, Расшифрованное: {decrypted_message}')
    return results

def main():
    cipher = CaesarsCipher()

    original_message = "The vacation was a success"
    key = 3
    encrypted_message = cipher.encrypt(original_message, key)

    print(f'Зашифрованное сообщение с ключом {key}: {encrypted_message}')

    encrypted_password = "o3zR v..D0?yRA0R8FR8v47w0ER4.R1WdC!sLF5D"
    print("\nПопытка подобрать ключ для зашифрованного пароля:")
    key_results = find_key(encrypted_password)

    for result in key_results:
        print(result)

    while True:
        file_path = input("Введите путь к файлу для записи результатов: ")
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(f'Оригинальное сообщение: {original_message}\n')
                file.write(f'Зашифрованное сообщение с ключом {key}: {encrypted_message}\n')
                file.write("\nРезультаты подбора ключа:\n")
                for result in key_results:
                    file.write(result + '\n')
            print(f'Результаты записаны в файл: {file_path}')
            break
        except Exception as e:
            print(f'Ошибка при записи в файл: {e}. Попробуйте еще раз.')

if __name__ == "__main__":
    main()
    
