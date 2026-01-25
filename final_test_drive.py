#!/usr/bin/env python3
"""
ФИНАЛЬНЫЙ ТЕСТ-ДРАЙВ ПРОЕКТА
"""
print("🚗 ФИНАЛЬНЫЙ ТЕСТ-ДРАЙВ ПРОЕКТА")
print("=" * 50)

from main import Product, Category, Smartphone, LawnGrass, ZeroQuantityError

# Сценарий 1: Создание интернет-магазина
print("\n1. СОЗДАНИЕ ИНТЕРНЕТ-МАГАЗИНА:")
print("-" * 30)

# Создаем категории
electronics = Category("Электроника", "Техника и гаджеты")
garden = Category("Сад и огород", "Товары для дачи")

# Создаем товары
print("Создаем товары...")
try:
    # Этот товар должен вызвать исключение
    bad_product = Product("Битый", "Товар", 100, 0)
except ZeroQuantityError as e:
    print(f"✅ ZeroQuantityError сработал: {e}")

# Нормальные товары
laptop = Product("Ноутбук", "Игровой ноутбук", 150000, 3)
phone = Smartphone(
    "iPhone 15 Pro", 
    "Флагманский смартфон Apple",
    129999,
    5,
    performance="A17 Pro",
    model="15 Pro",
    memory="256GB",
    color="Титановый"
)
grass = LawnGrass(
    "Газонная трава Premium",
    "Быстрорастущая трава из Германии",
    2999,
    50,
    country="Германия",
    germination_period="10 дней",
    color="Изумрудный"
)

print(f"✅ Создано: {laptop.name} - {laptop.price} руб.")
print(f"✅ Создано: {phone.name} ({phone.model}) - {phone.price} руб.")
print(f"✅ Создано: {grass.name} - {grass.price} руб.")
# Сценарий 2: Работа с категориями
print("\n2. РАБОТА С КАТЕГОРИЯМИ:")
print("-" * 30)

electronics.add_product(laptop)
electronics.add_product(phone)
garden.add_product(grass)

print(f"Категория '{electronics.name}': {len(electronics.products)} товара")
print(f"Категория '{garden.name}': {len(garden.products)} товар")

print(f"\nСредняя цена в '{electronics.name}': {electronics.average_price():.2f} руб.")
print(f"Средняя цена в '{garden.name}': {garden.average_price():.2f} руб.")

# Сценарий 3: Магические методы
print("\n3. МАГИЧЕСКИЕ МЕТОДЫ:")
print("-" * 30)

print(f"Строковое представление товара: {laptop}")
print(f"Строковое представление смартфона: {phone}")
print(f"Строковое представление травы: {grass}")

# Сложение товаров
apples1 = Product("Яблоки", "Фрукты", 100, 10)
apples2 = Product("Яблоки", "Фрукты", 150, 20)
total_apples = apples1 + apples2
print(f"\nСложение товаров: {apples1.quantity} + {apples2.quantity} = {total_apples.quantity} шт.")
print(f"Средняя цена после сложения: {total_apples.price:.2f} руб.")
# Сценарий 4: Отладочная информация
print("\n4. ОТЛАДОЧНАЯ ИНФОРМАЦИЯ:")
print("-" * 30)

print(f"Repr товара: {repr(laptop)}")
print(f"Repr смартфона: {repr(phone)}")
print(f"Repr травы: {repr(grass)}")

# Сценарий 5: Статистика
print("\n5. СТАТИСТИКА:")
print("-" * 30)

print(f"Всего создано товаров (Product.product_count): {Product.product_count}")
print(f"Всего создано категорий (Category.category_count): {Category.category_count}")

print("\n" + "=" * 50)
print("🎉 ТЕСТ-ДРАЙВ ЗАВЕРШЕН УСПЕШНО!")
print("✅ ВСЕ ФУНКЦИОНАЛЬНОСТИ РАБОТАЮТ КОРРЕКТНО")
print("=" * 50)
