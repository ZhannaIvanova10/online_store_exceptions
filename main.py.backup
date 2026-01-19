"""
Модуль для работы с интернет-магазином.
Реализует классы Product и Category с обработкой исключений.
"""


class ZeroQuantityError(ValueError):
    """Пользовательское исключение для товаров с нулевым количеством"""
    pass


class Product:
    """Класс для представления товара в магазине"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализация товара.

        Args:
            name: Название товара
            description: Описание товара
            price: Цена товара
            quantity: Количество товара в наличии

        Raises:
            ZeroQuantityError: Если quantity == 0
        """
        if quantity == 0:
            raise ZeroQuantityError("Товар с нулевым количеством не может быть добавлен")
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        """Строковое представление товара"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __repr__(self):
        """Представление для отладки"""
        return f"Product('{self.name}', '{self.description}', {self.price}, {self.quantity})"


class Category:
    """Класс для представления категории товаров"""

    category_count = 0  # Атрибут класса: счетчик категорий
    product_count = 0   # Атрибут класса: счетчик товаров

    def __init__(self, name: str, description: str):
        """Инициализация категории"""
        self.name = name
        self.description = description
        self.__products = []  # Приватный атрибут для списка товаров

        Category.category_count += 1

    def add_product(self, product: Product):
        """
        Добавление товара в категорию.

        Args:
            product: Объект класса Product
        """
        self.__products.append(product)
        Category.product_count += 1

    def average_price(self) -> float:
        """
        Расчет средней цены товаров в категории.

        Returns:
            Средняя цена товаров или 0, если товаров нет
        """
        try:
            # Используем обращение к приватному атрибуту
            total_price = sum(product.price for product in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0.0

    @property
    def products(self):
        """Геттер для получения строкового представления товаров"""
        result = ""
        for product in self.__products:
            result += str(product) + "\n"
        return result.rstrip()  # Убираем последний перевод строки

    def __str__(self):
        """Строковое представление категории"""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __repr__(self):
        """Представление для отладки"""
        return f"Category('{self.name}', '{self.description}')"


# Добавим простой тест для проверки импорта
if __name__ == "__main__":
    print("✅ Модуль main.py успешно загружен")
    print("Доступные классы: Product, Category, ZeroQuantityError")
