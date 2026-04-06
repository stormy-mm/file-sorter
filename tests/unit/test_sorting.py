import os

from pytest import fixture, raises

from my_app.common.exceptions import InvalidPathError
from my_app.core.file_sorter import FileSorter, adding_path


FILES = ("notes.txt", "report.docx", "vacation.jpg", "archive.zip", "track1.mp3", "my_script.py", "what_the_fuck.wtf")
FOLDERS = (adding_path("old_photos", "family.png"),
           adding_path("new_photos", "special_photos", "python.jpeg"),
           adding_path("new_photos", "hidden_photos", "python313.jpg"))


class TestFileSorter:
    """Тест реализации ядра программы"""

    @fixture
    def setup(self, tmp_path):
        """
        Подгрузка файлов

        В учебных целях я буду создавать в той же директории, что и вся программа
        """
        self.filesorter = FileSorter()
        self.path = tmp_path
        # Создание файлов
        for file in FILES:
            with open(adding_path(self.path, file), "a"):
                pass

        # Создание подпапок
        for folder in FOLDERS:
            os.makedirs(adding_path(self.path, folder), exist_ok=True)

    def test_can_get_folder_user(self, setup):
        """Тест: можно получить директорию пользователя"""
        assert self.filesorter.get_folder(self.path)

    def test_error_if_user_input_invalid_path(self, setup):
        """Тест: выбрасывается исключение, если вводится несуществующий путь"""
        with raises(FileNotFoundError):
            self.filesorter.get_folder(adding_path(os.path.split(self.path)[0], "XZ"))

    def test_can_create_folder(self, setup):
        """Тест: папка создаётся без проблем"""
        assert self.filesorter.create_folder(self.path)

    def test_cannot_create_folder_if_user_input_file(self, setup):
        """Тест: ошибка, если пользователь введёт путь к файлу"""
        with raises(InvalidPathError):
            self.filesorter.create_folder(self.path / "test.txt")

    def test_file_with_extension_in_the_correct_folder(self, setup):
        """Тест: файл после сортировки находится в правильной папке"""
        self.filesorter.create_folder(self.path)
        self.filesorter.sort_files(self.path)
        assert FILES[0] in os.listdir(adding_path(self.path, "Documents")) # notes.txt
        assert FILES[4] in os.listdir(adding_path(self.path, "Audio")) # track1.mp3

    def test_file_with_extension_in_not_user_folder(self, setup):
        """Тест: в директории пользователя нет файлов после сортировки"""
        self.filesorter.create_folder(self.path)
        self.filesorter.sort_files(self.path)
        assert self.filesorter.is_root_folder_clean(self.path)