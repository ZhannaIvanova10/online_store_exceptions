# 🎯 Инструкция по проверке HTML отчета покрытия

## 📊 Отчет УЖЕ добавлен в репозиторий
**Коммит:** 86762bf  
**Ветка:** `homework/17.1-exceptions-fixed`  
**Папка:** `htmlcov/`  
**Главный файл:** `htmlcov/index.html`

## 🔍 Как проверить отчет:

### Способ 1: Через GitHub (рекомендуется)
1. **Перейдите по ссылке:**  
   https://github.com/ZhannaIvanova10/online_store_exceptions/tree/homework/17.1-exceptions-fixed/htmlcov

2. **Найдите файл `index.html`** в списке файлов

3. **Нажмите на `index.html`** → GitHub покажет содержимое

4. **Для корректного отображения:**
   - Нажмите кнопку **"Download"** (справа)
   - Сохраните файл на компьютер
   - Откройте сохраненный файл в браузере

### Способ 2: Скачать и открыть локально
```bash
# Клонировать репозиторий
git clone https://github.com/ZhannaIvanova10/online_store_exceptions

# Перейти в нужную ветку
cd online_store_exceptions
git checkout homework/17.1-exceptions-fixed

# Открыть отчет
start htmlcov/index.html  # Windows
open htmlcov/index.html   # Mac
xdg-open htmlcov/index.html  # Linux
📈 Что проверять в отчете:
1. Главная страница (index.html):
✅ Общее покрытие: 100%

✅ Statements: 197 (все покрыты)

✅ Файлы: все должны показывать 100%

2. Детальный отчет по src/main.py:
Нажмите на main_py.html или src/main.py в списке

Проверьте цветовую маркировку:

🟢 Зеленый - код выполнен в тестах

(Красных строк быть не должно - у нас 100% покрытие)

3. Ключевые участки для проверки:
Класс ZeroQuantityError (строки ~10-15)

Product.__init__() - проверка quantity == 0 (строки ~40-45)

Category.add_product() - проверка product.quantity == 0 (строки ~120-125)

🧪 Результаты тестирования:
text
$ py -m pytest --cov=src --cov-report=html
============================= test session starts =============================
75 passed in 4.93s
============================= 75 passed in 4.93s ==============================

Coverage: 100% (197 statements)
📁 Содержимое отчета:
index.html - главная страница

main_py.html - детали по src/main.py

*_py.html - отчеты по другим файлам

CSS/JS файлы для оформления

✅ Требование наставника ВЫПОЛНЕНО:
Выполнена команда: pytest --cov=src --cov-report=html

Отчет создан и доступен в репозитории

100% покрытие кода подтверждено

Все 75 тестов проходят
