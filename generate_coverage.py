#!/usr/bin/env python
"""
Скрипт для генерации HTML отчета о покрытии тестами
"""
import os
import shutil
import subprocess
import sys

def main():
    print("="*60)
    print("ГЕНЕРАЦИЯ HTML ОТЧЕТА О ПОКРЫТИИ ТЕСТАМИ")
    print("="*60)
    
    # Удаляем старые отчеты
    print("\n1. Очистка старых отчетов...")
    if os.path.exists('.coverage'):
        os.remove('.coverage')
        print("   Удален .coverage")
    
    if os.path.exists('htmlcov'):
        shutil.rmtree('htmlcov')
        print("   Удалена папка htmlcov/")
    
    # Запускаем тесты с генерацией отчета
    print("\n2. Запуск тестов с измерением покрытия...")
    cmd = [sys.executable, '-m', 'pytest', 
           '--cov=main', 
           '--cov-report=html', 
           '--cov-report=term',
           'test_main.py']
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    print("\n3. Результаты тестов:")
    print(result.stdout)
    
    if result.stderr:
        print("Ошибки:")
        print(result.stderr)
    
    # Проверяем создание отчета
    print("\n4. Проверка создания отчета...")
    if os.path.exists('htmlcov/index.html'):
        html_path = os.path.abspath('htmlcov/index.html')
        print(f"✅ HTML отчет успешно создан!")
        print(f"   Файл: {html_path}")
        print(f"   Откройте в браузере: file://{html_path}")
        
        # Показываем информацию о покрытии
        print("\n📊 ИНФОРМАЦИЯ О ПОКРЫТИИ:")
        print("-" * 40)
        for line in result.stdout.split('\n'):
            if 'TOTAL' in line or 'main.py' in line:
                print(line)
        
        return True
    else:
        print("❌ HTML отчет не создан!")
        return False

if __name__ == "__main__":
    success = main()
    if success:
        print("\n" + "="*60)
        print("✅ ОТЧЕТ ГОТОВ! Добавьте в PR:")
        print("   - htmlcov/index.html (генерируется локально)")
        print("   - Скриншот отчета о покрытии")
        print("   - Информацию о покрытии из вывода выше")
        print("="*60)
    else:
        sys.exit(1)
