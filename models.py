import uuid
from typing import Dict


class Book:
    """Класс, представляющий книгу."""

    def __init__(self, title: str, author: str, year: int, status: str = "в наличии"):
        """
        Инициализация объекта книги.
        :param title: Название книги.
        :param author: Автор книги.
        :param year: Год издания книги.
        :param status: Статус книги (по умолчанию "в наличии").
        """
        self.id: str = str(uuid.uuid4())  # Уникальный идентификатор
        self.title: str = title
        self.author: str = author
        self.year: int = year
        self.status: str = status

    def to_dict(self) -> Dict:
        """
        Преобразовать объект книги в словарь.
        :return: Словарь, представляющий книгу.
        """
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }

    @staticmethod
    def from_dict(data: Dict) -> 'Book':
        """
        Создать объект книги из словаря.
        :param data: Словарь с данными о книге.
        :return: Объект Book.
        """
        book = Book(data["title"], data["author"], data["year"], data["status"])
        book.id = data["id"]
        return book
