import sys
from MESSAGES.messages import Messages as Ms
from DOMENS.file_sorter import run

def handler(argv):
    if len(argv) == 2:
        if run(argv[1]):
            sys.stdout.write(Ms.SUCCESSFUL_SORTING)
            sys.exit(0)
        else:
            sys.stderr.write(Ms.UNSUCCESSFUL_SORTING.format(argv[1]))
            sys.exit(1)
    else:
        sys.stderr.write(Ms.LOG_ERROR)