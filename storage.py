import json
from typing import List
from models import Book


class Storage:
    """Класс для работы с JSON-хранилищем."""

    def __init__(self, filepath: str):
        """
        Инициализация объекта Storage.
        :param filepath: Путь к файлу JSON.
        """
        self.filepath: str = filepath

    def load_books(self) -> List[Book]:
        """Загрузить книги из файла."""
        try:
            with open(self.filepath, "r", encoding="utf-8") as file:
                return [Book.from_dict(book) for book in json.load(file)]
        except FileNotFoundError:
            return []

    def save_books(self, books: List[Book]) -> None:
        """Сохранить книги в файл."""
        with open(self.filepath, "w", encoding="utf-8") as file:
            json.dump([book.to_dict() for book in books],
                      file, ensure_ascii=False, indent=4)
