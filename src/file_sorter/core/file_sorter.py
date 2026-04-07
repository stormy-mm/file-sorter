from pathlib import Path
from typing import Iterator

from file_sorter.common.exceptions import InvalidPathError


class FileSorter:
    """Класс для управления сортировщиком файлов"""

    def __init__(self):
        """Инициализация словаря с названиями директорий и расширениями"""
        self.dict_with_extension = {
            "Images": (".jpg", ".jpeg", ".png", ".svg"),
            "Documents": (".doc", ".docx", ".txt", ".pdf", ".xlsx", ".pptx"),
            "Archives": (".zip", ".gz", ".tar"),
            "Audio": (".mp3", ".ogg", ".wav", ".amr"),
            "Video": (".avi", ".mp4", ".mov", ".mkv"),
            "Other": (),
        }

    @staticmethod
    def path_check(path: Path) -> None:
        """Если файл, то поднимется исключение"""
        if path.is_file():
            raise InvalidPathError

    @staticmethod
    def remove_empty_folders(path: Path) -> None:
        """Удаляет пустые папки в директории пользователя"""
        for root, dirs, files in path.walk(top_down=False):
            for dir_name in dirs:
                try:
                    (root / dir_name).rmdir()
                except OSError:
                    pass

    @staticmethod
    def _get_unique_path(path: Path) -> Path:
        """Проверяет уникальность названия файла"""
        if not path.exists():
            return path

        stem = path.stem
        suffix = path.suffix
        parent = path.parent

        i = 1
        while True:
            new_path = parent / f"{stem}({i}){suffix}"
            if not new_path.exists():
                return new_path
            i += 1

    def get_folder(self, path: Path) -> Iterator[Path]:
        """Возвращает список файлов в директории пользователя"""
        self.path_check(path)
        return path.iterdir()

    def create_folders(self, path: Path) -> None:
        """Создание папки в директории пользователя"""
        self.path_check(path)
        for folder in self.dict_with_extension.keys():
            (path / folder).mkdir(exist_ok=True, parents=True)

    def is_root_folder_clean(self, path: Path) -> bool:
        """Проверяет отсутствие файлов в директории"""
        return "." not in "".join(map(str, self.get_folder(path)))

    def _get_target_folder(self, extension: str) -> str:
        """Возвращает название папки"""
        for folder, extensions in self.dict_with_extension.items():
            if extension in extensions:
                return folder
        return "Other"

    def sort_files(self, path: Path) -> dict[str, Path]:
        """Сортирует файлы"""
        logs = {}
        for file in self.get_folder(path):
            src = path / file

            if src.is_dir():
                continue

            target_folder = self._get_target_folder(file.suffix)
            dst = self._get_unique_path(path / target_folder / file.name)

            src.rename(dst)
            logs[file] = dst.name

        return logs