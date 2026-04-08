Сортировщик файлов

Приложение позволяет отсортировать файлы в директории по своим директориям и удаляет пустые

Для начала работы:
### 1) скачивание проекта в tags
```bash
git clone https://github.com/stormy-mm/file-sorter.git
cd file-sorter
```
### 2) Создание виртуального окружения: 
```bash
python -m venv .venv
source .venv/bin/activate
```
### 3) Установка зависимостей
```bash
pip install -r requirements.txt
pip install -e .
```
### 4) Запуск приложения
```bash
python -m file_sorter <your_path>
```
Для загрузки файлов
```bash
python -m file_sorter -l
или python -m file_sorter --load
```
Для получения справки
```bash
python -m file_sorter -h
или python -m file_sorter --help
```
## Запуск тестов

```bash
pytest
```
