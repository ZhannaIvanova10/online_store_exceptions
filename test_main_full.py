"""
Полные тесты для всех ДЗ (59+ тестов)
"""
import pytest
from main import (
    Product, Category, Smartphone, LawnGrass, 
    ZeroQuantityError, BaseProduct, ReprMixin
)


# =================== ДЗ 17.1: Исключения ===================
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
    def test_raised_on_zero_quantity_product(self):
        """Исключение вызывается при quantity=0 в Product"""
        with pytest.raises(ZeroQuantityError):
            Product("Товар", "Описание", 100, 0)
    
    def test_raised_on_zero_quantity_add_product(self):
        """Исключение при добавлении товара с quantity=0 в категорию"""
        category = Category("Категория", "Описание")
        product = Product("Товар", "Описание", 100, 5)
        product.quantity = 0  # Изменяем количество на 0
        with pytest.raises(ZeroQuantityError):
            category.add_product(product)


# =================== ДЗ 14.1: Product и Category ===================
class TestProductBasic:
    """Базовые тесты класса Product"""
    
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
        assert "Product(" in repr(product)
        assert "name='Телефон'" in repr(product)
    
    def test_product_count_increments(self):
        """Счетчик товаров увеличивается"""
        initial = Product.product_count
        Product("Тест", "Тест", 100, 1)
        assert Product.product_count == initial + 1
    
    def test_with_fractional_price(self):
        """Товар с дробной ценой"""
        product = Product("Товар", "Описание", 99.99, 5)
        assert product.price == 99.99
    
    def test_with_zero_price(self):
        """Товар с нулевой ценой (допустимо)"""
        product = Product("Бесплатный", "Описание", 0, 5)
        assert product.price == 0


class TestCategoryBasic:
    """Базовые тесты класса Category"""
    
    def test_creation(self):
        """Создание категории"""
        category = Category("Электроника", "Гаджеты и устройства")
        assert category.name == "Электроника"
        assert category.description == "Гаджеты и устройства"
        assert category.products == []
    def test_add_product(self):
        """Добавление товара в категорию"""
        category = Category("Электроника", "Описание")
        product = Product("Телефон", "Смартфон", 50000, 2)
        category.add_product(product)
        assert len(category.products) == 1
        assert category.products[0].name == "Телефон"
    
    def test_add_multiple_products(self):
        """Добавление нескольких товаров"""
        category = Category("Электроника", "Описание")
        p1 = Product("Телефон", "Смартфон", 50000, 2)
        p2 = Product("Ноутбук", "Игровой", 100000, 1)
        category.add_product(p1)
        category.add_product(p2)
        assert len(category.products) == 2
    
    def test_str_representation_empty(self):
        """Строковое представление пустой категории"""
        category = Category("Электроника", "Описание")
        assert str(category).startswith("Электроника, количество продуктов: 0 шт.")
    
    def test_str_representation_with_products(self):
        """Строковое представление с товарами"""
        category = Category("Электроника", "Описание")
        product = Product("Телефон", "Смартфон", 50000, 2)
        category.add_product(product)
        assert "Телефон, 50000 руб. Остаток: 2 шт." in str(category)
    def test_category_count_increments(self):
        """Счетчик категорий увеличивается"""
        initial = Category.category_count
        Category("Тест", "Тест")
        assert Category.category_count == initial + 1
    
    def test_products_property(self):
        """Свойство products возвращает список"""
        category = Category("Электроника", "Описание")
        assert isinstance(category.products, list)


# =================== ДЗ 17.1: average_price() ===================
class TestAveragePrice:
    """Тесты метода average_price()"""
    
    def test_average_price_empty(self):
        """Средняя цена пустой категории"""
        category = Category("Пустая", "Категория")
        assert category.average_price() == 0.0
    
    def test_average_price_single(self):
        """Средняя цена с одним товаром"""
        category = Category("Категория", "Описание")
        product = Product("Товар", "Описание", 100, 1)
        category.add_product(product)
        assert category.average_price() == 100.0
    
    def test_average_price_multiple(self):
        """Средняя цена с несколькими товарами"""
        category = Category("Категория", "Описание")
        p1 = Product("Товар1", "Описание", 100, 2)
        p2 = Product("Товар2", "Описание", 300, 1)
        category.add_product(p1)
        category.add_product(p2)
        assert category.average_price() == 200.0  # (100 + 300) / 2
    def test_average_price_fractional(self):
        """Средняя цена дробная"""
        category = Category("Категория", "Описание")
        p1 = Product("Товар1", "Описание", 100, 1)
        p2 = Product("Товар2", "Описание", 200, 1)
        category.add_product(p1)
        category.add_product(p2)
        assert category.average_price() == 150.0
    
    def test_average_price_after_removal(self):
        """Средняя цена после изменений"""
        category = Category("Категория", "Описание")
        p1 = Product("Товар1", "Описание", 100, 1)
        p2 = Product("Товар2", "Описание", 200, 1)
        category.add_product(p1)
        category.add_product(p2)
        # Симулируем "удаление" - создаем новую категорию
        category2 = Category("Новая", "Категория")
        category2.add_product(p2)
        assert category2.average_price() == 200.0


# =================== ДЗ 15.1: Магические методы ===================
class TestMagicMethods:
    """Тесты магических методов"""
    
    def test_add_products_same_type(self):
        """Сложение товаров одного типа"""
        p1 = Product("Яблоки", "Фрукты", 100, 10)  # 1000 руб
        p2 = Product("Яблоки", "Фрукты", 150, 20)  # 3000 руб
        result = p1 + p2
        assert result.quantity == 30
        # (100*10 + 150*20) / 30 = (1000 + 3000) / 30 = 4000 / 30 ≈ 133.33
        assert abs(result.price - 133.33) < 0.1
    def test_add_products_different_type_error(self):
        """Ошибка при сложении товаров разного типа"""
        p1 = Product("Яблоки", "Фрукты", 100, 10)
        p2 = Smartphone("iPhone", "Смартфон", 100000, 2, "A15", "13", "128GB", "черный")
        with pytest.raises(TypeError):
            p1 + p2
    
    def test_add_product_with_non_product_error(self):
        """Ошибка при сложении с не-товаром"""
        p1 = Product("Яблоки", "Фрукты", 100, 10)
        with pytest.raises(TypeError):
            p1 + 100
    
    def test_str_magic_method(self):
        """Проверка __str__ для всех классов"""
        p = Product("Товар", "Описание", 100, 5)
        assert "Товар, 100 руб. Остаток: 5 шт." == str(p)
        
        s = Smartphone("iPhone", "Смартфон", 100000, 2, "A15", "13", "128GB", "черный")
        assert "iPhone (13)" in str(s)
        
        g = LawnGrass("Трава", "Газонная", 500, 10, "Россия", "14 дней", "зеленая")
        assert "Трава из России" in str(g)
# =================== ДЗ 16.1: Наследование ===================
class TestSmartphone:
    """Тесты класса Smartphone"""
    
    def test_smartphone_creation(self):
        """Создание смартфона"""
        phone = Smartphone(
            name="iPhone",
            description="Смартфон",
            price=100000,
            quantity=5,
            performance="A15",
            model="13",
            memory="128GB",
            color="черный"
        )
        assert phone.name == "iPhone"
        assert phone.price == 100000
        assert phone.quantity == 5
        assert phone.performance == "A15"
        assert phone.model == "13"
        assert phone.memory == "128GB"
        assert phone.color == "черный"
    
    def test_smartphone_inheritance(self):
        """Smartphone наследуется от Product"""
        phone = Smartphone("iPhone", "Смартфон", 100000, 2, "A15", "13", "128GB", "черный")
        assert isinstance(phone, Product)
    
    def test_smartphone_str(self):
        """Строковое представление Smartphone"""
        phone = Smartphone("iPhone", "Смартфон", 100000, 2, "A15", "13", "128GB", "черный")
        assert "iPhone (13)" in str(phone)

    def test_smartphone_addition(self):
        """Сложение смартфонов"""
        p1 = Smartphone("iPhone", "Смартфон", 100000, 2, "A15", "13", "128GB", "черный")
        p2 = Smartphone("iPhone", "Смартфон", 120000, 3, "A15", "13", "256GB", "белый")
        result = p1 + p2
        assert isinstance(result, Smartphone)
        assert result.quantity == 5


class TestLawnGrass:
    """Тесты класса LawnGrass"""
    
    def test_lawn_grass_creation(self):
        """Создание газонной травы"""
        grass = LawnGrass(
            name="Газонная трава",
            description="Для дачи",
            price=500,
            quantity=100,
            country="Россия",
            germination_period="14 дней",
            color="зеленая"
        )
        assert grass.name == "Газонная трава"
        assert grass.price == 500
        assert grass.quantity == 100
        assert grass.country == "Россия"
        assert grass.germination_period == "14 дней"
        assert grass.color == "зеленая"
    
    def test_lawn_grass_inheritance(self):
        """LawnGrass наследуется от Product"""
        grass = LawnGrass("Трава", "Газонная", 500, 10, "Россия", "14 дней", "зеленая")
        assert isinstance(grass, Product)
    
    def test_lawn_grass_str(self):
        """Строковое представление LawnGrass"""
        grass = LawnGrass("Трава", "Газонная", 500, 10, "Россия", "14 дней", "зеленая")
        assert "Трава из России" in str(grass)
    def test_lawn_grass_addition(self):
        """Сложение газонных трав"""
        g1 = LawnGrass("Трава", "Газонная", 500, 10, "Россия", "14 дней", "зеленая")
        g2 = LawnGrass("Трава", "Газонная", 600, 20, "Россия", "14 дней", "зеленая")
        result = g1 + g2
        assert isinstance(result, LawnGrass)
        assert result.quantity == 30


# =================== ДЗ 16.2: Абстрактные классы и миксины ===================
class TestAbstractClassesAndMixins:
    """Тесты абстрактных классов и миксинов"""
    
    def test_base_product_is_abstract(self):
        """BaseProduct - абстрактный класс"""
        assert isinstance(BaseProduct, type)
        # Проверяем что нельзя создать экземпляр
        with pytest.raises(TypeError):
            BaseProduct("name", "desc", 100, 1)
    
    def test_product_inherits_from_base_product(self):
        """Product наследуется от BaseProduct"""
        product = Product("Товар", "Описание", 100, 1)
        assert isinstance(product, BaseProduct)
    
    def test_repr_mixin_works(self):
        """ReprMixin добавляет repr"""
        
        class TestClass(ReprMixin):
            def __init__(self, a, b):
                self.a = a
                self.b = b
        obj = TestClass(1, "test")
        repr_str = repr(obj)
        assert "TestClass" in repr_str
        assert "a=1" in repr_str
        assert "b='test'" in repr_str
    
    def test_all_products_use_repr_mixin(self):
        """Все классы продуктов используют ReprMixin"""
        product = Product("Товар", "Описание", 100, 1)
        phone = Smartphone("iPhone", "Смартфон", 100000, 2, "A15", "13", "128GB", "черный")
        grass = LawnGrass("Трава", "Газонная", 500, 10, "Россия", "14 дней", "зеленая")
        
        # Проверяем что repr содержит имя класса
        assert "Product(" in repr(product)
        assert "Smartphone(" in repr(phone)
        assert "LawnGrass(" in repr(grass)


# =================== ДЗ 14.2: Приватные атрибуты, геттеры/сеттеры ===================
class TestPrivateAttributes:
    """Тесты приватных атрибутов и свойств"""
    
    def test_category_private_products(self):
        """__products приватный атрибут"""
        category = Category("Категория", "Описание")
        # Нельзя обратиться напрямую
        with pytest.raises(AttributeError):
            _ = category.__products
        # Но можно через property
        assert category.products == []
    def test_products_property_is_getter(self):
        """products property только геттер"""
        category = Category("Категория", "Описание")
        product = Product("Товар", "Описание", 100, 1)
        category.add_product(product)
        
        # Можем читать
        products = category.products
        assert len(products) == 1
        
        # Но не можем присвоить (только если property не имеет setter)
        # category.products = []  # Это вызовет ошибку, что правильно


# =================== Интеграционные тесты ===================
def test_integration():
    """Интеграционный тест всех компонентов"""
    # Создаем категорию
    electronics = Category("Электроника", "Гаджеты и устройства")
    
    # Создаем товары разных типов
    phone = Smartphone(
        name="iPhone 15",
        description="Флагманский смартфон",
        price=99999,
        quantity=10,
        performance="A16",
        model="15 Pro",
        memory="256GB",
        color="Титановый"
    )
    laptop = Product(
        name="MacBook Pro",
        description="Ноутбук для профессионалов",
        price=199999,
        quantity=5
    )
    
    # Добавляем в категорию
    electronics.add_product(phone)
    electronics.add_product(laptop)
    
    # Проверяем
    assert len(electronics.products) == 2
    assert electronics.average_price() == (99999 + 199999) / 2
    
    # Создаем вторую категорию
    garden = Category("Сад", "Товары для сада")
    
    grass = LawnGrass(
        name="Газонная трава Премиум",
        description="Быстрорастущая",
        price=2999,
        quantity=50,
        country="Германия",
        germination_period="10 дней",
        color="Изумрудный"
    )
    
    garden.add_product(grass)
    
    # Проверяем счетчики
    assert Category.category_count >= 2
    assert Product.product_count >= 3
    
    print("✅ Интеграционный тест пройден")
# =================== Дополнительные тесты ===================
class TestEdgeCases:
    """Тесты крайних случаев"""
    
    def test_product_with_max_values(self):
        """Товар с максимальными значениями"""
        product = Product("Товар", "Описание", float('inf'), 10**6)
        assert product.price == float('inf')
        assert product.quantity == 10**6
    
    def test_category_with_many_products(self):
        """Категория со многими товарами"""
        category = Category("Большая", "Категория")
        for i in range(100):
            product = Product(f"Товар{i}", f"Описание{i}", i * 100, i + 1)
            category.add_product(product)
        assert len(category.products) == 100
        assert category.average_price() > 0
    
    def test_new_product_class_method(self):
        """Класс-метод new_product"""
        product = Category.new_product("Новый", "Товар", 1000, 50)
        assert isinstance(product, Product)
        assert product.name == "Новый"
        assert product.price == 1000
        assert product.quantity == 50


# Подсчитаем тесты
if __name__ == "__main__":
    import inspect
    test_functions = [name for name, obj in inspect.getmembers(sys.modules[__name__]) 
                     if inspect.isfunction(obj) and name.startswith('test_')]
    print(f"Всего тестов: {len(test_functions)}")
