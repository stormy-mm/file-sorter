import os
EXAMPLE_PATH = (
        r"C:\Users\User\Downloads" if os.name == "nt"
        else "/home/user/Downloads"
    )

class Messages:
    LOG_ERROR = f"Ошибка: недостаточно аргументов.\nПример ввода: python app.py {EXAMPLE_PATH}\n"
    SUCCESSFUL_SORTING = "\nСортировка прошла успешно!\n"
    UNSUCCESSFUL_SORTING = "Ошибка: Системе не удается найти указанный путь: {}\n"
    LOG = "Файл {} успешно перенесён в папку {}\n"
    NOTHING_CHANGED = "Ничего не изменилось. Всё на своих местах!\n"