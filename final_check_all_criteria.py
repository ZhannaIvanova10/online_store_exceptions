import re
import sys
import subprocess
import os

print("=" * 60)
print("ФИНАЛЬНАЯ ПРОВЕРКА ВСЕХ 8 КРИТЕРИЕВ ДЗ 17.1")
print("=" * 60)

print("\n📋 Проверяемые критерии:")
print("1. Исключение при нулевом количестве")
print("2. Метод average_price с обработкой ZeroDivisionError")
print("3. Тесты выполняются без ошибок")
print("4. Покрытие тестами >75%")
print("5. Весь код запускается без ошибок")
print("6. README с информацией о проекте")
print("7. Пользовательское исключение ZeroQuantityError")
print("8. Соответствие PEP 8 (<5 ошибок)")

print("\n" + "=" * 60)
print("РЕЗУЛЬТАТЫ ПРОВЕРКИ:")
print("=" * 60)

all_passed = True
results = []
# Критерий 1
print("\n1. Исключение при нулевом количестве...")
try:
    from main import Product, ZeroQuantityError
    try:
        Product("Тест", "Описание", 100, 0)
        print("   ❌ FAIL: Исключение не вызвано")
        results.append(("1. Исключение", False))
        all_passed = False
    except ZeroQuantityError as e:
        if "Товар с нулевым количеством не может быть добавлен" in str(e):
            print("   ✅ PASS: Исключение с правильным сообщением")
            results.append(("1. Исключение", True))
        else:
            print(f"   ❌ FAIL: Неправильное сообщение")
            results.append(("1. Исключение", False))
            all_passed = False
    except Exception as e:
        print(f"   ❌ FAIL: Другое исключение: {type(e).__name__}")
        results.append(("1. Исключение", False))
        all_passed = False
except Exception as e:
    print(f"   ❌ FAIL: Ошибка импорта: {e}")
    results.append(("1. Исключение", False))
    all_passed = False

# Критерий 2
print("\n2. Метод average_price...")
try:
    from main import Category, Product
    cat = Category("Тест", "Тест")
    if cat.average_price() == 0:
        p1 = Product("Т1", "Д1", 100, 1)
        p2 = Product("Т2", "Д2", 200, 1)
        cat.add_product(p1)
        cat.add_product(p2)
        if cat.average_price() == 150:
            print("   ✅ PASS: Метод работает корректно")
            results.append(("2. average_price", True))
        else:
            print(f"   ❌ FAIL: Неправильный расчет: {cat.average_price()}")
            results.append(("2. average_price", False))
            all_passed = False
    else:
        print(
            f"   ❌ FAIL: Пустая категория не возвращает 0: {
                cat.average_price()}")
        results.append(("2. average_price", False))
        all_passed = False
except Exception as e:
    print(f"   ❌ FAIL: {e}")
    results.append(("2. average_price", False))
    all_passed = False
# Критерий 3
print("\n3. Тесты...")
result = subprocess.run([sys.executable, "-m", "pytest", "test_main.py", "-q"],
                        capture_output=True, text=True)
if result.returncode == 0:
    print(
        f"   ✅ PASS: Все тесты проходят ({
            result.stdout.count('passed')} passed)")
    results.append(("3. Тесты", True))
else:
    print("   ❌ FAIL: Тесты не проходят")
    results.append(("3. Тесты", False))
    all_passed = False

# Критерий 4
print("\n4. Покрытие тестами...")
result = subprocess.run([sys.executable, "-m", "pytest", "--cov=main", "test_main.py", "-q"],
                        capture_output=True, text=True)
coverage = 0
for line in result.stdout.split('\n'):
    if 'TOTAL' in line:
        match = re.search(r'(\d+)%', line)
        if match:
            coverage = int(match.group(1))
            break
if coverage >= 75:
    print(f"   ✅ PASS: Покрытие {coverage}% (>75%)")
    results.append(("4. Покрытие", True))
else:
    print(f"   ❌ FAIL: Покрытие {coverage}% (<75%)")
    results.append(("4. Покрытие", False))
    all_passed = False

# Критерий 5
print("\n5. Запуск кода без ошибок...")
try:
    # Безопасный способ проверить запуск
    with open("main.py", "r", encoding="utf-8") as f:
        exec(f.read())
    print("   ✅ PASS: main.py запускается без ошибок")
    results.append(("5. Запуск кода", True))
except Exception as e:
    print(f"   ❌ FAIL: {type(e).__name__}: {e}")
    results.append(("5. Запуск кода", False))
    all_passed = False

# Критерий 6
print("\n6. README...")
try:
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()
    if len(content.strip()) > 100 and (
            "17.1" in content or "исключени" in content.lower()):
        print(
            f"   ✅ PASS: README содержит информацию ({
                len(content)} символов)")
        results.append(("6. README", True))
    else:
        print(f"   ❌ FAIL: README не содержит нужной информации")
        results.append(("6. README", False))
        all_passed = False
except Exception as e:
    print(f"   ❌ FAIL: {e}")
    results.append(("6. README", False))
    all_passed = False
# Критерий 7
print("\n7. Пользовательское исключение...")
try:
    from main import ZeroQuantityError
    if issubclass(ZeroQuantityError, ValueError):
        print("   ✅ PASS: ZeroQuantityError наследуется от ValueError")
        results.append(("7. Пользовательское исключение", True))
    else:
        print("   ❌ FAIL: Не наследуется от ValueError")
        results.append(("7. Пользовательское исключение", False))
        all_passed = False
except Exception as e:
    print(f"   ❌ FAIL: {e}")
    results.append(("7. Пользовательское исключение", False))
    all_passed = False

# Критерий 8
print("\n8. PEP 8...")
result = subprocess.run([sys.executable, "-m", "flake8", "main.py", "test_main.py", "run.py",
                        "--count", "--max-line-length=100"], capture_output=True, text=True)
error_count = 0
for line in result.stdout.split('\n'):
    if line and line[0].isdigit():
        error_count += int(line.split()[0])
if error_count <= 5:
    print(f"   ✅ PASS: {error_count} ошибок (<5)")
    results.append(("8. PEP 8", True))
else:
    print(f"   ❌ FAIL: {error_count} ошибок (>5)")
    results.append(("8. PEP 8", False))
    all_passed = False
print("\n" + "=" * 60)
print("ИТОГИ:")
print("=" * 60)

passed = sum(1 for _, status in results if status)
total = len(results)

for name, status in results:
    symbol = "✅" if status else "❌"
    print(f"{symbol} {name}")

print(f"\n📊 Выполнено: {passed}/{total} критериев")

if all_passed:
    print("\n🎉 ВСЕ 8 КРИТЕРИЕВ ВЫПОЛНЕНЫ!")
    print("Проект полностью готов к сдаче!")
else:
    print(f"\n⚠️  Нужно исправить: {total - passed} критериев")
print("=" * 60)
