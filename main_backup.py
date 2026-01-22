"""
Минимальная реализация ДЗ 17.1 с гарантированным покрытием >75%
"""
class ZeroQuantityError(ValueError):
    """Исключение для товара с нулевым количеством"""
    def __init__(self, message="Товар с нулевым количеством не может быть добавлен"):
        super().__init__(message)


class Product:
    """Класс товара"""
    product_count = 0
    
    def __init__(self, name, description, price, quantity):
        if quantity == 0:
            raise ZeroQuantityError()
        
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        Product.product_count += 1
    
    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."
    
    def __repr__(self):
        return f"Product(name={self.name!r}, description={self.description!r}, price={self.price}, quantity={self.quantity})"


class Category:
    """Класс категории"""
    category_count = 0
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__products = []
        Category.category_count += 1
    @property
    def products(self):
        return self.__products
    
    def add_product(self, product):
        self.__products.append(product)
    
    def average_price(self):
        if not self.__products:
            return 0.0
        total = sum(p.price for p in self.__products)
        return total / len(self.__products)
    
    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.__products)} шт."
    
    def __repr__(self):
        return f"Category(name={self.name!r}, description={self.description!r}, products_count={len(self.__products)})"
