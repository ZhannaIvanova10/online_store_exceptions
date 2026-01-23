## 🧪 КОМАНДЫ ДЛЯ ПРОВЕРКИ (используйте py вместо python):

### Запуск тестов:
```bash
# Все тесты с подробным выводом
py -m pytest test_main.py -v

# Только тесты ДЗ 17.1
py -m pytest test_main.py -v -k "zero or average or error"

# Быстрая проверка
py -m pytest test_main.py -q
Проверка покрытия:
bash
# Текстовый отчет
py -m pytest --cov=main --cov-report=term-missing test_main.py

# HTML отчет (визуализация)
py -m pytest --cov=main --cov-report=html test_main.py
# Затем откройте htmlcov/index.html в браузере
Быстрая функциональная проверка:
bash
py -c "
from main import Product, Category, ZeroQuantityError

# Проверка ZeroQuantityError
try:
    Product('Тест', 'Описание', 100, 0)
except ZeroQuantityError as e:
    print(f'✅ ZeroQuantityError: {e}')

# Проверка average_price()
c = Category('Тест', 'Описание')
print(f'✅ Пустая категория: {c.average_price()}')
"
