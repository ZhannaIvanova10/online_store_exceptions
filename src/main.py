"""
Полная реализация всех ДЗ (14-17) с обработкой исключений
"""
from abc import ABC, abstractmethod
from typing import Union


class ReprMixin:
    """Миксин для единообразного repr"""
    def __repr__(self):
        params = ', '.join(f"{k}={v!r}" for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}({params})"


class ZeroQuantityError(ValueError):
    """Исключение для товара с нулевым количеством (ДЗ 17.1)"""
    def __init__(self, message="Товар с нулевым количеством не может быть добавлен"):
        super().__init__(message)


class BaseProduct(ABC):
    """Абстрактный базовый класс товара (ДЗ 16.2)"""
    product_count = 0
    
    @abstractmethod
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        BaseProduct.product_count += 1
    @abstractmethod
    def __str__(self):
        pass
    
    @abstractmethod
    def __add__(self, other):
        pass


class Product(BaseProduct, ReprMixin):
    """Класс товара (ДЗ 14.1, 15.1)"""
    
    def __init__(self, name, description, price, quantity):
        # ДЗ 17.1: Проверка нулевого количества
        if quantity == 0:
            raise ZeroQuantityError()
        
        super().__init__(name, description, price, quantity)
    
    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."
    
    def __add__(self, other: 'Product') -> 'Product':
        # ДЗ 15.1: Сложение товаров
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только товары одного класса")
        if type(self) != type(other):
            raise TypeError("Можно складывать только товары одного типа")
        
        total_price = (self.price * self.quantity) + (other.price * other.quantity)
        total_quantity = self.quantity + other.quantity

        # Возвращаем товар того же типа
        if isinstance(self, Smartphone):
            return Smartphone(
                name=self.name,
                description=self.description,
                price=total_price / total_quantity if total_quantity > 0 else 0,
                quantity=total_quantity,
                performance=self.performance,
                model=self.model,
                memory=self.memory,
                color=self.color
            )
        elif isinstance(self, LawnGrass):
            return LawnGrass(
                name=self.name,
                description=self.description,
                price=total_price / total_quantity if total_quantity > 0 else 0,
                quantity=total_quantity,
                country=self.country,
                germination_period=self.germination_period,
                color=self.color
            )
        else:
            return Product(
                name=self.name,
                description=self.description,
                price=total_price / total_quantity if total_quantity > 0 else 0,
                quantity=total_quantity
            )

class Smartphone(Product, ReprMixin):
    """Класс смартфона (ДЗ 16.1)"""
    def __init__(self, name, description, price, quantity, 
                 performance, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color
    
    def __str__(self):
        return f"{self.name} ({self.model}), {self.price} руб. Остаток: {self.quantity} шт."


class LawnGrass(Product, ReprMixin):
    """Класс газонной травы (ДЗ 16.1)"""
    def __init__(self, name, description, price, quantity,
                 country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
    
    def __str__(self):
        # ИСПРАВЛЕНИЕ: "из России" вместо "из России"
        return f"{self.name} из {self.country}, {self.price} руб. Остаток: {self.quantity} шт."


class Category:
    """Класс категории (ДЗ 14.1, 17.1)"""
    category_count = 0
    product_count = 0
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__products = []
        Category.category_count += 1
    
    @property
    def products(self):
        return self.__products
    
    def add_product(self, product):
        # ДЗ 17.1: Проверка перед добавлением
        if product.quantity == 0:
            raise ZeroQuantityError(f"Товар {product.name} имеет нулевое количество")
        self.__products.append(product)
        Category.product_count += 1
    
    @classmethod
    def new_product(cls, name, description, price, quantity):
        """Класс-метод создания товара (ДЗ 14.2)"""
        return Product(name, description, price, quantity)
    
    def average_price(self):
        """Метод подсчета средней цены (ДЗ 17.1)"""
        try:
            total = sum(product.price for product in self.__products)
            return total / len(self.__products)
        except ZeroDivisionError:
            return 0.0
    def __str__(self):
        products_str = "\n".join(str(p) for p in self.__products)
        return f"{self.name}, количество продуктов: {len(self.__products)} шт.\n{products_str}"
    
    def __repr__(self):
        return f"Category(name={self.name!r}, description={self.description!r}, products_count={len(self.__products)})"
