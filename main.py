"""Модуль для работы с интернет-магазином."""

from abc import ABC, abstractmethod


class ReprMixin:
    """Миксин для красивого repr представления."""

    def __repr__(self):
        attrs = []
        for key, value in self.__dict__.items():
            attrs.append(f"{key}={value!r}")
        return f"{self.__class__.__name__}({', '.join(attrs)})"


class BaseProduct(ABC):
    """Абстрактный базовый класс для товаров."""

    @abstractmethod
    def __init__(self, name, description, price, quantity):
        pass


class ZeroQuantityError(ValueError):
    """Исключение для товаров с нулевым количеством."""

    pass


class Product(BaseProduct, ReprMixin):
    """Класс для представления товара."""

    def __init__(self, name, description, price, quantity):
        """Инициализация товара."""
        if quantity == 0:
            msg = "Товар с нулевым количеством не может быть добавлен"
            raise ZeroQuantityError(msg)
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут
        self.quantity = quantity

    @property
    def price(self):
        """Геттер для цены."""
        return self.__price

    @price.setter
    def price(self, value):
        """Сеттер для цены с проверкой."""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = value

    def __str__(self):
        """Строковое представление товара."""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Сложение товаров."""
        if isinstance(self, type(other)):
            total = self.__price * self.quantity + other.__price * other.quantity
            return total
        raise TypeError("Можно складывать только товары одного типа")

    @classmethod
    def new_product(cls, product_data, products_list=None):
        """Создает товар из словаря."""
        required = ['name', 'description', 'price', 'quantity']
        for field in required:
            if field not in product_data:
                raise ValueError(f"Отсутствует поле: {field}")
        if products_list:
            for existing in products_list:
                if existing.name == product_data['name']:
                    existing.quantity += product_data['quantity']
                    if product_data['price'] > existing.price:
                        existing.price = product_data['price']
                    return existing

        return cls(
            name=product_data['name'],
            description=product_data['description'],
            price=product_data['price'],
            quantity=product_data['quantity']
        )


class Smartphone(Product):
    """Класс для представления смартфона."""

    def __init__(self, name, description, price, quantity,
                 efficiency, model, memory, color):
        """Инициализация смартфона."""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        """Строковое представление смартфона."""
        return (f"{self.name} ({self.model}), {self.price} руб. "
                f"Остаток: {self.quantity} шт. Память: {self.memory}ГБ")


class LawnGrass(Product):
    """Класс для представления газонной травы."""

    def __init__(self, name, description, price, quantity,
                 country, germination_period, color):
        """Инициализация газонной травы."""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        """Строковое представление газонной травы."""
        return (f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт. "
                f"Страна: {self.country}, Прорастание: {self.germination_period} дней")


class Category:
    """Класс для представления категории товаров."""

    category_count = 0
    product_count = 0

    def __init__(self, name, description):
        """Инициализация категории."""
        self.name = name
        self.description = description
        self.__products = []
        Category.category_count += 1

    def add_product(self, product):
        """Добавление товара в категорию."""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только товары")
        self.__products.append(product)
        Category.product_count += 1

    def average_price(self):
        """Расчет средней цены товаров в категории."""
        try:
            total = sum(p.price for p in self.__products)
            return total / len(self.__products)
        except ZeroDivisionError:
            return 0.0

    @property
    def products(self):
        """Геттер для строкового представления товаров."""
        return "\n".join(str(p) for p in self.__products)

    def __str__(self):
        """Строковое представление категории."""
        total = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total} шт."

    def __repr__(self):
        """Представление для отладки."""
        return f"Category('{self.name}', '{self.description}')"


if __name__ == "__main__":
    print("✅ Модуль main.py успешно загружен")
    print("Доступные классы: Product, Smartphone, LawnGrass, Category, ZeroQuantityError")
