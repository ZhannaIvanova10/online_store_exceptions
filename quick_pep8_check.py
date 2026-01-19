import subprocess

print("Быстрая проверка PEP 8")
print("=" * 50)

# Проверяем каждый файл отдельно
files = ["main.py", "test_main.py", "run.py"]
total_errors = 0

for file in files:
    print(f"\n{file}:")
    result = subprocess.run(
        ["python", "-m", "flake8", file, "--max-line-length=100", "--count"],
        capture_output=True,
        text=True
    )
    
    if result.stdout.strip():
        errors = int(result.stdout.strip())
        print(f"  ❌ {errors} ошибок")
        total_errors += errors
        # Показываем первые 3 ошибки
        show_result = subprocess.run(
            ["python", "-m", "flake8", file, "--max-line-length=100"],
            capture_output=True,
            text=True
        )
        for line in show_result.stdout.strip().split('\n')[:3]:
            print(f"    {line}")
    else:
        print("  ✅ Нет ошибок")

print(f"\n" + "=" * 50)
print(f"Всего ошибок: {total_errors}")

if total_errors <= 5:
    print("✅ КРИТЕРИЙ PEP 8 ВЫПОЛНЕН (<5 ошибок)")
else:
    print(f"❌ КРИТЕРИЙ PEP 8 НЕ ВЫПОЛНЕН ({total_errors} > 5)")
print("=" * 50)
