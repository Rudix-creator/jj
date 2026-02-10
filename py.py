from abc import ABC, abstractmethod


class Human(ABC):
    def __init__(self, full_name):
        self.__full_name = full_name
    
    def get_full_name(self):
        return self.__full_name
    
    @abstractmethod
    def role(self):
        pass


class Worker(Human):
    def role(self):
        return "Сотрудник"


class Librarian(Worker):
    def role(self):
        return "Библиотекарь"


class Client(Human):
    def role(self):
        return "Читатель"


class Item:
    def __init__(self, book_title, book_author):
        self.__book_title = book_title
        self.__book_author = book_author
        self.__is_free = True
    
    def get_book_title(self):
        return self.__book_title
    
    def get_book_author(self):
        return self.__book_author
    
    def get_status(self):
        return self.__is_free
    
    def mark_as_taken(self):
        if self.__is_free:
            self.__is_free = False
            return True
        return False
    
    def mark_as_returned(self):
        self.__is_free = True
    
    def display_info(self):
        state = "доступна" if self.__is_free else "выдана"
        return f"{self.__book_title} - {self.__book_author} ({state})"


class Library:
    def __init__(self):
        self.__librarian = Librarian("Тим")
        self.__collection = []
        self.__registry = []
        self.__authorized = False
        
        self.__collection.append(Item("Герой нашего времени", "М. Ю. Лермонтов"))
        self.__collection.append(Item("Преступление и наказание", "Ф. Достоевский"))
        self.__registry.append(Client("Иван"))
    
    def enter_system(self, provided_name):
        if provided_name == self.__librarian.get_full_name():
            self.__authorized = True
            return True
        return False
    
    def leave_system(self):
        self.__authorized = False
    
    def include_item(self, book_title, book_author):
        self.__collection.append(Item(book_title, book_author))
        print("Книга добавлена")
    
    def exclude_item(self, book_title):
        search_title = book_title.lower()
        for item in self.__collection:
            if item.get_book_title().lower() == search_title:
                if not item.get_status():
                    print("Невозможно удалить: книга выдана читателю")
                    return
                self.__collection.remove(item)
                print("Книга удалена")
                return
        print("Книга не найдена в каталоге")
    
    def enroll_client(self, client_name):
        search_name = client_name.lower()
        for client in self.__registry:
            if client.get_full_name().lower() == search_name:
                print("Читатель с таким именем уже зарегистрирован")
                return
        self.__registry.append(Client(client_name))
        print("Читатель зарегистрирован")
    
    def show_registry(self):
        if not self.__registry:
            print("Реестр читателей пуст")
            return
        print("Реестр читателей:")
        for client in self.__registry:
            print(f"- {client.get_full_name()} ({client.role()})")
    
    def show_collection(self):
        if not self.__collection:
            print("Коллекция книг пуста")
            return
        print("Коллекция книг:")
        for item in self.__collection:
            print(f"- {item.display_info()}")
    
    def run(self):
        print("Библиотека")
        
        while True:
            if not self.__authorized:
                print("\nГлавное меню:")
                print("1. Авторизация библиотекаря")
                print("2. Завершение работы")
                option = input("Выбор: ")
                
                if option == "1":
                    name_input = input("Введите имя библиотекаря: ")
                    if self.enter_system(name_input):
                        print("Авторизация успешна")
                    else:
                        print("Авторизация не удалась")
                elif option == "2":
                    print("Работа завершена")
                    break
                else:
                    print("Некорректный выбор")
            else:
                print("\nМеню библиотекаря:")
                print("1. Внести новую книгу")
                print("2. Исключить книгу")
                print("3. Зарегистрировать читателя")
                print("4. Показать реестр читателей")
                print("5. Показать коллекцию книг")
                print("6. Завершить сеанс")
                option = input("Выбор: ")
                
                if option == "1":
                    title = input("Название книги: ")
                    author = input("Автор: ")
                    self.include_item(title, author)
                elif option == "2":
                    title = input("Название книги для исключения: ")
                    self.exclude_item(title)
                elif option == "3":
                    name = input("Имя читателя: ")
                    self.enroll_client(name)
                elif option == "4":
                    self.show_registry()
                elif option == "5":
                    self.show_collection()
                elif option == "6":
                    self.leave_system()
                    print("Сеанс завершён")
                else:
                    print("Некорректный выбор")


Library().run()