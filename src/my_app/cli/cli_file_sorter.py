import sys
from src.my_app.common.messages import Messages as Ms
from src.my_app.core.file_sorter import FileSorter


def run(path: str):
    """Запуск программы"""
    file_sort = FileSorter()

    try:
        file_sort.get_folder_user(path)
    except FileNotFoundError:
        return False, {}

    file_sort.create_folder_in_user(path)
    logs = file_sort.sort_files(path)
    file_sort.remove_empty_folders(path)

    return file_sort.is_root_folder_clean(path), logs


def handler(argv):
    """Обработчик команды"""
    if len(argv) != 2:
        sys.stderr.write(Ms.LOG_ERROR)
        sys.exit(1)

    success, logs = run(argv[1])

    if not success:
        sys.stderr.write(Ms.UNSUCCESSFUL_SORTING.format(argv[1]))
        sys.exit(1)

    if not logs:
        sys.stdout.write(Ms.NOTHING_CHANGED)
        sys.exit(0)

    for filename, folder in logs.items():
        sys.stdout.write(Ms.LOG.format(filename, folder))

    sys.stdout.write(Ms.SUCCESSFUL_SORTING)
    sys.exit(0)