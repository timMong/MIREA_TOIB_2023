# воспользуемся модулем "re", который отвечает за регулярные выражения
import re

def check_password(password):
    # Проверяем длину пароля
    if len(password) < 8:
        return False

    # Проверяем наличие прописных букв
    if not any(c.isupper() for c in password):
        return False

    # Проверяем наличие строчных букв
    if not any(c.islower() for c in password):
        return False

    # Проверяем наличие цифр
    if not any(c.isdigit() for c in password):
        return False

    # Проверяем наличие специальных символов
    if not re.search("[!@#$%&]", password):
        return False

    return True

# Вводим пароль до тех пор, пока не будут удовлетворены все условия
while True:
    password = input("Введите пароль: ")
    if check_password(password):
        print("Действительный пароль")
        break
    else:
        print("Пароль не соответствует требованиям")
