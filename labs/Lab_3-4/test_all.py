import os
from pathlib import Path

# Запуск всех файлов
files = [
    'field.py', 'gen_random.py', 'unique.py', 'sort.py',
    'print_result.py', 'cm_timer.py', 'process_data.py'
]

print("=== ЛАБОРАТОРНАЯ РАБОТА №3-4 ===")
print("Функциональные возможности Python\n")

for file in files:
    file_path = Path(__file__).parent / file
    if file_path.exists():
        print(f"\n{'='*50}")
        print(f"ТЕСТ: {file}")
        print('='*50)
        os.system(f'python {file}')
    else:
        print(f"❌ Файл {file} не найден")

print("\n✅ Все тесты завершены!")
