from typing import Iterator

from pytest import fixture, raises

from file_sorter.core.file_sorter import FileSorter
from file_sorter.common.exceptions import InvalidPathError
from file_sorter.common.files_folders import FOLDERS, FILES


class TestFileSorter:
    """Тест реализации ядра программы"""

    @fixture
    def setup(self, tmp_path):
        """
        Подгрузка файлов

        В учебных целях я буду создавать в той же директории, что и вся программа
        """
        self.fs = FileSorter()
        self.path = tmp_path
        # Создание файлов
        for file in FILES:
            with open(self.path / file, "a"):
                pass

        # Создание подпапок
        for folder in FOLDERS:
            (self.path / folder).mkdir(exist_ok=True, parents=True)

    @fixture
    def load_sort(self):
        """Сортировка файлов для тестов"""
        self.fs.create_folders(self.path)
        self.fs.sort_files(self.path)
        self.fs.remove_empty_folders(self.path)

    @fixture
    def file_path(self):
        """Создаёт файл"""
        file_path = self.path / "notes.txt"
        file_path.touch()
        return file_path

    def test_valid_path_is_correct(self, setup):
        """Тест: введённый путь корректен: исключение не поднимается"""
        self.fs.path_check(self.path)

    def test_invalid_path_is_not_correct(self, setup, file_path):
        """Тест: введённый путь с файлом некорректен"""
        with raises(InvalidPathError):
            self.fs.path_check(file_path)

    def test_path_is_not_str(self, setup):
        """Тест: ошибка при строке, где ожидается Path(str)"""
        with raises(AttributeError):
            self.fs.path_check(str(self.path))

    def test_can_get_folder(self, setup):
        """Тест: можно получить содержимое директории"""
        assert isinstance(self.fs.get_folder(self.path), Iterator)

    def test_error_if_invalid_path(self, setup):
        """Тест: выбрасывается исключение при несуществующем путе"""
        with raises(FileNotFoundError):
            self.fs.get_folder(self.path / "test")

    def test_can_create_folder(self, setup):
        """Тест: папка создаётся без проблем"""
        self.fs.create_folders(self.path)
        assert (self.path / "Documents").exists()
        assert (self.path / "Other").exists()

    def test_cannot_create_folder_if_file(self, setup, file_path):
        """Тест: ошибка при путе к файлу"""
        with raises(InvalidPathError):
            self.fs.create_folders(file_path)

    def test_file_with_extension_in_the_correct_folder(self, setup, load_sort):
        """Тест: файл после сортировки находится в правильной папке"""
        assert (self.path / r"Documents\notes.txt").exists()
        assert (self.path / r"Audio\track1.mp3").exists()

    def test_file_with_extension_in_not_user_folder(self, setup, load_sort):
        """Тест: в директории нет файлов после сортировки"""
        assert self.fs.is_root_folder_clean(self.path)

    def test_if_is_file_then_false(self, setup, load_sort, file_path):
        """Тест: если после сортировки остался файл, то False"""
        assert not self.fs.is_root_folder_clean(self.path)

    def test_adds_incremented_suffix_when_file_name_conflicts(self, setup, load_sort, file_path):
        """Тест: если после сортировки создать файл с таким же названием в корневой папке и сортировать, то новому файлу
        прибавляется номер"""
        self.fs.sort_files(self.path) # повторная сортировка
        assert (self.path / r"Documents\notes(1).txt").exists()