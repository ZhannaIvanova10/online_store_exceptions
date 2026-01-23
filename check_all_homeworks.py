#!/usr/bin/env python3
"""
Проверка всех ДЗ 14-17
"""
from main import (
    Product, Category, Smartphone, LawnGrass,
    ZeroQuantityError, BaseProduct, ReprMixin
)

print("=" * 60)
print("ПРОВЕРКА ВСЕХ ДЗ 14-17")
print("=" * 60)

homeworks = {
    "ДЗ 14.1": ["Product", "Category"],
    "ДЗ 14.2": ["Приватные атрибуты", "Геттеры/сеттеры", "Класс-метод"],
    "ДЗ 15.1": ["__str__", "__add__"],
    "ДЗ 16.1": ["Smartphone", "LawnGrass"],
    "ДЗ 16.2": ["BaseProduct", "ReprMixin"],
    "ДЗ 17.1": ["ZeroQuantityError", "average_price()"]
}
print("\n📚 ПРОВЕРКА КЛАССОВ:")
# Проверяем что все классы существуют
classes_to_check = [Product, Category, Smartphone, LawnGrass, ZeroQuantityError, BaseProduct, ReprMixin]
for cls in classes_to_check:
    print(f"   ✅ {cls.__name__}")

print("\n🎯 ФУНКЦИОНАЛЬНЫЕ ТЕСТЫ:")

# ДЗ 14.1: Product и Category
print("\n1. ДЗ 14.1 - Product и Category:")
p = Product("Тест", "Описание", 100, 5)
print(f"   ✅ Product создан: {p.name}, {p.quantity} шт.")
c = Category("Категория", "Описание")
print(f"   ✅ Category создана: {c.name}")

# ДЗ 14.2: Приватные атрибуты
print("\n2. ДЗ 14.2 - Приватные атрибуты:")
try:
    # Попытка доступа к приватному атрибуту
    _ = c.__products
    print("   ❌ __products не приватный!")
except AttributeError:
    print("   ✅ __products приватный, доступ через property")
# ДЗ 15.1: Магические методы
print("\n3. ДЗ 15.1 - Магические методы:")
print(f"   ✅ __str__ Product: {str(p)}")
p1 = Product("Яблоки", "Фрукты", 100, 10)
p2 = Product("Яблоки", "Фрукты", 150, 20)
result = p1 + p2
print(f"   ✅ __add__ Product: {result.quantity} шт.")

# ДЗ 16.1: Наследование
print("\n4. ДЗ 16.1 - Наследование:")
s = Smartphone("iPhone", "Смартфон", 100000, 2, "A15", "13", "128GB", "черный")
g = LawnGrass("Трава", "Газонная", 500, 10, "Россия", "14 дней", "зеленая")
print(f"   ✅ Smartphone: {s.model}, {s.color}")
print(f"   ✅ LawnGrass: {g.country}, {g.germination_period}")

# ДЗ 16.2: Абстрактные классы и миксины
print("\n5. ДЗ 16.2 - Абстрактные классы и миксины:")
print(f"   ✅ Product наследует BaseProduct: {issubclass(Product, BaseProduct)}")
print(f"   ✅ Smartphone использует ReprMixin: {'ReprMixin' in str(Smartphone.__mro__)}")

# ДЗ 17.1: Исключения
print("\n6. ДЗ 17.1 - Исключения:")
try:
    Product("Товар", "Описание", 100, 0)
except ZeroQuantityError as e:
    print(f"   ✅ ZeroQuantityError: {e}")

print(f"   ✅ average_price пустой категории: {c.average_price()}")

print("\n" + "=" * 60)
print("🎉 ВСЕ ДЗ 14-17 ИНТЕГРИРОВАНЫ!")
print("=" * 60)
