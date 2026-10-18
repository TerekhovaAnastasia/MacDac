from storage import save_data
from colorama import Fore, Style


def execute_action(username, obj_name, action, data):
    obj = data["objects"][obj_name]

    if action == "read":
        print(f"\n{Fore.YELLOW}[Содержимое '{obj_name}']: {obj['value']}{Style.RESET_ALL}")

    elif action == "write":
        new_val = input("Введите новое значение для записи: ")
        obj["value"] = new_val
        print(f"{Fore.GREEN}Значение '{obj_name}' перезаписано.{Style.RESET_ALL}")

    elif action == "append":
        add_val = input("Введите текст для дописывания в конец: ")
        obj["value"] += add_val
        print(f"{Fore.GREEN}Текст дописан в '{obj_name}'.{Style.RESET_ALL}")

    elif action == "delete":
        obj["value"] = ""
        print(f"{Fore.GREEN}Объект '{obj_name}' очищен (удален).{Style.RESET_ALL}")

    save_data(data)