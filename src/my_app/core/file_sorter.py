import os


def adding_path(*args) -> str | bytes:
    """Возвращает склеенный путь"""
    return os.path.join(*args)


class FileSorter:
    """Класс для управления сортировщиком файлов"""

    def __init__(self):
        """Инициализация словаря с названиями директорий и расширениями"""
        self._DICT_WITH_EXTENSION = {
            "Images": (".jpg", ".jpeg", ".png", ".svg"),
            "Documents": (".doc", ".docx", ".txt", ".pdf", ".xlsx", ".pptx"),
            "Archives": (".zip", ".gz", ".tar"),
            "Audio": (".mp3", ".ogg", ".wav", ".amr"),
            "Video": (".avi", ".mp4", ".mov", ".mkv"),
            "Other": ()
        }

    def get_extension(self) -> dict:
        """Возвращает словарь папок и расширений"""
        return self._DICT_WITH_EXTENSION

    @staticmethod
    def get_folder_user(folder_name: str) -> list:
        """Возвращает список файлов в директории пользователя"""
        if os.path.exists(folder_name):
            return os.listdir(folder_name)
        else:
            raise FileNotFoundError

    def create_folder_in_user(self, folder_name: str) -> bool:
        """Создание папки в директории пользователя"""
        for folder in self.get_extension().keys():
            os.makedirs(adding_path(folder_name, folder), exist_ok=True)
        return True

    def is_root_folder_clean(self, folder_name: str) -> bool:
        """Проверяет отсутствие файлов в директории"""
        for file in self.get_folder_user(folder_name):
            if os.path.isfile(adding_path(folder_name, file)):
                return False
        return True

    def _get_target_folder(self, extension: str) -> str:
        """Возвращает название папки"""
        for folder, extensions in self.get_extension().items():
            if extension in extensions:
                return folder
        return "Other"

    def sort_files(self, folder_user: str) -> dict:
        """Сортирует файлы"""
        logs = {}
        for file in self.get_folder_user(folder_user):
            src = adding_path(folder_user, file)

            if not os.path.isfile(src):
                continue

            extension = os.path.splitext(file)[1]
            target_folder = self._get_target_folder(extension)
            dst = adding_path(folder_user, target_folder, file)

            try:
                os.rename(src, dst)
                logs[file] = os.path.split(dst)[0]
            except FileExistsError:
                pass

        return logs

    @staticmethod
    def remove_empty_folders(folder_user: str) -> None:
        """Удаляет пустые папки в директории пользователя"""
        for root, dirs, files in os.walk(folder_user, topdown=False):
            for dir_name in dirs:
                full_path = os.path.join(root, dir_name)

                try:
                    if not os.listdir(full_path):
                        os.rmdir(full_path)
                except FileNotFoundError:
                    pass