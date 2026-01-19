print("ТЕСТ ЗАДАНИЯ 2: Метод average_price")
print("=" * 60)

# Импортируем модуль
try:
    from main import Product, Category
    print("✅ Модуль main импортирован успешно")
except ImportError as e:
    print(f"❌ Ошибка импорта: {e}")
    exit(1)

# Тест 1: Проверяем наличие метода average_price
print("\n--- Тест 1: Наличие метода ---")
if hasattr(Category, 'average_price'):
    print("✅ Метод average_price существует в классе Category")
else:
    print("❌ Метод average_price не найден!")
    exit(1)
# Тест 2: Пустая категория (должен вернуть 0)
print("\n--- Тест 2: Пустая категория ---")
empty_cat = Category("Пустая категория", "Нет товаров")
result = empty_cat.average_price()
print(f"   Категория: '{empty_cat.name}'")
print(f"   average_price() = {result}")

if result == 0:
    print("✅ Метод возвращает 0 для пустой категории")
else:
    print(f"❌ Ожидалось 0, получено {result}")

# Тест 3: Категория с одним товаром
print("\n--- Тест 3: Один товар ---")
cat1 = Category("Один товар", "Тест")
try:
    p1 = Product("Товар1", "Описание", 1500.0, 2)
    cat1.add_product(p1)
    result = cat1.average_price()
    print(f"   Добавлен: {p1.name} за {p1.price} руб.")
    print(f"   average_price() = {result}")
    
    if result == 1500.0:
        print("✅ Средняя цена правильная: 1500.0")
    else:
        print(f"❌ Ожидалось 1500.0, получено {result}")
except Exception as e:
    print(f"❌ Ошибка: {e}")

# Тест 4: Категория с несколькими товарами
print("\n--- Тест 4: Несколько товаров ---")
cat2 = Category("Несколько товаров", "Тест")
try:
    p2 = Product("Товар2", "Описание", 1000.0, 1)
    p3 = Product("Товар3", "Описание", 2000.0, 1)
    p4 = Product("Товар4", "Описание", 3000.0, 1)
    
    cat2.add_product(p2)
    cat2.add_product(p3)
    cat2.add_product(p4)
    
    result = cat2.average_price()
    expected = (1000 + 2000 + 3000) / 3  # 2000.0
    
    print(f"   Товары: {p2.price}, {p3.price}, {p4.price} руб.")
    print(f"   average_price() = {result}")
    print(f"   Ожидалось: {expected}")
    
    if abs(result - expected) < 0.001:
        print("✅ Средняя цена рассчитана правильно")
    else:
        print(f"❌ Неправильный расчет!")
except Exception as e:
    print(f"❌ Ошибка: {e}")

# Тест 5: Товары с нулевой ценой
print("\n--- Тест 5: Товары с нулевой ценой ---")
cat3 = Category("Нулевые цены", "Тест")
try:
    p5 = Product("Бесплатный", "Описание", 0.0, 5)
    p6 = Product("Еще один", "Описание", 0.0, 3)
    cat3.add_product(p5)
    cat3.add_product(p6)
    
    result = cat3.average_price()
    print(f"   average_price() = {result}")
    
    if result == 0.0:
        print("✅ Средняя цена 0 для товаров с нулевой ценой")
    else:
        print(f"❌ Ожидалось 0.0, получено {result}")
except Exception as e:
    print(f"❌ Ошибка: {e}")

print("\n" + "=" * 60)
print("ТЕСТ ЗАДАНИЯ 2 ЗАВЕРШЕН")
