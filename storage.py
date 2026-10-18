import json
import os

FILE_NAME = "access_rules.json"


def get_default_data():
    return {
        "users": {
            "admin": {"password": "admin123", "clearance": "TOP_SECRET"},
            "manager": {"password": "pass1", "clearance": "SECRET"},
            "guest": {"password": "pass2", "clearance": "PUBLIC"}
        },
        "objects": {
            "doc_secret": {
                "value": "Секретные данные компании",
                "classification": "SECRET",
                "owner": "admin",
                "acl": {"manager": ["read", "append"]}
            },
            "doc_public": {
                "value": "Публичная инструкция",
                "classification": "PUBLIC",
                "owner": "manager",
                "acl": {"guest": ["read", "write"]}
            }
        }
    }


def load_data():
    if not os.path.exists(FILE_NAME):
        default_data = get_default_data()
        save_data(default_data)
        return default_data

    with open(FILE_NAME, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_data(data):
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)