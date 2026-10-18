import getpass
from colorama import Fore, Style


def login(users):
    print(f"\n{Fore.CYAN}--- Вход в систему ---{Style.RESET_ALL}")
    while True:
        username = input("Введите логин (или 'exit' для выхода): ")
        if username.lower() == 'exit':
            return None

        if username not in users:
            print(f"{Fore.RED}Ошибка: Пользователь не найден.{Style.RESET_ALL}")
            continue

        password = getpass.getpass("Введите пароль: ")

        if users[username]["password"] == password:
            print(f"{Fore.GREEN}Успешная аутентификация. Добро пожаловать, {username}!{Style.RESET_ALL}")
            return username
        else:
            print(f"{Fore.RED}Ошибка: Неверный пароль.{Style.RESET_ALL}")