import shutil
from pathlib import Path

from ..core.file_sorter import FileSorter
from ..common.files_folders import FILES, FOLDERS


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

    for file in FILES:
        (path / file).touch()

    for folder in FOLDERS:
        (path / folder).parent.mkdir(exist_ok=True, parents=True)
        (path / folder).touch()

    return path


def run(path: str) -> tuple[bool, dict]:
    """Запуск программы"""
    fs = FileSorter(Path(path))

    fs.create_folders()
    logs = fs.sort_files()
    fs.remove_empty_folders()

    return fs.is_root_folder_clean(), logs