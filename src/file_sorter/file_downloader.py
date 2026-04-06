from pathlib import Path
from file_sorter.common.files_folders import FOLDERS, FILES


PATH = Path().cwd() / "../../mess"

Path(PATH).mkdir(exist_ok=True)

# Создание файлов
for file in FILES:
    with open(PATH / file, "a"):
        ...

# Создание подпапок
for folder in FOLDERS:
    Path(PATH / folder).mkdir(exist_ok=True, parents=True)

print("Файлы созданы")