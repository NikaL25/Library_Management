from typing import List
from models import Book
from storage import Storage


class Library:
    """Класс для управления библиотекой книг."""

    def __init__(self, filepath: str = "library.json"):
        """
        Инициализация библиотеки.
        :param filepath: Путь к файлу для хранения данных.
        """
        self.storage = Storage(filepath)
        self.books: List[Book] = self.storage.load_books()

    def list_books(self) -> None:
        """Вывести список всех книг."""
        if not self.books:
            print("Библиотека пуста.")
            return
        print(f"Всего книг: {len(self.books)}")
        for book in self.books:
            print(book.to_dict())

    def add_book(self, title: str, author: str, year: int) -> None:
        """Добавить книгу в библиотеку."""
        new_book = Book(title, author, year)
        self.books.append(new_book)
        self.storage.save_books(self.books)
        print(f"Книга добавлена: {new_book.to_dict()}")

    def remove_book(self, book_id: str) -> None:
        """Удалить книгу по ID."""
        book = next((b for b in self.books if b.id == book_id), None)
        if not book:
            print("Книга с таким ID не найдена.")
            return
        self.books.remove(book)
        self.storage.save_books(self.books)
        print(f"Книга удалена: {book.to_dict()}")

    def search_books(self, query: str, field: str = "title") -> None:
        """Найти книги по указанному полю."""
        if field not in ["title", "author", "year"]:
            print("Некорректное поле для поиска. Используйте title, author или year.")
            return
        results = [book for book in self.books if query.lower() in str(
            getattr(book, field)).lower()]
        print(f"Найдено {len(results)} книг:")
        for book in results:
            print(book.to_dict())

    def update_status(self, book_id: str, status: str) -> None:
        """Изменить статус книги."""
        if status not in ["в наличии", "выдана"]:
            print("Недопустимый статус. Используйте 'в наличии' или 'выдана'.")
            return
        book = next((b for b in self.books if b.id == book_id), None)
        if not book:
            print("Книга с таким ID не найдена.")
            return
        book.status = status
        self.storage.save_books(self.books)
        print(f"Статус книги обновлен: {book.to_dict()}")
