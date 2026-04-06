from pathlib import Path
from typing import Iterator

from file_sorter.common.exceptions import InvalidPathError


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
            "Other": (),
        }

    def get_extension(self) -> dict:
        """Возвращает словарь папок и расширений"""
        return self._DICT_WITH_EXTENSION

    @staticmethod
    def path_check(path: Path) -> None:
        """Если будет расширение на конце, то поднимется исключение"""
        if "." in Path(path).name:
            raise InvalidPathError

    def get_folder(self, path: Path) -> Iterator[Path]:
        """Возвращает список файлов в директории пользователя"""
        self.path_check(path)
        return Path(path).iterdir()

    def create_folders(self, path: Path) -> None:
        """Создание папки в директории пользователя"""
        self.path_check(path)
        for folder in self.get_extension().keys():
            Path(path / folder).mkdir(exist_ok=True, parents=True)

    def is_root_folder_clean(self, path: Path) -> bool:
        """Проверяет отсутствие файлов в директории"""
        for file in self.get_folder(path):
            if (Path(path) / file).is_file():
                return False
        return True

    def _get_target_folder(self, extension: str) -> str:
        """Возвращает название папки"""
        for folder, extensions in self.get_extension().items():
            if extension in extensions:
                return folder + ""
        return "Other"

    def sort_files(self, path: Path) -> dict:
        """Сортирует файлы"""
        logs = {}
        for file in self.get_folder(path):
            src = path / file

            if Path(src).is_dir():
                continue

            target_folder = self._get_target_folder(Path(src).suffix)
            dst = path / target_folder / file.name

            try:
                Path(src).rename(dst)
                logs[file] = Path(dst).name
            except FileExistsError:
                pass

        return logs

    # @staticmethod
    # def remove_empty_folders(path: Path) -> None:
    #     """Удаляет пустые папки в директории пользователя"""
    #     for root, dirs, files in os.walk(path, topdown=False):
    #         for dir_name in dirs:
    #             full_path = os.path.join(root, dir_name)
    #
    #             try:
    #                 if not os.listdir(full_path):
    #                     os.rmdir(full_path)
    #             except FileNotFoundError:
    #                 pass