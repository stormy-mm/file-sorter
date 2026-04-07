import shutil

from pathlib import Path
from file_sorter.common.files_folders import FOLDERS, FILES


def main():
    path = Path().cwd() / "../../mess"

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

    print("Файлы созданы")

if __name__ == "__main__":
    main()