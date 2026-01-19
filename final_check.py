import sys
import subprocess

print("=" * 60)
print("ФИНАЛЬНАЯ ПРОВЕРКА 8 КРИТЕРИЕВ ДЗ 17.1")
print("=" * 60)

criteria_passed = 0
criteria_total = 8

print("\n1. Проверка исключения при нулевом количестве...")
try:
    from main import Product, ZeroQuantityError
    try:
        Product("Тест", "Описание", 100, 0)
        print("   ❌ FAIL")
    except ZeroQuantityError as e:
        if "Товар с нулевым количеством не может быть добавлен" in str(e):
            print("   ✅ PASS")
            criteria_passed += 1
        else:
            print(f"   ❌ FAIL: Неправильное сообщение")
except Exception as e:
    print(f"   ❌ FAIL: {e}")
print("\n2. Проверка метода average_price...")
try:
    from main import Category, Product
    cat = Category("Тест", "Тест")
    if cat.average_price() == 0:
        p1 = Product("Т1", "Д1", 100, 1)
        p2 = Product("Т2", "Д2", 200, 1)
        cat.add_product(p1)
        cat.add_product(p2)
        if cat.average_price() == 150:
            print("   ✅ PASS")
            criteria_passed += 1
        else:
            print(f"   ❌ FAIL: Неправильный расчет")
    else:
        print(f"   ❌ FAIL: Пустая категория не возвращает 0")
except Exception as e:
    print(f"   ❌ FAIL: {e}")

print("\n3. Проверка тестов...")
result = subprocess.run([sys.executable, "-m", "pytest", "test_main.py", "-q"], 
                       capture_output=True, text=True)
if result.returncode == 0:
    print("   ✅ PASS (Все тесты проходят)")
    criteria_passed += 1
else:
    print("   ❌ FAIL")

print("\n4. Проверка покрытия тестами (>75%)...")
result = subprocess.run([sys.executable, "-m", "pytest", "--cov=main", "test_main.py", "-q"],
                       capture_output=True, text=True)
import re
coverage = 0
for line in result.stdout.split('\n'):
    if 'TOTAL' in line:
        match = re.search(r'(\d+)%', line)
        if match:
            coverage = int(match.group(1))
            break
if coverage >= 75:
    print(f"   ✅ PASS (Покрытие: {coverage}%)")
    criteria_passed += 1
else:
    print(f"   ❌ FAIL (Покрытие: {coverage}%)")

print("\n5. Проверка запуска кода без ошибок...")
try:
    exec(open("main.py").read())
    print("   ✅ PASS")
    criteria_passed += 1
except Exception as e:
    print(f"   ❌ FAIL: {e}")

print("\n6. Проверка README...")
try:
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()
    if len(content.strip()) > 100:
        print("   ✅ PASS (README не пустой)")
        criteria_passed += 1
    else:
        print("   ❌ FAIL (README слишком короткий)")
except:
    print("   ❌ FAIL (README не найден)")
print("\n7. Проверка пользовательского исключения...")
try:
    from main import ZeroQuantityError
    if issubclass(ZeroQuantityError, ValueError):
        print("   ✅ PASS")
        criteria_passed += 1
    else:
        print("   ❌ FAIL (Не наследуется от ValueError)")
except:
    print("   ❌ FAIL (Исключение не найдено)")

print("\n8. Проверка PEP 8 (<5 ошибок)...")
result = subprocess.run([sys.executable, "-m", "flake8", "main.py", "test_main.py", "run.py", 
                        "--count", "--max-line-length=100"], capture_output=True, text=True)
error_count = 0
for line in result.stdout.split('\n'):
    if line and line[0].isdigit():
        error_count += int(line.split()[0])
if error_count <= 5:
    print(f"   ✅ PASS (Ошибок: {error_count})")
    criteria_passed += 1
else:
    print(f"   ❌ FAIL (Ошибок: {error_count})")

print("\n" + "=" * 60)
print(f"РЕЗУЛЬТАТ: {criteria_passed}/{criteria_total} критериев")

if criteria_passed == criteria_total:
    print("🎉 ВСЕ КРИТЕРИИ ВЫПОЛНЕНЫ!")
    print("Проект готов к сдаче!")
else:
    print(f"⚠️  Нужно исправить {criteria_total - criteria_passed} критериев")
print("=" * 60)
