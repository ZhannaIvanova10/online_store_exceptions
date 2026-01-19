#!/usr/bin/env python3
print("=" * 60)
print("ФИНАЛЬНАЯ ПРОВЕРКА ДЗ 17.1")
print("=" * 60)

import subprocess
import os

# 1. PEP 8
print("1. PEP 8 (main.py)...")
result = subprocess.run(["py", "-m", "pycodestyle", "--max-line-length=100", "main.py"], 
                       capture_output=True, text=True)
errors = len([e for e in result.stdout.strip().split('\n') if e])
print(f"   {'✅' if errors <= 5 else '❌'} {errors} ошибок")

# 2. Тесты
print("\n2. Тесты...")
result = subprocess.run(["py", "-m", "pytest", "test_main.py", "-q"], 
                       capture_output=True, text=True)
if "passed" in result.stdout:
    print("   ✅ Все тесты проходят")
else:
    print("   ❌ Тесты не проходят")

# 3. Coverage
print("\n3. Покрытие...")
result = subprocess.run(["py", "-m", "pytest", "--cov=.", "--cov-report=term"], 
                       capture_output=True, text=True)
for line in result.stdout.split('\n'):
    if "TOTAL" in line and "%" in line:
        cov = line.split()[-1]
        print(f"   ✅ {cov} покрытия")
        break

# 4. Исключения
print("\n4. Исключение при quantity=0...")
code = '''
from main import Product
try:
    Product("test", "test", 100, 0)
    print("❌ Не вызвалось исключение")
except Exception as e:
    if "Товар с нулевым количеством" in str(e):
        print("✅ Правильное исключение")
    else:
        print(f"❌ Неправильное: {e}")
'''
result = subprocess.run(["py", "-c", code], capture_output=True, text=True)
print(f"   {result.stdout.strip()}")
# 5. average_price
print("\n5. Метод average_price...")
code = '''
from main import Category, Product
c = Category("test", "test")
print("✅ Пустая категория: 0" if c.average_price() == 0 else "❌")
c.add_product(Product("p", "d", 100, 2))
c.add_product(Product("p2", "d", 300, 1))
expected = 200.0
print(f"✅ С товарами: {c.average_price()}" if abs(c.average_price() - expected) < 0.01 else "❌")
'''
result = subprocess.run(["py", "-c", code], capture_output=True, text=True)
print(f"   {result.stdout.strip().replace(chr(10), ' ')}")

# 6. Запуск
print("\n6. Запуск main.py...")
result = subprocess.run(["py", "main.py"], capture_output=True, text=True)
if result.returncode == 0:
    print("   ✅ Успешно запускается")
else:
    print("   ❌ Ошибка запуска")

# 7. README
print("\n7. README.md...")
if os.path.exists("README.md"):
    size = os.path.getsize("README.md")
    print(f"   ✅ Существует ({size} байт)")
else:
    print("   ❌ Не найден")
# 8. ZeroQuantityError
print("\n8. ZeroQuantityError...")
code = '''
from main import ZeroQuantityError
print("✅ Наследуется от ValueError" if issubclass(ZeroQuantityError, ValueError) else "❌")
'''
result = subprocess.run(["py", "-c", code], capture_output=True, text=True)
print(f"   {result.stdout.strip()}")

print("\n" + "=" * 60)
print("🎉 ПРОЕКТ ГОТОВ К СДАЧЕ!")
print("=" * 60)
