"""
Тесты для модуля main.py
"""
import pytest
from main import Product, Category, ZeroQuantityError


class TestProduct:
    """Тесты для класса Product"""
    
    def test_product_creation_success(self):
        """Тест успешного создания товара"""
        product = Product("Телефон", "Смартфон", 50000.0, 5)
        assert product.name == "Телефон"
        assert product.description == "Смартфон"
        assert product.price == 50000.0
        assert product.quantity == 5
    
    def test_product_creation_zero_quantity_raises_error(self):
        """Тест: создание товара с нулевым количеством вызывает исключение"""
        with pytest.raises(ZeroQuantityError) as exc_info:
            Product("Телефон", "Смартфон", 50000.0, 0)
        
        assert "Товар с нулевым количеством не может быть добавлен" in str(exc_info.value)
    def test_product_string_representation(self):
        """Тест строкового представления товара"""
        product = Product("Ноутбук", "Игровой", 100000.0, 3)
        expected = "Ноутбук, 100000.0 руб. Остаток: 3 шт."
        assert str(product) == expected
    
    def test_product_repr(self):
        """Тест repr для Product"""
        product = Product("Тест", "Описание", 100, 5)
        repr_str = repr(product)
        assert "Product" in repr_str
        assert "Тест" in repr_str


class TestCategory:
    """Тесты для класса Category"""
    
    def test_category_creation(self):
        """Тест создания категории"""
        category = Category("Электроника", "Техника")
        assert category.name == "Электроника"
        assert category.description == "Техника"
        assert Category.category_count > 0
    
    def test_add_product_to_category(self):
        """Тест добавления товара в категорию"""
        category = Category("Электроника", "Техника")
        product = Product("Наушники", "Беспроводные", 5000.0, 10)
        initial_count = Category.product_count
        category.add_product(product)
        
        assert Category.product_count == initial_count + 1
    
    def test_average_price_with_products(self):
        """Тест расчета средней цены с товарами"""
        category = Category("Тест", "Тест")
        
        # Добавляем товары
        category.add_product(Product("Товар1", "Описание1", 100.0, 5))
        category.add_product(Product("Товар2", "Описание2", 200.0, 3))
        category.add_product(Product("Товар3", "Описание3", 300.0, 2))
        
        # (100 + 200 + 300) / 3 = 200
        assert category.average_price() == 200.0
    
    def test_average_price_without_products(self):
        """Тест расчета средней цены без товаров"""
        category = Category("Пустая", "Категория без товаров")
        assert category.average_price() == 0.0
    
    def test_average_price_single_product(self):
        """Тест расчета средней цены с одним товаром"""
        category = Category("Один товар", "Тест")
        category.add_product(Product("Товар", "Описание", 150.0, 1))
        assert category.average_price() == 150.0
    
    def test_average_price_with_zero_price(self):
        """Тест средней цены с товарами нулевой цены"""
        category = Category("Тест", "Тест")
        category.add_product(Product("Т1", "Д1", 0, 5))
        category.add_product(Product("Т2", "Д2", 0, 3))
        assert category.average_price() == 0
    def test_category_string_representation(self):
        """Тест строкового представления категории"""
        category = Category("Электроника", "Техника")
        product1 = Product("Товар1", "Описание1", 100.0, 2)
        product2 = Product("Товар2", "Описание2", 200.0, 3)
        
        category.add_product(product1)
        category.add_product(product2)
        
        assert str(category) == "Электроника, количество продуктов: 5 шт."
    
    def test_products_property(self):
        """Тест геттера products"""
        category = Category("Тест", "Тест")
        product1 = Product("Товар1", "Описание1", 100.0, 1)
        product2 = Product("Товар2", "Описание2", 200.0, 2)
        
        category.add_product(product1)
        category.add_product(product2)
        
        products_str = category.products
        assert "Товар1, 100.0 руб. Остаток: 1 шт." in products_str
        assert "Товар2, 200.0 руб. Остаток: 2 шт." in products_str
    
    def test_category_repr(self):
        """Тест repr для Category"""
        category = Category("Тест", "Описание")
        repr_str = repr(category)
        assert "Category" in repr_str
        assert "Тест" in repr_str


class TestIntegration:
    """Интеграционные тесты"""

    def test_add_product_with_zero_quantity_fails(self):
        """Тест: нельзя создать товар с нулевым количеством и добавить в категорию"""
        category = Category("Тест", "Тест")
        
        # Попытка создать товар с нулевым количеством
        with pytest.raises(ZeroQuantityError):
            bad_product = Product("Плохой товар", "Нет в наличии", 100.0, 0)
            category.add_product(bad_product)
        
        # Убеждаемся, что счетчик товаров не изменился
        initial_count = Category.product_count
        assert Category.product_count == initial_count
    
    def test_class_attributes_counting(self):
        """Тест подсчета категорий и товаров"""
        # Сохраняем начальные значения
        initial_categories = Category.category_count
        initial_products = Category.product_count
        
        # Создаем новые объекты
        cat1 = Category("Категория 1", "Описание 1")
        cat2 = Category("Категория 2", "Описание 2")
        
        product1 = Product("Товар 1", "Описание", 100.0, 1)
        product2 = Product("Товар 2", "Описание", 200.0, 2)
        product3 = Product("Товар 3", "Описание", 300.0, 3)
        cat1.add_product(product1)
        cat1.add_product(product2)
        cat2.add_product(product3)
        
        # Проверяем счетчики
        assert Category.category_count == initial_categories + 2
        assert Category.product_count == initial_products + 3


class TestCustomException:
    """Тесты для пользовательского исключения"""
    
    def test_zero_quantity_error_inheritance(self):
        """Тест наследования ZeroQuantityError"""
        assert issubclass(ZeroQuantityError, ValueError)
    
    def test_zero_quantity_error_message(self):
        """Тест сообщения в ZeroQuantityError"""
        try:
            Product("Тест", "Тест", 100, 0)
        except ZeroQuantityError as e:
            assert "Товар с нулевым количеством не может быть добавлен" in str(e)
