#!/usr/bin/env python3
"""
Демонстрационный скрипт для показа работы исключений
"""
from main import Product, Category, ZeroQuantityError


def demonstrate_exceptions():
    """Демонстрация работы исключений"""
    print("=" * 50)
    print("ДЕМОНСТРАЦИЯ ОБРАБОТКИ ИСКЛЮЧЕНИЙ")
    print("=" * 50)
    
    # 1. Демонстрация исключения при нулевом количестве
    print("\n1. Попытка создать товар с нулевым количеством:")
    print("-" * 40)
    try:
        bad_product = Product("Сломанный телефон", "Не работает", 10000, 0)
    except ZeroQuantityError as e:
        print(f"✗ Поймано исключение: {e}")
    else:
        print("✓ Товар создан успешно")
    # 2. Успешное создание товаров
    print("\n2. Создание корректных товаров:")
    print("-" * 40)
    try:
        product1 = Product("iPhone 15", "Смартфон Apple", 99990, 5)
        product2 = Product("MacBook Pro", "Ноутбук Apple", 199990, 3)
        product3 = Product("AirPods Pro", "Наушники Apple", 24990, 10)
        print("✓ Все товары созданы успешно")
    except ZeroQuantityError as e:
        print(f"✗ Ошибка: {e}")
    
    # 3. Создание категории и добавление товаров
    print("\n3. Создание категории и расчет средней цены:")
    print("-" * 40)
    category = Category("Apple", "Техника Apple")
    category.add_product(product1)
    category.add_product(product2)
    category.add_product(product3)
    
    print(f"Категория: {category}")
    print(f"Средняя цена товаров: {category.average_price():.2f} руб.")
    
    # 4. Демонстрация пустой категории
    print("\n4. Работа с пустой категорией:")
    print("-" * 40)
    empty_category = Category("Пустая", "Категория без товаров")
    print(f"Категория: {empty_category}")
    print(f"Средняя цена: {empty_category.average_price()} руб.")
    # 5. Вывод списка товаров
    print("\n5. Список товаров в категории:")
    print("-" * 40)
    print(category.products)
    
    print("\n" + "=" * 50)
    print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
    print("=" * 50)


def demonstrate_statistics():
    """Демонстрация статистики по категориям и товарам"""
    print("\n" + "=" * 50)
    print("СТАТИСТИКА")
    print("=" * 50)
    
    print(f"Всего создано категорий: {Category.category_count}")
    print(f"Всего создано товаров: {Category.product_count}")


if __name__ == "__main__":
    demonstrate_exceptions()
    demonstrate_statistics()
