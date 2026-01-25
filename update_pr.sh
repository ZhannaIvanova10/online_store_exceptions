#!/bin/bash
echo "🔄 ОБНОВЛЕНИЕ PR ДЗ 17.1"
echo "========================"

# 1. Обновляем HTML отчет
echo "1. Обновление HTML отчета..."
rm -rf htmlcov 2>/dev/null
py -m pytest --cov=main --cov-report=html test_main.py -q
echo "   ✅ HTML отчет обновлен"

# 2. Создаем финальное описание
echo "2. Создание финального описания..."
cat > PR_FINAL_FULL.md << 'EOF'
$(cat FULL_PR_README.md)
EOF
echo "   ✅ Описание создано"

# 3. Копируем в буфер обмена
echo "3. Копирование в буфер обмена..."
cat PR_FINAL_FULL.md | clip
echo "   ✅ Скопировано в буфер обмена"

# 4. Инструкция
echo ""
echo "🎯 ИНСТРУКЦИЯ:"
echo "1. Откройте: https://github.com/ZhannaIvanova10/online_store_exceptions/pull/1"
echo "2. Нажмите 'Edit' на PR"
echo "3. Вставьте содержимое (Ctrl+V)"
echo "4. Сохраните"
echo "5. Добавьте комментарий: @преподаватель Работа готова к проверке!"
echo ""
echo "✅ ВСЕ ГОТОВО ДЛЯ СДАЧИ!"
