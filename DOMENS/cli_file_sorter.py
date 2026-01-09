import sys
from MESSAGES.messages import Messages as Ms
from DOMENS.file_sorter import FileSorter


def run(path: str):
    """Запуск программы"""
    FILE_SORT = FileSorter()

    try:
        FILE_SORT.get_folder_user(path)
    except FileNotFoundError:
        return False, {}

    FILE_SORT.create_folder_in_user(path)
    logs = FILE_SORT.sort_files(path)
    FILE_SORT.remove_empty_folders(path)

    return FILE_SORT.is_root_folder_clean(path), logs


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