from pathlib import Path
from file_sorter.common.files_folders import FOLDERS, FILES


PATH = Path().cwd() / "../../mess"

PATH.mkdir(exist_ok=True)

# Создание файлов
for file in FILES:
    with open(PATH / file, "a"):
        pass

# Создание подпапок
for folder in FOLDERS:
    (PATH / folder).mkdir(exist_ok=True, parents=True)

print("Файлы созданы")