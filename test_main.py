"""
Тесты для 100% покрытия кода
"""
import pytest
from main import Product, Category, ZeroQuantityError


class TestZeroQuantityError:
    """Тесты исключения ZeroQuantityError"""
    
    def test_inheritance(self):
        """ZeroQuantityError наследуется от ValueError"""
        assert issubclass(ZeroQuantityError, ValueError)
    
    def test_default_message(self):
        """Сообщение по умолчанию"""
        error = ZeroQuantityError()
        assert str(error) == "Товар с нулевым количеством не может быть добавлен"
    
    def test_custom_message(self):
        """Кастомное сообщение"""
        error = ZeroQuantityError("Кастомное сообщение")
        assert str(error) == "Кастомное сообщение"
    def test_raised_on_zero_quantity(self):
        """Исключение вызывается при quantity=0"""
        with pytest.raises(ZeroQuantityError) as exc:
            Product("Товар", "Описание", 100, 0)
        assert "Товар с нулевым количеством не может быть добавлен" in str(exc.value)


class TestProduct:
    """Тесты класса Product"""
    
    def test_creation_valid(self):
        """Создание товара с валидными данными"""
        product = Product("Телефон", "Смартфон", 50000.0, 10)
        assert product.name == "Телефон"
        assert product.description == "Смартфон"
        assert product.price == 50000.0
        assert product.quantity == 10
    
    def test_str_representation(self):
        """Строковое представление"""
        product = Product("Телефон", "Смартфон", 50000.0, 10)
        expected = "Телефон, 50000.0 руб. Остаток: 10 шт."
        assert str(product) == expected
    
    def test_repr_representation(self):
        """Отладочное представление"""
        product = Product("Телефон", "Смартфон", 50000.0, 10)
        repr_str = repr(product)
        assert "Product(" in repr_str
        assert "name='Телефон'" in repr_str
        assert "description='Смартфон'" in repr_str
        assert "price=50000.0" in repr_str
        assert "quantity=10" in repr_str
    def test_product_count_increments(self):
        """Счетчик товаров увеличивается"""
        initial = Product.product_count
        Product("Товар1", "Описание", 100, 1)
        Product("Товар2", "Описание", 200, 2)
        assert Product.product_count == initial + 2
    
    def test_with_fractional_price(self):
        """Товар с дробной ценой"""
        product = Product("Товар", "Описание", 99.99, 5)
        assert product.price == 99.99
        assert "99.99" in str(product)
    
    def test_with_zero_price(self):
        """Товар с нулевой ценой (допустимо)"""
        product = Product("Бесплатный", "Даром", 0.0, 5)
        assert product.price == 0.0
        assert "0.0" in str(product)


class TestCategory:
    """Тесты класса Category"""
    
    def test_creation(self):
        """Создание категории"""
        category = Category("Электроника", "Техника")
        assert category.name == "Электроника"
        assert category.description == "Техника"
        assert len(category.products) == 0
    
    def test_add_product(self):
        """Добавление товара в категорию"""
        category = Category("Электроника", "Техника")
        product = Product("Телефон", "Смартфон", 50000.0, 10)
        category.add_product(product)
        assert len(category.products) == 1
        assert category.products[0] == product
    
    def test_add_multiple_products(self):
        """Добавление нескольких товаров"""
        category = Category("Электроника", "Техника")
        
        products = [
            Product("Телефон", "Смартфон", 50000.0, 10),
            Product("Ноутбук", "Игровой", 100000.0, 5),
            Product("Планшет", "10 дюймов", 30000.0, 8)
        ]
        
        for product in products:
            category.add_product(product)
        
        assert len(category.products) == 3
        assert category.products == products
    
    def test_average_price_empty(self):
        """Средняя цена пустой категории"""
        category = Category("Пустая", "Нет товаров")
        assert category.average_price() == 0.0
    
    def test_average_price_single(self):
        """Средняя цена с одним товаром"""
        category = Category("Категория", "Описание")
        product = Product("Товар", "Описание", 100.0, 5)
        category.add_product(product)

        assert category.average_price() == 100.0
    
    def test_average_price_multiple(self):
        """Средняя цена с несколькими товарами"""
        category = Category("Категория", "Описание")
        
        category.add_product(Product("Т1", "Описание", 100.0, 2))
        category.add_product(Product("Т2", "Описание", 200.0, 3))
        category.add_product(Product("Т3", "Описание", 300.0, 1))
        
        # (100 + 200 + 300) / 3 = 200
        assert category.average_price() == 200.0
    
    def test_str_representation_empty(self):
        """Строковое представление пустой категории"""
        category = Category("Электроника", "Техника")
        expected = "Электроника, количество продуктов: 0 шт."
        assert str(category) == expected
    
    def test_str_representation_with_products(self):
        """Строковое представление категории с товарами"""
        category = Category("Электроника", "Техника")
        category.add_product(Product("Телефон", "Смартфон", 50000.0, 10))
        
        expected = "Электроника, количество продуктов: 1 шт."
        assert str(category) == expected
    def test_repr_representation(self):
        """Отладочное представление категории"""
        category = Category("Электроника", "Техника")
        repr_str = repr(category)
        
        assert "Category(" in repr_str
        assert "name='Электроника'" in repr_str
        assert "description='Техника'" in repr_str
        assert "products_count=0" in repr_str
        
        # С товаром
        category.add_product(Product("Телефон", "Смартфон", 50000.0, 10))
        repr_str = repr(category)
        assert "products_count=1" in repr_str
    
    def test_category_count_increments(self):
        """Счетчик категорий увеличивается"""
        initial = Category.category_count
        Category("Категория1", "Описание")
        Category("Категория2", "Описание")
        assert Category.category_count == initial + 2
    
    def test_products_property(self):
        """Свойство products возвращает список"""
        category = Category("Категория", "Описание")
        assert isinstance(category.products, list)
        assert len(category.products) == 0
def test_integration():
    """Интеграционный тест"""
    # Создаем товары
    phone = Product("Смартфон", "Android", 30000.0, 15)
    laptop = Product("Ноутбук", "16GB RAM", 80000.0, 8)
    headphones = Product("Наушники", "Беспроводные", 5000.0, 25)
    
    # Создаем категорию
    electronics = Category("Электроника", "Техника")
    
    # Добавляем товары
    electronics.add_product(phone)
    electronics.add_product(laptop)
    electronics.add_product(headphones)
    
    # Проверяем
    assert len(electronics.products) == 3
    assert electronics.average_price() == (30000 + 80000 + 5000) / 3
    assert "Электроника, количество продуктов: 3 шт." == str(electronics)
    
    # Проверяем счетчики
    assert Product.product_count >= 3
    assert Category.category_count >= 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
