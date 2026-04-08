"""Файл с загрузочными файлами и директориями"""
from pathlib import Path

FILES = (
    "notes.txt",
    "report.docx",
    "vacation.jpg",
    "archive.zip",
    "track1.mp3",
    "my_script.py",
    "what_the_fuck.wtf",
)
FOLDERS = (
    Path("old_photos", "family.png"),
    Path("new_photos", "special_photos", "python.jpeg"),
    Path("new_photos", "hidden_photos", "python313.jpg"),
)