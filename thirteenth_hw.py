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
    for key in range(1, 95):
        decrypted_message = cipher.decrypt(encrypted_message, key)
        print(f'Ключ: {key}, Расшифрованное: {decrypted_message}')


cipher = CaesarsCipher()

encrypted_password = "o3zR v..D0?yRA0R8FR8v47w0ER4.R1WdC!sLF5D"
print("\nПопытка подобрать ключ для зашифрованного пароля:")
find_key(encrypted_password)
