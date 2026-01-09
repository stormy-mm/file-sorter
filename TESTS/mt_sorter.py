import unittest
import os
# from DOMENS.file_sorter import FileSorter

DIR = "MESS"
FILES = ("notes.txt", "report.docx", "vacation.jpg", "archive.zip", "track1.mp3", "my_script.py")
FOLDERS = (os.path.join("old_photos", "family.png"), os.path.join("new_photos", "python.png"))

# Создание директории с файлами
os.chdir("..")  # выход из TESTS
print(os.getcwd())
# os.makedirs(DIR, exist_ok=True)
#
# # Создание файлов
# for file in FILES:
#     open(os.path.join(DIR, file), "w")
#
# # Создание подпапок
# for folder in FOLDERS:
#     os.makedirs(os.path.join(DIR, folder), exist_ok=True)

#
# class TestFileSorter(unittest.TestCase):
#     """Тест реализации ядра программы"""
#
#     def setUp(self):
#         """
#         Подгрузка файлов
#
#         В учебных целях я буду создавать в той же директории, что и вся программа
#         """
#
#
#
#         # Работа завершена. Возвращаемся в TESTS
#         # os.chdir("TESTS")
#
#     # def tearDown(self):
#     #     """Удаление файлов"""
#     #     for file in FILES:
#     #         os.remove(os.path.join(DIR, file))
