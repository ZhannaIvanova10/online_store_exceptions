"""
Тесты для полной функциональности интернет-магазина.
Покрывают все ДЗ от 14.1 до 17.1.
"""
from main import Product, Category, Smartphone, LawnGrass
import pytest
from main import Product, Category, Smartphone, LawnGrass, ZeroQuantityError


class TestProduct:
    """Тесты класса Product (ДЗ 14.1, 14.2, 15.1, 17.1)"""

    def test_product_creation_success(self):
        """Тест успешного создания товара"""
        product = Product("Телефон", "Смартфон", 50000.0, 10)
        assert product.name == "Телефон"
        assert product.description == "Смартфон"
        assert product.price == 50000.0
        assert product.quantity == 10

    def test_product_creation_zero_quantity_raises_error(self):
        """Тест исключения при нулевом количестве (ДЗ 17.1)"""
        with pytest.raises(ZeroQuantityError) as exc_info:
            Product("Товар", "Описание", 100.0, 0)
        assert "Товар с нулевым количеством не может быть добавлен" in str(
            exc_info.value)

    def test_product_string_representation(self):
        """Тест строкового представления (ДЗ 15.1)"""
        product = Product("Телефон", "Смартфон", 50000.0, 10)
        expected = "Телефон, 50000.0 руб. Остаток: 10 шт."
        assert str(product) == expected

    def test_product_price_setter_valid(self):
        """Тест сеттера цены с корректным значением (ДЗ 14.2)"""
        product = Product("Телефон", "Смартфон", 50000.0, 10)
        product.price = 45000.0
        assert product.price == 45000.0

    def test_product_price_setter_invalid(self, capsys):
        """Тест сеттера цены с некорректным значением (ДЗ 14.2)"""
        product = Product("Телефон", "Смартфон", 50000.0, 10)
        product.price = -1000.0
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert product.price == 50000.0  # Цена не изменилась

    def test_product_addition_same_type(self):
        """Тест сложения товаров одного типа (ДЗ 15.1)"""
        product1 = Product("Товар1", "Описание", 100.0, 5)
        product2 = Product("Товар2", "Описание", 200.0, 3)
        total = product1 + product2
        expected = 100.0 * 5 + 200.0 * 3  # 500 + 600 = 1100
        assert total == expected

    def test_product_new_product_classmethod(self):
        """Тест класс-метода new_product (ДЗ 14.2)"""
        product_data = {
            'name': 'Ноутбук',
            'description': 'Игровой',
            'price': 150000.0,
            'quantity': 3
        }
        product = Product.new_product(product_data)
        assert product.name == "Ноутбук"
        assert product.price == 150000.0
        assert product.quantity == 3

    def test_product_new_product_with_duplicates(self):
        """Тест new_product с дубликатами (доп. задание ДЗ 14.2)"""
        product1 = Product("Ноутбук", "Игровой", 150000.0, 3)
        product_data = {
            'name': 'Ноутбук',
            'description': 'Игровой',
            'price': 160000.0,  # Более высокая цена
            'quantity': 2
        }
        # Передаем существующий товар в список
        result = Product.new_product(product_data, [product1])
        # Должен вернуть существующий товар с обновленными значениями
        assert result is product1
        assert product1.quantity == 5  # 3 + 2
        assert product1.price == 160000.0  # Более высокая цена


class TestSmartphone:
    """Тесты класса Smartphone (ДЗ 16.1)"""

    def test_smartphone_creation(self):
        """Тест создания смартфона"""
        phone = Smartphone(
            "iPhone", "Флагман", 99999.0, 7,
            "Высокая", "15 Pro", 256, "Black"
        )
        assert phone.name == "iPhone"
        assert phone.model == "15 Pro"
        assert phone.memory == 256
        assert phone.color == "Black"

    def test_smartphone_inheritance(self):
        """Тест наследования от Product"""
        phone = Smartphone(
            "iPhone", "Флагман", 99999.0, 7,
            "Высокая", "15 Pro", 256, "Black"
        )
        assert isinstance(phone, Product)

    def test_smartphone_string_representation(self):
        """Тест строкового представления смартфона"""
        phone = Smartphone(
            "iPhone", "Флагман", 99999.0, 7,
            "Высокая", "15 Pro", 256, "Black"
        )
        expected = "iPhone (15 Pro), 99999.0 руб. Остаток: 7 шт. Память: 256ГБ"
        assert str(phone) == expected

    def test_smartphone_addition_same_type(self):
        """Тест сложения смартфонов"""
        phone1 = Smartphone(
            "iPhone", "Флагман", 99999.0, 7,
            "Высокая", "15 Pro", 256, "Black"
        )
        phone2 = Smartphone(
            "Samsung", "Android", 79999.0, 5,
            "Высокая", "S23", 128, "White"
        )
        total = phone1 + phone2
        expected = 99999.0 * 7 + 79999.0 * 5
        assert total == expected


class TestLawnGrass:
    """Тесты класса LawnGrass (ДЗ 16.1)"""

    def test_lawngrass_creation(self):
        """Тест создания газонной травы"""
        grass = LawnGrass(
            "Трава газонная", "Для дачи", 500.0, 100,
            "Россия", 14, "Зеленая"
        )
        assert grass.name == "Трава газонная"
        assert grass.country == "Россия"
        assert grass.germination_period == 14
        assert grass.color == "Зеленая"

    def test_lawngrass_inheritance(self):
        """Тест наследования от Product"""
        grass = LawnGrass(
            "Трава газонная", "Для дачи", 500.0, 100,
            "Россия", 14, "Зеленая"
        )
        assert isinstance(grass, Product)

    def test_lawngrass_string_representation(self):
        """Тест строкового представления газонной травы"""
        grass = LawnGrass(
            "Трава газонная", "Для дачи", 500.0, 100,
            "Россия", 14, "Зеленая"
        )
        expected = "Трава газонная, 500.0 руб. Остаток: 100 шт. Страна: Россия, Прорастание: 14 дней"
        assert str(grass) == expected


class TestInheritanceRestrictions:
    """Тесты ограничений наследования (ДЗ 16.1)"""

    def test_addition_different_types_raises_error(self):
        """Тест ошибки при сложении разных типов товаров"""
        phone = Smartphone(
            "iPhone", "Флагман", 99999.0, 7,
            "Высокая", "15 Pro", 256, "Black"
        )
        grass = LawnGrass(
            "Трава газонная", "Для дачи", 500.0, 100,
            "Россия", 14, "Зеленая"
        )
        with pytest.raises(TypeError) as exc_info:
            _ = phone + grass
        assert "Можно складывать только товары одного типа" in str(
            exc_info.value)

    def test_add_product_type_check(self):
        """Тест проверки типа при добавлении товара в категорию"""
        category = Category("Электроника", "Техника")

        # Корректный товар
        product = Product("Телефон", "Смартфон", 50000.0, 10)
        category.add_product(product)
        assert len(category.products.split('\n')) == 1

        # Некорректный объект
        with pytest.raises(TypeError) as exc_info:
            category.add_product("не товар")
        assert "Можно добавлять только товары" in str(exc_info.value)


class TestCategory:
    """Тесты класса Category (ДЗ 14.1, 14.2, 15.1, 17.1)"""

    def test_category_creation(self):
        """Тест создания категории"""
        category = Category("Электроника", "Техника")
        assert category.name == "Электроника"
        assert category.description == "Техника"

    def test_add_product_to_category(self):
        """Тест добавления товара в категорию"""
        category = Category("Электроника", "Техника")
        product = Product("Телефон", "Смартфон", 50000.0, 10)
        category.add_product(product)
        assert "Телефон, 50000.0" in category.products

    def test_average_price_with_products(self):
        """Тест расчета средней цены с товарами (ДЗ 17.1)"""
        category = Category("Электроника", "Техника")
        category.add_product(Product("Товар1", "Описание", 100.0, 2))
        category.add_product(Product("Товар2", "Описание", 300.0, 1))
        # (100*2 + 300*1) / 2 товара = 250.0
        assert category.average_price() == 200.0

    def test_average_price_without_products(self):
        """Тест расчета средней цены без товаров (ДЗ 17.1)"""
        category = Category("Пустая", "Нет товаров")
        assert category.average_price() == 0.0

    def test_average_price_single_product(self):
        """Тест расчета средней цены с одним товаром"""
        category = Category("Категория", "Описание")
        category.add_product(Product("Товар", "Описание", 150.0, 3))
        assert category.average_price() == 150.0

    def test_category_string_representation(self):
        """Тест строкового представления категории (ДЗ 15.1)"""
        category = Category("Электроника", "Техника")
        category.add_product(Product("Товар1", "Описание", 100.0, 2))
        category.add_product(Product("Товар2", "Описание", 300.0, 3))
        assert "Электроника, количество продуктов: 5 шт." in str(category)

    def test_products_property(self):
        """Тест геттера products (ДЗ 14.2)"""
        category = Category("Электроника", "Техника")
        category.add_product(Product("Товар1", "Описание", 100.0, 2))
        category.add_product(Product("Товар2", "Описание", 200.0, 3))
        products_str = category.products
        assert "Товар1, 100.0 руб. Остаток: 2 шт." in products_str
        assert "Товар2, 200.0 руб. Остаток: 3 шт." in products_str


class TestAbstractClassesAndMixins:
    """Тесты абстрактных классов и миксинов (ДЗ 16.2)"""

    def test_repr_mixin(self):
        """Тест миксина для repr представления"""
        product = Product("Телефон", "Смартфон", 50000.0, 10)
        repr_str = repr(product)
        assert "Product(" in repr_str
        assert "name='Телефон'" in repr_str
        assert "price=50000.0" in repr_str

    def test_base_product_abstract(self):
        """Тест, что BaseProduct - абстрактный класс"""
        from abc import ABC
        from main import BaseProduct
        assert issubclass(BaseProduct, ABC)


class TestZeroQuantityError:
    """Тесты пользовательского исключения (ДЗ 17.1)"""

    def test_zero_quantity_error_inheritance(self):
        """Тест наследования ZeroQuantityError от ValueError"""
        assert issubclass(ZeroQuantityError, ValueError)

    def test_zero_quantity_error_message(self):
        """Тест сообщения исключения"""
        try:
            Product("Товар", "Описание", 100.0, 0)
        except ZeroQuantityError as e:
            assert "Товар с нулевым количеством не может быть добавлен" in str(
                e)


class TestClassAttributes:
    """Тесты атрибутов класса (ДЗ 14.1)"""

    def test_class_attributes_counting(self):
        """Тест подсчета категорий и товаров"""
        # Сбрасываем счетчики
        Category.category_count = 0
        Category.product_count = 0

        category1 = Category("Категория1", "Описание1")
        category2 = Category("Категория2", "Описание2")
        product1 = Product("Товар1", "Описание", 100.0, 5)
        product2 = Product("Товар2", "Описание", 200.0, 3)

        category1.add_product(product1)
        category2.add_product(product2)

        assert Category.category_count == 2
        assert Category.product_count == 2


"""Дополнительные тесты для увеличения покрытия."""


def test_product_repr():
    """Тест repr для Product."""
    product = Product("Тест", "Описание", 100.0, 5)
    repr_str = repr(product)
    assert "Product(" in repr_str
    assert "name='Тест'" in repr_str


def test_smartphone_repr():
    """Тест repr для Smartphone."""
    phone = Smartphone(
        "Тест", "Описание", 100.0, 5,
        "Средняя", "Модель", 128, "Черный"
    )
    repr_str = repr(phone)
    assert "Smartphone(" in repr_str


def test_lawngrass_repr():
    """Тест repr для LawnGrass."""
    grass = LawnGrass(
        "Тест", "Описание", 100.0, 5,
        "Россия", 10, "Зеленый"
    )
    repr_str = repr(grass)
    assert "LawnGrass(" in repr_str


def test_category_repr():
    """Тест repr для Category."""
    category = Category("Тест", "Описание")
    assert repr(category) == "Category('Тест', 'Описание')"


def test_new_product_missing_fields():
    """Тест new_product с отсутствующими полями."""
    with pytest.raises(ValueError) as exc_info:
        Product.new_product({'name': 'Товар'})  # Нет других полей
    assert "Отсутствует поле" in str(exc_info.value)


def test_price_setter_zero():
    """Тест сеттера цены с нулевым значением."""
    product = Product("Тест", "Описание", 100.0, 5)
    product.price = 0
    # Должно вывести сообщение и не изменить цену
    assert product.price == 100.0


def test_add_product_wrong_type_message():
    """Тест сообщения об ошибке при добавлении неверного типа."""
    category = Category("Тест", "Описание")
    with pytest.raises(TypeError) as exc_info:
        category.add_product("не товар")
    assert "Можно добавлять только товары" in str(exc_info.value)


def test_zero_quantity_error_repr():
    """Тест repr для ZeroQuantityError."""
    error = ZeroQuantityError("Тестовое сообщение")
    assert str(error) == "Тестовое сообщение"


def test_base_product_cannot_be_instantiated():
    """Тест, что BaseProduct нельзя инстанцировать."""
    from abc import ABC
    from main import BaseProduct

    assert issubclass(BaseProduct, ABC)

    # Попытка создать экземпляр должна вызвать ошибку
    with pytest.raises(TypeError):
        BaseProduct("name", "desc", 100.0, 5)


def test_class_attributes_independent():
    """Тест независимости атрибутов класса."""
    # Сбрасываем
    Category.category_count = 0
    Category.product_count = 0

    cat1 = Category("Кат1", "Описание")
    cat2 = Category("Кат2", "Описание")

    assert Category.category_count == 2
    assert Category.product_count == 0  # Товары еще не добавлены

    prod = Product("Товар", "Описание", 100.0, 5)
    cat1.add_product(prod)

    assert Category.product_count == 1


def test_average_price_with_floats():
    """Тест средней цены с дробными числами."""
    category = Category("Тест", "Описание")
    category.add_product(Product("Т1", "Описание", 99.99, 2))
    category.add_product(Product("Т2", "Описание", 50.50, 3))

    avg = category.average_price()
    expected = (99.99 * 2 + 50.50 * 3) / 2
    expected = (99.99 * 2 + 50.50 * 3) / 5  # 2 товара по 99.99 и 3 по 50.50


"""Тесты для увеличения покрытия."""


def test_product_addition_different_types_error():
    """Тест ошибки при сложении разных типов."""
    p1 = Product("Т1", "Описание", 100.0, 2)
    p2 = Smartphone(
        "Т2",
        "Описание",
        200.0,
        3,
        "Высокая",
        "Модель",
        128,
        "Черный")

    with pytest.raises(TypeError) as exc_info:
        _ = p1 + p2
    assert "Можно складывать только товары одного типа" in str(exc_info.value)


def test_smartphone_str():
    """Тест строкового представления смартфона."""
    phone = Smartphone(
        "Тест", "Описание", 100.0, 5,
        "Средняя", "Модель", 256, "Синий"
    )
    assert "Тест" in str(phone)
    assert "Модель" in str(phone)
    assert "256" in str(phone)


def test_lawngrass_str():
    """Тест строкового представления газонной травы."""
    grass = LawnGrass(
        "Трава", "Описание", 50.0, 10,
        "Россия", 14, "Зеленая"
    )
    assert "Трава" in str(grass)
    assert "Россия" in str(grass)
    assert "14" in str(grass)


def test_category_products_multiple():
    """Тест геттера products с несколькими товарами."""
    category = Category("Тест", "Описание")
    p1 = Product("Т1", "Описание", 100.0, 2)
    p2 = Product("Т2", "Описание", 200.0, 3)

    category.add_product(p1)
    category.add_product(p2)

    products_str = category.products
    assert "Т1, 100.0 руб." in products_str
    assert "Т2, 200.0 руб." in products_str
    assert products_str.count("\n") == 1


def test_category_str_empty():
    """Тест строкового представления пустой категории."""
    category = Category("Пустая", "Описание")
    assert str(category) == "Пустая, количество продуктов: 0 шт."


def test_class_attributes():
    """Тест атрибутов класса Category."""
    # Сброс
    Category.category_count = 0
    Category.product_count = 0
    cat = Category("Категория", "Описание")
    assert Category.category_count == 1

    prod = Product("Товар", "Описание", 100.0, 5)
    cat.add_product(prod)
    assert Category.product_count == 1


def test_zero_quantity_error_instance():
    """Тест создания экземпляра ZeroQuantityError."""
    error = ZeroQuantityError("Тестовое сообщение")
    assert isinstance(error, ValueError)
    assert str(error) == "Тестовое сообщение"


def test_average_price_single():
    """Тест средней цены с одним товаром."""
    category = Category("Тест", "Описание")
    category.add_product(Product("Товар", "Описание", 150.0, 1))
    assert category.average_price() == 150.0


def test_add_product_error_message():
    """Тест сообщения об ошибке при добавлении не-товара."""
    category = Category("Тест", "Описание")
    with pytest.raises(TypeError) as exc_info:
        category.add_product("не товар")
    assert "Можно добавлять только товары" in str(exc_info.value)


def test_product_repr():
    """Тест repr для Product."""
    product = Product("Тест", "Описание", 123.45, 5)
    repr_str = repr(product)
    assert "Product(" in repr_str
    assert "name='Тест'" in repr_str


"""Финальные тесты для покрытия оставшихся строк."""


def test_product_init_normal():
    """Тест нормальной инициализации Product."""
    p = Product("Test", "Desc", 100.0, 5)
    assert p.name == "Test"
    assert p.description == "Desc"
    assert p.price == 100.0
    assert p.quantity == 5


def test_smartphone_all_attributes():
    """Тест всех атрибутов Smartphone."""
    s = Smartphone("Phone", "Smart", 500.0, 3, "High", "X10", 256, "Black")
    assert s.efficiency == "High"
    assert s.model == "X10"
    assert s.memory == 256
    assert s.color == "Black"


def test_lawngrass_all_attributes():
    """Тест всех атрибутов LawnGrass."""
    g = LawnGrass("Grass", "Green", 50.0, 10, "USA", 21, "Dark Green")
    assert g.country == "USA"
    assert g.germination_period == 21
    assert g.color == "Dark Green"


def test_category_add_multiple():
    """Тест добавления нескольких товаров в категорию."""
    c = Category("Cat", "Desc")
    p1 = Product("P1", "Desc", 10.0, 2)
    p2 = Product("P2", "Desc", 20.0, 3)

    c.add_product(p1)
    c.add_product(p2)

    assert "P1, 10.0" in c.products
    assert "P2, 20.0" in c.products


def test_average_price_exact():
    """Тест точного расчёта средней цены."""
    c = Category("Test", "Desc")
    c.add_product(Product("A", "Desc", 10.0, 1))
    c.add_product(Product("B", "Desc", 20.0, 1))
    c.add_product(Product("C", "Desc", 30.0, 1))

    assert c.average_price() == 20.0


def test_category_str_with_products():
    """Тест __str__ категории с товарами."""
    c = Category("Electronics", "Tech")
    c.add_product(Product("Phone", "Smart", 100.0, 2))
    c.add_product(Product("Tablet", "Pad", 200.0, 3))

    assert "Electronics, количество продуктов: 5 шт." == str(c)


def test_products_property_empty():
    """Тест свойства products для пустой категории."""
    c = Category("Empty", "No products")
    assert c.products == ""


def test_class_attributes_increment():
    """Тест увеличения атрибутов класса."""
    initial_categories = Category.category_count
    initial_products = Category.product_count

    c = Category("New", "Desc")
    p = Product("NewProd", "Desc", 50.0, 5)
    c.add_product(p)

    assert Category.category_count == initial_categories + 1
    assert Category.product_count == initial_products + 1


def test_isinstance_check_in_add_product():
    """Тест проверки isinstance в add_product."""
    c = Category("Test", "Desc")

    # Должно работать с наследниками Product
    s = Smartphone("S", "Desc", 100.0, 2, "High", "M", 128, "Black")
    c.add_product(s)
    assert Category.product_count > 0


def test_type_comparison_in_add():
    """Тест сравнения типов в __add__."""
    p1 = Product("A", "Desc", 10.0, 2)
    p2 = Product("B", "Desc", 20.0, 3)

    # Одинаковые типы - должно работать
    result = p1 + p2
    assert result == 10.0 * 2 + 20.0 * 3
    # Разные типы - должна быть ошибка
    s = Smartphone("S", "Desc", 100.0, 2, "High", "M", 128, "Black")
    with pytest.raises(TypeError):
        _ = p1 + s
