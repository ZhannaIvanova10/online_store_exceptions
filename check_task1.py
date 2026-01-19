print("ТЕСТ ЗАДАНИЯ 1: Исключение при нулевом количестве")
print("=" * 60)

# Импортируем модуль
try:
    from main import Product, ZeroQuantityError
    print("✅ Модуль main импортирован успешно")
except ImportError as e:
    print(f"❌ Ошибка импорта: {e}")
    exit(1)

# Тест 1: Проверяем, что исключение выбрасывается при quantity=0
print("\n--- Тест 1: quantity=0 ---")
try:
    product = Product("Тестовый товар", "Описание", 100.0, 0)
    print("❌ ОШИБКА: Исключение не было вызвано!")
    print(f"   Создан товар: {product}")
except ZeroQuantityError as e:
    print(f"✅ Вызвано ZeroQuantityError")
    error_msg = str(e)
    print(f"   Сообщение: '{error_msg}'")
    
    # Проверяем точное сообщение
    expected = "Товар с нулевым количеством не может быть добавлен"
    if expected in error_msg:
        print(f"✅ Сообщение корректно содержит: '{expected}'")
    else:
        print(f"❌ Ожидалось: '{expected}'")
        print(f"   Получено: '{error_msg}'")
except Exception as e:
    print(f"❌ Вызвано другое исключение: {type(e).__name__}: {e}")
# Тест 2: Проверяем, что товар создается при quantity>0
print("\n--- Тест 2: quantity>0 ---")
try:
    product = Product("Смартфон", "Новый", 50000.0, 5)
    print(f"✅ Товар создан успешно")
    print(f"   Название: {product.name}")
    print(f"   Цена: {product.price}")
    print(f"   Количество: {product.quantity}")
    
    if product.quantity == 5:
        print("✅ Количество установлено правильно")
    else:
        print(f"❌ Количество {product.quantity}, ожидалось 5")
except Exception as e:
    print(f"❌ Ошибка при создании: {e}")

# Тест 3: Проверяем строковое представление
print("\n--- Тест 3: __str__ метод ---")
try:
    product = Product("Наушники", "Беспроводные", 5000.0, 3)
    str_repr = str(product)
    expected = "Наушники, 5000.0 руб. Остаток: 3 шт."
    
    print(f"   str(product) = '{str_repr}'")
    print(f"   Ожидалось:   '{expected}'")
    
    if str_repr == expected:
        print("✅ Строковое представление корректно")
    else:
        print("❌ Строковое представление неверное")
except Exception as e:
    print(f"❌ Ошибка: {e}")

print("\n" + "=" * 60)
print("ТЕСТ ЗАДАНИЯ 1 ЗАВЕРШЕН")
