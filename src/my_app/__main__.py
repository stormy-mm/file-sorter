import sys
from src.my_app.cli.cli_file_sorter import handler

def main():
    """Главная функция"""
    handler(sys.argv)

if __name__ == "__main__":
    main()