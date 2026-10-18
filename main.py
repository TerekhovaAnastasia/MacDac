from colorama import init, Fore, Style
from storage import load_data
from auth import login
from access_control import authorize
from actions import execute_action
from models import ACTIONS_MAP

init(autoreset=True)


def main_menu(username, data):
    while True:
        print(f"\n{Fore.CYAN}=== Меню пользователя: {username} ==={Style.RESET_ALL}")
        print("1. Прочитать объект")
        print("2. Записать в объект (перезапись)")
        print("3. Дописать в конец объекта")
        print("4. Удалить объект (очистить строку)")
        print("5. Выйти из системы")

        choice = input("Выберите действие (1-5): ")

        if choice == "5":
            print("Выход из системы...")
            break

        if choice not in ACTIONS_MAP:
            print(f"{Fore.RED}Неверный выбор.{Style.RESET_ALL}")
            continue

        action = ACTIONS_MAP[choice]
        obj_name = input("Введите имя объекта: ")

        is_allowed, message = authorize(username, obj_name, action, data)

        if is_allowed:
            execute_action(username, obj_name, action, data)
        else:
            print(f"\n{Fore.RED}[ОТКАЗ В ДОСТУПЕ] {message}{Style.RESET_ALL}")


if __name__ == "__main__":
    try:
        data = load_data()

        current_user = login(data["users"])

        if current_user:
            main_menu(current_user, data)

    except KeyboardInterrupt:
        print("\nПринудительное завершение работы.")
    except Exception as e:
        print(f"{Fore.RED}Критическая ошибка: {e}{Style.RESET_ALL}")