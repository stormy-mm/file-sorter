import os
EXAMPLE_PATH = (
        r"C:\Users\User\Downloads" if os.name == "nt"
        else "/home/user/downloads"
    )

class Messages:
    LOG_ERROR = (f"Ошибка: недостаточно аргументов\nПример ввода: python -m file_sorter {EXAMPLE_PATH}\n"
                 f"Для получения справки: python -m file_sorter -h")
    SUCCESSFUL_SORTING = "\nСортировка прошла успешно!\n"
    UNFOUND_PATH = "Ошибка: Системе не удается найти указанный путь: {}\n"
    LOG = "Файл {} успешно перенесён в папку {}\n"
    NOTHING_CHANGED = "Ничего не изменилось. Всё на своих местах!\n"
    FILES_LOADS = "Тестовые файлы загружены в {}\n"
    HELP = ("\nДля сортировки файлов нужно ввести путь к директории\n"
            "Пример ввода: python -m file_sorter {EXAMPLE_PATH}\n\n"
            "Для теста программы можно загрузить готовые файлы по команде:\n"
            "python -m file_sorter -l\n"
            "python -m file_sorter --load")
    ERROR = "Произошла ошибка: некоторые файлы остались в указанной директории"