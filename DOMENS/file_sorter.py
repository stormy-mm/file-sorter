import os


def adding_path(*args: tuple) -> str:
    """Возвращает склеенный путь"""
    return os.path.join(*args)

class FileSorter:
    """Класс для управления сортировщиком файлов"""

    def __init__(self):
        """Инициализация словаря с названиями директорий и расширениями"""
        self._DICT_WITH_EXTENSION = {
            "Images": [".jpg", ".jpeg", ".png", ".svg"],
            "Documents": [".doc", ".docx", ".txt", ".pdf", ".xlsx", ".pptx"],
            "Archives": [".zip", ".gz", ".tar"],
            "Audio": [".mp3", ".ogg", ".wav", ".amr"],
            "Video": [".avi", ".mp4", ".mov", ".mkv"],
            "Other": []
        }

    def get_extension(self) -> dict:
        """Возвращает словарь папок и расширений"""
        return self._DICT_WITH_EXTENSION

    def get_folder_user(self, folder_name: str) -> list:
        """Возвращает директорию пользователя"""
        if os.path.exists(folder_name):
            return os.listdir(folder_name)
        else:
            raise FileNotFoundError

    def create_folder_in_user(self, folder_name: str) -> bool:
        """Создание папки в директории пользователя"""
        for folder in self.get_extension().keys():
            os.makedirs(adding_path(folder_name, folder), exist_ok=True)
        return True

    def checker_files_in_folder_user(self, folder_name: str) -> bool:
        """Проверяет отсутствие файлов в директории"""
        for file in self.get_folder_user(folder_name):
            if os.path.isfile(adding_path(folder_name, file)):
                return False
        return True

    def _get_target_folder(self, extension: str) -> str:
        for folder, extensions in self.get_extension().items():
            if extension in extensions:
                return folder
        return "Other"

    def sort_files(self, folder_user: str) -> bool:
        for file in self.get_folder_user(folder_user):
            src = adding_path(folder_user, file)

            if not os.path.isfile(src):
                continue

            extension = os.path.splitext(file)[1]
            target_folder = self._get_target_folder(extension)
            dst = adding_path(folder_user, target_folder, file)

            try:
                os.rename(src, dst)
            except FileExistsError:
                pass

        return True


def run(path: str) -> bool:
    """Запуск программы"""
    FILE_SORT = FileSorter()
    try:
        FILE_SORT.get_folder_user(path)
    except FileNotFoundError:
        return False
    FILE_SORT.create_folder_in_user(path)
    FILE_SORT.sort_files(path)
    return FILE_SORT.checker_files_in_folder_user(path)