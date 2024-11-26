from library import Library

def main() -> None:
    """Главная функция для запуска приложения."""
    library = Library("library.json")

    while True:
        print("\nДоступные команды:")
        print("1. Показать все книги")
        print("2. Добавить книгу")
        print("3. Удалить книгу")
        print("4. Найти книгу")
        print("5. Изменить статус книги")
        print("6. Выход")
        choice = input("Введите номер команды: ")

        try:
            if choice == "1":
                library.list_books()
            elif choice == "2":
                title = input("Введите название книги: ")
                author = input("Введите автора книги: ")
                year = int(input("Введите год издания книги: "))
                library.add_book(title, author, year)
            elif choice == "3":
                book_id = input("Введите ID книги для удаления: ")
                library.remove_book(book_id)
            elif choice == "4":
                query = input("Введите строку для поиска: ")
                field = input("Введите поле для поиска (title, author, year): ")
                library.search_books(query, field)
            elif choice == "5":
                book_id = input("Введите ID книги для обновления статуса: ")
                status = input("Введите новый статус ('в наличии' или 'выдана'): ")
                library.update_status(book_id, status)
            elif choice == "6":
                print("Выход из программы.")
                break
            else:
                print("Некорректная команда. Попробуйте еще раз.")
        except ValueError as e:
            print(f"Ошибка ввода: {e}")
        except Exception as e:
            print(f"Неожиданная ошибка: {e}")


if __name__ == "__main__":
    main()
