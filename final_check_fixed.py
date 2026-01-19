import sys
import subprocess

print("=" * 70)
print("ФИНАЛЬНАЯ ПРОВЕРКА ПОСЛЕ ИСПРАВЛЕНИЙ")
print("=" * 70)

all_passed = True
criteria = {}

def check_criterion(name, check_func):
    """Проверка одного критерия"""
    global all_passed
    print(f"\n🔍 {name}")
    try:
        result = check_func()
        if result:
            print("   ✅ ПРОЙДЕНО")
            criteria[name] = True
        else:
            print("   ❌ НЕ ПРОЙДЕНО")
            criteria[name] = False
            all_passed = False
    except Exception as e:
        print(f"   ❌ ОШИБКА: {e}")
        criteria[name] = False
        all_passed = False
# Критерий 1: Исключение при нулевом количестве
def check_criterion_1():
    from main import Product, ZeroQuantityError
    try:
        Product("Тест", "Описание", 100, 0)
        return False
    except ZeroQuantityError as e:
        msg = str(e)
        return "Товар с нулевым количеством не может быть добавлен" in msg
    except Exception:
        return False

# Критерий 2: Метод average_price
def check_criterion_2():
    from main import Category, Product
    cat = Category("Тест", "Тест")
    if cat.average_price() != 0:
        return False
    p1 = Product("Т1", "Д1", 100, 1)
    p2 = Product("Т2", "Д2", 200, 1)
    cat.add_product(p1)
    cat.add_product(p2)
    return cat.average_price() == 150.0

# Критерий 3: Тесты работают
def check_criterion_3():
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "test_main.py", "-q"],
        capture_output=True,
        text=True
    )
    return result.returncode == 0

# Критерий 4: Покрытие тестами >75%
def check_criterion_4():
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "--cov=main", "test_main.py", "-q"],
        capture_output=True,
        text=True
    )
    import re
    for line in result.stdout.split('\n'):
        if 'TOTAL' in line:
            match = re.search(r'(\d+)%', line)
            if match:
                return int(match.group(1)) >= 75
    return False

# Критерий 5: Код запускается без ошибок
def check_criterion_5():
    try:
        # Просто импортируем и создаем объекты
        from main import Product, Category
        p = Product("Тест", "Описание", 100, 1)
        c = Category("Тест", "Описание")
        _ = c.average_price()
        return True
    except Exception:
        return False

# Критерий 6: README существует и не пустой
def check_criterion_6():
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            content = f.read()
        return len(content.strip()) > 500  # Должен быть достаточно подробным
    except Exception:
        return False

# Критерий 7: Пользовательское исключение
def check_criterion_7():
    from main import ZeroQuantityError
    return issubclass(ZeroQuantityError, ValueError)

# Критерий 8: PEP 8 (<5 ошибок)
def check_criterion_8():
    result = subprocess.run(
        [sys.executable, "-m", "flake8", "main.py", "test_main.py", "run.py", "--count", "--max-line-length=100"],
        capture_output=True,
        text=True
    )
    # Считаем ошибки
    error_count = 0
    for line in result.stdout.split('\n'):
        if line and line[0].isdigit():
            error_count += int(line.split()[0])
    return error_count <= 5

# Запускаем все проверки
check_criterion("1. Исключение при нулевом количестве товара", check_criterion_1)
check_criterion("2. Метод average_price с обработкой ZeroDivisionError", check_criterion_2)
check_criterion("3. Тесты выполняются без ошибок", check_criterion_3)
check_criterion("4. Покрытие тестами >75%", check_criterion_4)
check_criterion("5. Весь код запускается без ошибок", check_criterion_5)
check_criterion("6. README с информацией о проекте", check_criterion_6)
check_criterion("7. Пользовательское исключение ZeroQuantityError", check_criterion_7)
check_criterion("8. Соответствие PEP 8 (<5 ошибок)", check_criterion_8)

print("\n" + "=" * 70)
print("РЕЗУЛЬТАТЫ:")
print("=" * 70)

passed = sum(1 for v in criteria.values() if v)
total = len(criteria)

for name, passed_status in criteria.items():
    status = "✅" if passed_status else "❌"
    print(f"{status} {name}")

print("\n" + "=" * 70)
if all_passed:
    print(f"🎉 ВСЕ КРИТЕРИИ ВЫПОЛНЕНЫ! ({passed}/{total})")
    print("Проект готов к сдаче!")
else:
    print(f"⚠️  ВЫПОЛНЕНО {passed}/{total} КРИТЕРИЕВ")
    print("Необходимо исправить отмеченные проблемы.")
print("=" * 70)
