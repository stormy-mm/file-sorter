import shutil
import unittest
import os
from DOMENS.file_sorter import FileSorter, adding_path


PATH = fr"{adding_path(os.getcwd(), "MESS")}"
FILES = ("notes.txt", "report.docx", "vacation.jpg", "archive.zip", "track1.mp3", "my_script.py", "what_the_fuck.wtf")
FOLDERS = (adding_path("old_photos", "family.png"),
           adding_path("new_photos", "special_photos", "python.jpeg"),
           adding_path("new_photos", "hidden_photos", "python313.jpg"))


class TestFileSorter(unittest.TestCase):
    """Тест реализации ядра программы"""

    def setUp(self):
        """
        Подгрузка файлов

        В учебных целях я буду создавать в той же директории, что и вся программа
        """
        os.makedirs(PATH, exist_ok=True)

        # Создание файлов
        for file in FILES:
            with open(adding_path(PATH, file), "a"):
                pass

        # Создание подпапок
        for folder in FOLDERS:
            os.makedirs(adding_path(PATH, folder), exist_ok=True)

        print("Тест начался. Файлы созданы")

    def tearDown(self):
        """Удаление файлов и папок"""
        shutil.rmtree(PATH)
        print("Тест завершился. Файлы подчищены")

    def test_dict_with_extension(self):
        """Тест: наличие словаря с расширениями"""
        self.assertTrue(FileSorter().get_extension())

    def test_can_get_folder_user(self):
        """Тест: можно получить директорию пользователя"""
        self.assertTrue(FileSorter().get_folder_user(PATH))

    def test_ERROR_if_user_input_invalid_path(self):
        """Тест: выбрасывается исключение, если вводится несуществующий путь"""
        with self.assertRaises(FileNotFoundError):
            FileSorter().get_folder_user(adding_path(os.path.split(PATH)[0], "XZ"))

    def test_can_create_folder(self):
        """Тест: папка создаётся без проблем"""
        self.assertTrue(FileSorter().create_folder_in_user(PATH))

    def test_file_with_extension_in_user_folder(self):
        """Тест: проверяет наличие файлов в директории пользователя ПЕРЕД сортировкой"""
        self.assertFalse(FileSorter().checker_files_in_folder_user(PATH))

    def test_sort_is_True(self):
        """Тест: сортировка прошла успешно"""
        FileSorter().create_folder_in_user(PATH)
        self.assertTrue(FileSorter().sort_files(PATH))

    def test_file_with_extension_in_the_correct_folder(self):
        """Тест: файл ПОСЛЕ сортировки находится в правильной папке"""
        FileSorter().create_folder_in_user(PATH)
        FileSorter().sort_files(PATH)
        self.assertIn(FILES[0], os.listdir(adding_path(PATH, "Documents"))) # notes.txt
        self.assertIn(FILES[4], os.listdir(adding_path(PATH, "Audio"))) # track1.mp3

    def test_file_with_extension_in_not_user_folder(self):
        """Тест: проверяет наличие файлов в директории пользователя ПОСЛЕ сортировки"""
        fs = FileSorter()
        fs.create_folder_in_user(PATH)
        fs.sort_files(PATH)
        self.assertTrue(fs.checker_files_in_folder_user(PATH))