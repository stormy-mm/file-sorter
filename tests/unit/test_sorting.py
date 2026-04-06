from pathlib import Path
from typing import Iterator

from pytest import fixture, raises

from my_app.common.exceptions import InvalidPathError
from my_app.core.file_sorter import FileSorter
from my_app.common.files_folders import FOLDERS, FILES


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
            with open(self.path / file, "a"):
                pass

        # Создание подпапок
        for folder in FOLDERS:
            Path(self.path / folder).mkdir(exist_ok=True, parents=True)

    def test_valid_path_is_correct(self, setup):
        """Тест: введённый путь корректен: исключение не поднимается"""
        self.filesorter.path_check(self.path)

    def test_invalid_path_is_not_correct(self, setup):
        """Тест: введённый путь с расширением на конце некорректен"""
        with raises(InvalidPathError):
            self.filesorter.path_check(self.path / "test.txt")

    def test_can_get_folder_user(self, setup):
        """Тест: можно получить содержимое директории пользователя"""
        assert isinstance(self.filesorter.get_folder(self.path), Iterator)

    def test_error_if_user_input_invalid_path(self, setup):
        """Тест: выбрасывается исключение, если вводится несуществующий путь"""
        with raises(FileNotFoundError):
            self.filesorter.get_folder(self.path / "test")

    def test_can_create_folder(self, setup):
        """Тест: папка создаётся без проблем"""
        self.filesorter.create_folders(self.path)
        assert (self.path / "Documents").exists()
        assert (self.path / "Other").exists()

    def test_cannot_create_folder_if_user_input_file(self, setup):
        """Тест: ошибка, если пользователь введёт путь к файлу"""
        with raises(InvalidPathError):
            self.filesorter.create_folders(self.path / "test.txt")

    def test_file_with_extension_in_the_correct_folder(self, setup):
        """Тест: файл после сортировки находится в правильной папке"""
        self.filesorter.create_folders(self.path)
        self.filesorter.sort_files(self.path)
        assert (self.path / r"Documents\notes.txt").exists()
        assert (self.path / r"Audio\track1.mp3").exists()

    def test_file_with_extension_in_not_user_folder(self, setup):
        """Тест: в директории пользователя нет файлов после сортировки"""
        self.filesorter.create_folders(self.path)
        self.filesorter.sort_files(self.path)
        assert self.filesorter.is_root_folder_clean(self.path)