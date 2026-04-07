import sys

from ..common.messages import Messages as Ms
from .functions import run, load


def st_and_message(soo, mode=0):
    """Выводит в терминал сообщение и завершает работу с кодом"""
    sys.stdout.write(soo) if mode == 0 else sys.stderr.write(soo)
    sys.exit(mode)


def handler(argv):
    """Обработчик команды"""
    if len(argv) != 2:
        st_and_message(Ms.LOG_ERROR, 1)

    match argv[1]:
        case "-l" | "--load":
            st_and_message(Ms.FILES_LOADS.format(load()))
        case "-h" | "--help":
            st_and_message(Ms.HELP)

    try:
        success, logs = run(argv[1])
    except FileNotFoundError:
        st_and_message(Ms.UNFOUND_PATH.format(argv[1]), 1)

    if not success:
        st_and_message(Ms.ERROR)

    if not logs:
        st_and_message(Ms.NOTHING_CHANGED)

    for filename, folder in logs.items():
        sys.stdout.write(Ms.LOG.format(filename, folder))
    st_and_message(Ms.SUCCESSFUL_SORTING)