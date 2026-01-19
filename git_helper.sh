#!/bin/bash
# Скрипт-помощник для работы с GitFlow в учебном проекте

echo "=== GitFlow Helper для интернет-магазина ==="
echo ""

case "$1" in
    "init")
        echo "Инициализация структуры веток:"
        echo "1. main - стабильная ветка"
        echo "2. develop - ветка разработки"
        echo "3. homework/* - ветки для ДЗ"
        ;;
    
    "hw-start")
        if [ -z "$2" ]; then
            echo "Использование: ./git_helper.sh hw-start <номер-дз>"
            echo "Пример: ./git_helper.sh hw-start 17.1"
        else
            git checkout develop
            git checkout -b "homework/$2"
            echo "Создана ветка homework/$2"
        fi
        ;;
    "hw-finish")
        if [ -z "$2" ]; then
            echo "Использование: ./git_helper.sh hw-finish <описание>"
            echo "Пример: ./git_helper.sh hw-finish 'Реализация исключений'"
        else
            git add .
            git commit -m "$2"
            echo "Изменения закоммичены. Создайте пул-реквест в develop!"
        fi
        ;;
    
    "status")
        echo "Текущая ветка: $(git branch --show-current)"
        echo ""
        echo "Все ветки домашних заданий:"
        git branch | grep homework
        ;;
    
    "merge-to-develop")
        current_branch=$(git branch --show-current)
        if [[ $current_branch == homework/* ]]; then
            git checkout develop
            git merge --no-ff "$current_branch" -m "Merge $current_branch into develop"
            echo "Ветка $current_branch успешно вмержена в develop"
        else
            echo "Вы не в ветке домашнего задания!"
        fi
        ;;
    
    *)

        echo "Доступные команды:"
        echo "  init               - показать структуру веток"
        echo "  hw-start <номер>   - начать новое ДЗ"
        echo "  hw-finish <описание> - завершить ДЗ"
        echo "  status             - показать статус веток"
        echo "  merge-to-develop   - вмержить текущую ветку в develop"
        ;;
esac
