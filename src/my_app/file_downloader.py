import os
from my_app.common.files_folders import FOLDERS, FILES


def adding_path(*args) -> str | bytes:
    """Возвращает склеенный путь"""
    return os.path.join(*args)


PATH = os.getcwd() + "\\mess"

os.makedirs(PATH, exist_ok=True)

# Создание файлов
for file in FILES:
    with open(adding_path(PATH, file), "a"): pass

# Создание подпапок
for folder in FOLDERS:
    os.makedirs(adding_path(PATH, folder), exist_ok=True)

print("Файлы созданы")