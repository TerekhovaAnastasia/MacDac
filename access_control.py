from models import LEVELS


def check_mac(user_level, obj_level, action):
    if action == "read":
        # правило "Не читать выше"
        if user_level >= obj_level:
            return True, ""
        return False, "MAC: Отказано (Нарушение правила 'Не читать выше')"
    elif action in ["write", "append", "delete"]:
        # правило "Не писать ниже"
        if user_level <= obj_level:
            return True, ""
        return False, "MAC: Отказано (Нарушение правила 'Не писать ниже')"
    return True, ""


def check_dac(username, obj_data, action):
    if obj_data["owner"] == username:
        return True, ""

    acl = obj_data.get("acl", {})
    user_rights = acl.get(username, [])

    if action == "delete" and ("write" in user_rights or "delete" in user_rights):
        return True, ""

    if action in user_rights:
        return True, ""

    return False, "DAC: Отказано (Нет прав в списке контроля доступа)"


def authorize(username, obj_name, action, data):
    """Комплексная проверка доступа (сначала MAC, потом DAC)."""
    user = data["users"][username]
    obj = data["objects"].get(obj_name)

    if not obj:
        return False, "Ошибка: Объект не найден."

    user_level = LEVELS[user["clearance"]]
    obj_level = LEVELS[obj["classification"]]

    #MAC
    mac_ok, mac_msg = check_mac(user_level, obj_level, action)
    if not mac_ok:
        return False, mac_msg

    #DAC
    dac_ok, dac_msg = check_dac(username, obj, action)
    if not dac_ok:
        return False, dac_msg

    return True, "Доступ разрешен"