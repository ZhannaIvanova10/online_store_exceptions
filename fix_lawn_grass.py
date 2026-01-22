# Исправляем опечатку в main.py
with open('main.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Меняем "из Россия" на "из России"
content = content.replace('из Россия', 'из России')

with open('main.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("✅ Исправлено: 'из Россия' → 'из России'")
