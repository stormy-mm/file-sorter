import shutil
from pathlib import Path

from ..core.file_sorter import FileSorter
from ..common.files_folders import FOLDERS, FILES


def load() -> Path:
    """
    Загружает файлы для тестов

    Я решил пренебречь стилизацией расположений модулей по своим директориям ссылаясь на то, что этой функции место
    больше тут по смыслу
    """
    path = Path().cwd() / "mess"

    if path.exists():
        shutil.rmtree(path)

    path.mkdir(exist_ok=True)

    # Создание файлов
    for file in FILES:
        with open(path / file, "a"):
            pass

    # Создание подпапок
    for folder in FOLDERS:
        (path / folder).mkdir(exist_ok=True, parents=True)

    return path


def run(path_: str) -> tuple[bool, dict]:
    """Запуск программы"""
    path = Path(path_)
    fs = FileSorter()

    # если такого пути не существует, то поднимется исключение
    fs.get_folder(path)
    fs.create_folders(path)
    logs = fs.sort_files(path)
    fs.remove_empty_folders(path)

    return fs.is_root_folder_clean(path), logs


