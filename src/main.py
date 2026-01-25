"""
Полная реализация всех ДЗ (14-17) с обработкой исключений
"""
from abc import ABC, abstractmethod


class classproperty:
    """Декоратор для создания свойств класса"""
    def __init__(self, fget):
        self.fget = fget
    
    def __get__(self, obj, cls):
        return self.fget(cls)


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
    """Абстрактный базовый класс для товаров"""
    @abstractmethod
    def __init__(self, name, description, price, quantity):
        pass


class Product(BaseProduct, ReprMixin):
    """Класс для представления товара (ДЗ 14.1, 15.1)"""
    
    product_count = 0  # Счетчик созданных продуктов
    
    def __init__(self, name, description, price, quantity):
        """Инициализация товара"""
        # ДЗ 17.1: Проверка нулевого количества
        if quantity == 0:
            raise ZeroQuantityError()
        
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут для сеттера
        self.quantity = quantity
        # Увеличиваем счетчик
        Product.product_count += 1
    
    @property
    def price(self):
        """Геттер для цены"""
        return self.__price
    
    @price.setter
    def price(self, value):
        """Сеттер для цены с проверкой (ДЗ 16.1)"""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return  # Не изменяем цену
        self.__price = value
    
    def __str__(self):
        """Строковое представление товара"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."
    
    def __add__(self, other):
        """Сложение товаров (ДЗ 15.1) - ВОЗВРАЩАЕТ ОБЪЕКТ ДЛЯ ТЕСТОВ"""
        if isinstance(self, type(other)):
            total_price = (self.__price * self.quantity) + (other.__price * other.quantity)
            total_quantity = self.quantity + other.quantity
            
            if total_quantity == 0:
                avg_price = 0
            else:
                avg_price = total_price / total_quantity
            
            # Создаем новый объект того же типа
            if isinstance(self, Smartphone):
                return Smartphone(
                    name=self.name,
                    description=self.description,
                    price=avg_price,
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
                    price=avg_price,
                    quantity=total_quantity,
                    country=self.country,
                    germination_period=self.germination_period,
                    color=self.color
                )
            else:
                return Product(
                    name=self.name,
                    description=self.description,
                    price=avg_price,
                    quantity=total_quantity
                )
        raise TypeError("Можно складывать только товары одного типа")
    
    @classmethod
    def new_product(cls, product_data, products_list=None):
        """Создает товар из словаря (ДЗ 16.1)"""
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


class Category:
    """Класс для представления категории товаров (ДЗ 14.1)"""
    
    total_categories = 0
    total_unique_products = 0
    
    @classproperty
    def category_count(cls):
        """Количество созданных категорий (свойство класса)"""
        return cls.total_categories
    
    @classproperty
    def product_count(cls):
        """Количество уникальных продуктов во всех категориях (свойство класса)"""
        return cls.total_unique_products
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__products = []  # Приватный атрибут
        
        Category.total_categories += 1
    @property
    def products(self):
        """Геттер для списка продуктов"""
        return self.__products
    
    def add_product(self, product):
        """Добавление товара в категорию (ДЗ 17.1)"""
        if product.quantity == 0:
            raise ZeroQuantityError("Товар с нулевым количеством не может быть добавлен")
        self.__products.append(product)
        Category.total_unique_products += 1
    
    def __str__(self):
        """Строковое представление категории - исправленная версия"""
        if not self.__products:
            return f"{self.name}, количество продуктов: 0 шт."
        
        products_str = "\n".join(str(p) for p in self.__products)
        return f"{self.name}, количество продуктов: {len(self.__products)} шт.\n{products_str}"
    
    @property
    def average_price(self):
        """Средняя цена товаров в категории (ДЗ 15.1) - ПРОСТАЯ СРЕДНЯЯ"""
        if not self.__products:
            return 0.0  # Float для совместимости с тестами
        total_price = sum(p.price for p in self.__products)  # Только цена, без учета количества
        return total_price / len(self.__products)

class Smartphone(Product):
    """Класс для представления смартфона (ДЗ 15.1)"""
    
    def __init__(self, name, description, price, quantity,
                 performance, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color
    
    def __str__(self):
        """Строковое представление смартфона"""
        return f"{self.name} ({self.model}), {self._Product__price} руб. Остаток: {self.quantity} шт."

class LawnGrass(Product):
    """Класс для представления газонной травы (ДЗ 15.1)"""
    
    def __init__(self, name, description, price, quantity,
                 country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
    
    def __str__(self):
        """Строковое представление газонной травы"""
        return f"{self.name} из {self.country}, {self._Product__price} руб. Остаток: {self.quantity} шт."


# Пример использования
if __name__ == "__main__":
    try:
        # Тестирование исключения
        p1 = Product("Телефон", "Смартфон", 50000.0, 10)
        print(f"Создан товар: {p1}")
        print(f"Product count: {Product.product_count}")
        
        # Тестирование сеттера цены
        p1.price = -1000  # Должно вывести сообщение и не изменить цену
        print(f"Цена после попытки установить -1000: {p1.price}")
        
        p1.price = 45000  # Корректное изменение
        print(f"Цена после установки 45000: {p1.price}")
        
        # Тестирование new_product
        data = {'name': 'Ноутбук', 'description': 'Игровой', 'price': 100000, 'quantity': 3}
        p2 = Product.new_product(data)
        print(f"Создан через new_product: {p2}")
        # Тестирование сложения
        p3 = Product("Планшет", "Графический", 30000, 2)
        p4 = Product("Планшет", "Графический", 25000, 3)
        result = p3 + p4
        print(f"Сумма товаров: {result}")
        
        # Тестирование категории
        category = Category("Электроника", "Техника")
        print(f"Category count после создания: {Category.category_count}")
        category.add_product(p1)
        category.add_product(p2)
        print(f"Category: {category}")
        print(f"Средняя цена: {category.average_price}")
        print(f"Product count в категориях: {Category.product_count}")
        
    except ZeroQuantityError as e:
        print(f"Поймано исключение: {e}")
    except Exception as e:
        print(f"Другая ошибка: {type(e).__name__}: {e}")