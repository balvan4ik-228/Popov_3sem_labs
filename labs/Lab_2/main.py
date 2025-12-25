import sys
import os
import math

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from rectangle import Rectangle
from circle import Circle
from square import Square

try:
    from colorama import init, Fore, Back, Style
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False
    Fore = Back = Style = None  # Инициализируем пустыми для избежания ошибок


def print_colored(text, color="WHITE", style="NORMAL"):
    """Выводит текст цветом, если colorama доступен"""
    if COLORAMA_AVAILABLE and Fore and Style:
        try:
            color_obj = getattr(Fore, color.upper(), Fore.WHITE)
            style_obj = getattr(Style, style.upper(), Style.NORMAL)
            print(f"{style_obj}{color_obj}{text}{Style.RESET_ALL}")
        except (AttributeError, KeyError):
            print(text)
    else:
        print(text)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_user_input(prompt, input_type=float):
    while True:
        try:
            value = input(prompt)
            if value.lower() in ['выход', 'exit', 'quit']:
                return None
            return input_type(value)
        except ValueError:
            print_colored("Ошибка: введите корректное число!", "RED")
        except KeyboardInterrupt:
            print("\n\nПрограмма прервана пользователем.")
            sys.exit(0)


def test_rectangle_interactive():
    clear_screen()
    print_colored("=" * 60, "CYAN")
    print_colored("ИНТЕРАКТИВНАЯ ПРОВЕРКА: ПРЯМОУГОЛЬНИК", "YELLOW", "BRIGHT")
    print_colored("=" * 60, "CYAN")

    print("\nВведите параметры для проверки:")
    print("(или введите 'выход' для возврата в меню)")

    width = get_user_input("Ширина прямоугольника: ")
    if width is None: return

    height = get_user_input("Высота прямоугольника: ")
    if height is None: return

    color = input("Цвет прямоугольника (например: синий): ").strip()
    if color.lower() in ['выход', 'exit', 'quit']: return

    print_colored("\n" + "-" * 60, "MAGENTA")
    user_area = get_user_input("Ваше предположение о площади прямоугольника: ")
    if user_area is None: return

    rectangle = Rectangle(width, height, color)
    program_area = rectangle.area()

    print_colored("\n" + "=" * 60, "CYAN")
    print_colored("РЕЗУЛЬТАТЫ СРАВНЕНИЯ:", "YELLOW")
    print_colored("=" * 60, "CYAN")

    print(f"Параметры: {width} × {height}, цвет: {color}")
    print(f"Ваш ответ: {user_area:.2f}")
    print(f"Ответ программы: {program_area:.2f}")

    if math.isclose(user_area, program_area, rel_tol=1e-9):
        print_colored(f"✓ ВЕРНО! Площадь прямоугольника: {program_area:.2f}", "GREEN")
    else:
        print_colored(f"✗ НЕВЕРНО. Правильный ответ: {program_area:.2f}", "RED")
        difference = abs(user_area - program_area)
        print(f"Разница: {difference:.2f}")

    input("\nНажмите Enter для продолжения...")


def test_circle_interactive():
    clear_screen()
    print_colored("=" * 60, "CYAN")
    print_colored("ИНТЕРАКТИВНАЯ ПРОВЕРКА: КРУГ", "YELLOW", "BRIGHT")
    print_colored("=" * 60, "CYAN")

    print("\nВведите параметры для проверки:")
    print("(или введите 'выход' для возврата в меню)")

    radius = get_user_input("Радиус круга: ")
    if radius is None: return

    color = input("Цвет круга (например: зеленый): ").strip()
    if color.lower() in ['выход', 'exit', 'quit']: return

    print_colored("\n" + "-" * 60, "MAGENTA")
    user_area = get_user_input("Ваше предположение о площади круга: ")
    if user_area is None: return

    circle = Circle(radius, color)
    program_area = circle.area()

    print_colored("\n" + "=" * 60, "CYAN")
    print_colored("РЕЗУЛЬТАТЫ СРАВНЕНИЯ:", "YELLOW")
    print_colored("=" * 60, "CYAN")

    print(f"Параметры: радиус {radius}, цвет: {color}")
    print(f"Ваш ответ: {user_area:.2f}")
    print(f"Ответ программы: {program_area:.2f}")

    if math.isclose(user_area, program_area, rel_tol=1e-9):
        print_colored(f"✓ ВЕРНО! Площадь круга: {program_area:.2f}", "GREEN")
    else:
        print_colored(f"✗ НЕВЕРНО. Правильный ответ: {program_area:.2f}", "RED")
        difference = abs(user_area - program_area)
        print(f"Разница: {difference:.2f}")

    input("\nНажмите Enter для продолжения...")


def test_square_interactive():
    clear_screen()
    print_colored("=" * 60, "CYAN")
    print_colored("ИНТЕРАКТИВНАЯ ПРОВЕРКА: КВАДРАТ", "YELLOW", "BRIGHT")
    print_colored("=" * 60, "CYAN")

    print("\nВведите параметры для проверки:")
    print("(или введите 'выход' для возврата в меню)")

    side = get_user_input("Длина стороны квадрата: ")
    if side is None: return

    color = input("Цвет квадрата (например: красный): ").strip()
    if color.lower() in ['выход', 'exit', 'quit']: return

    print_colored("\n" + "-" * 60, "MAGENTA")
    user_area = get_user_input("Ваше предположение о площади квадрата: ")
    if user_area is None: return

    square = Square(side, color)
    program_area = square.area()

    print_colored("\n" + "=" * 60, "CYAN")
    print_colored("РЕЗУЛЬТАТЫ СРАВНЕНИЯ:", "YELLOW")
    print_colored("=" * 60, "CYAN")

    print(f"Параметры: сторона {side}, цвет: {color}")
    print(f"Ваш ответ: {user_area:.2f}")
    print(f"Ответ программы: {program_area:.2f}")

    if math.isclose(user_area, program_area, rel_tol=1e-9):
        print_colored(f"✓ ВЕРНО! Площадь квадрата: {program_area:.2f}", "GREEN")
    else:
        print_colored(f"✗ НЕВЕРНО. Правильный ответ: {program_area:.2f}", "RED")
        difference = abs(user_area - program_area)
        print(f"Разница: {difference:.2f}")

    input("\nНажмите Enter для продолжения...")


def comprehensive_test():
    clear_screen()
    print_colored("=" * 60, "CYAN")
    print_colored("КОМПЛЕКСНАЯ ПРОВЕРКА ВСЕХ ФИГУР", "YELLOW", "BRIGHT")
    print_colored("=" * 60, "CYAN")

    print("\nВведите общий параметр N для всех фигур:")
    print("(или введите 'выход' для возврата в меню)")

    N = get_user_input("Значение N: ")
    if N is None: return

    print_colored("\n" + "=" * 60, "CYAN")
    print_colored("ВАШИ ПРЕДПОЛОЖЕНИЯ:", "MAGENTA")
    print_colored("=" * 60, "CYAN")

    print(f"\nДля N = {N}:")
    rect_guess = get_user_input("  Площадь прямоугольника N×N: ")
    if rect_guess is None: return

    circle_guess = get_user_input("  Площадь круга радиусом N: ")
    if circle_guess is None: return

    square_guess = get_user_input("  Площадь квадрата со стороной N: ")
    if square_guess is None: return

    rectangle = Rectangle(N, N, "синий")
    circle = Circle(N, "зеленый")
    square = Square(N, "красный")

    rect_area = rectangle.area()
    circle_area = circle.area()
    square_area = square.area()

    print_colored("\n" + "=" * 60, "CYAN")
    print_colored("РЕЗУЛЬТАТЫ ПРОВЕРКИ:", "YELLOW")
    print_colored("=" * 60, "CYAN")

    results = []

    print("\n1. Прямоугольник (синий):")
    print(f"   Размеры: {N} × {N}")
    print(f"   Ваш ответ: {rect_guess:.2f}")
    print(f"   Правильный ответ: {rect_area:.2f}")
    if math.isclose(rect_guess, rect_area, rel_tol=1e-9):
        print_colored("   ✓ ВЕРНО", "GREEN")
        results.append(True)
    else:
        print_colored(f"   ✗ НЕВЕРНО, разница: {abs(rect_guess - rect_area):.2f}", "RED")
        results.append(False)

    print("\n2. Круг (зеленый):")
    print(f"   Радиус: {N}")
    print(f"   Ваш ответ: {circle_guess:.2f}")
    print(f"   Правильный ответ: {circle_area:.2f}")
    if math.isclose(circle_guess, circle_area, rel_tol=1e-9):
        print_colored("   ✓ ВЕРНО", "GREEN")
        results.append(True)
    else:
        print_colored(f"   ✗ НЕВЕРНО, разница: {abs(circle_guess - circle_area):.2f}", "RED")
        results.append(False)

    print("\n3. Квадрат (красный):")
    print(f"   Сторона: {N}")
    print(f"   Ваш ответ: {square_guess:.2f}")
    print(f"   Правильный ответ: {square_area:.2f}")
    if math.isclose(square_guess, square_area, rel_tol=1e-9):
        print_colored("   ✓ ВЕРНО", "GREEN")
        results.append(True)
    else:
        print_colored(f"   ✗ НЕВЕРНО, разница: {abs(square_guess - square_area):.2f}", "RED")
        results.append(False)

    correct_count = sum(results)
    total_count = len(results)
    percentage = (correct_count / total_count) * 100

    print_colored("\n" + "=" * 60, "CYAN")
    print_colored("ИТОГОВЫЙ РЕЗУЛЬТАТ:", "YELLOW")
    print_colored("=" * 60, "CYAN")

    print(f"\nПравильных ответов: {correct_count} из {total_count}")
    print(f"Процент правильных ответов: {percentage:.1f}%")

    if percentage == 100:
        print_colored("Отличный результат! Все ответы верны!", "GREEN", "BRIGHT")
    elif percentage >= 70:
        print_colored("Хороший результат!", "GREEN")
    elif percentage >= 50:
        print_colored("Удовлетворительный результат.", "YELLOW")
    else:
        print_colored("Нужно больше практики!", "RED")

    input("\nНажмите Enter для продолжения...")


def show_main_menu():
    if COLORAMA_AVAILABLE:
        init(autoreset=True)

    while True:
        clear_screen()
        print_colored("=" * 60, "CYAN")
        print_colored("ГЛАВНОЕ МЕНЮ: ИНТЕРАКТИВНАЯ ПРОВЕРКА ГЕОМЕТРИЧЕСКИХ ФИГУР", "YELLOW", "BRIGHT")
        print_colored("=" * 60, "CYAN")

        print("\nВыберите режим работы:")
        print_colored("1. Демонстрация программы (по заданию)", "GREEN")
        print_colored("2. Проверка прямоугольника", "CYAN")
        print_colored("3. Проверка круга", "MAGENTA")
        print_colored("4. Проверка квадрата", "BLUE")
        print_colored("5. Комплексная проверка всех фигур", "YELLOW")
        print_colored("6. Информация о формулах", "WHITE")
        print_colored("0. Выход", "RED")

        choice = input("\nВаш выбор: ").strip()

        if choice == "1":
            run_demo()
        elif choice == "2":
            test_rectangle_interactive()
        elif choice == "3":
            test_circle_interactive()
        elif choice == "4":
            test_square_interactive()
        elif choice == "5":
            comprehensive_test()
        elif choice == "6":
            show_formulas_info()
        elif choice == "0":
            print_colored("\nДо свидания!", "CYAN")
            break
        else:
            print_colored("\nНеверный выбор. Попробуйте снова.", "RED")
            input("Нажмите Enter для продолжения...")


def run_demo():
    clear_screen()
    print_colored("=" * 60, "CYAN")
    print_colored("ДЕМОНСТРАЦИЯ ПРОГРАММЫ (ПО ЗАДАНИЮ)", "YELLOW", "BRIGHT")
    print_colored("=" * 60, "CYAN")

    N = get_user_input("\nВведите номер вашего варианта (N): ")
    if N is None: return

    print_colored(f"\nСоздание фигур для N = {N}:", "GREEN")

    rectangle = Rectangle(N, N, "синий")
    circle = Circle(N, "зеленый")
    square = Square(N, "красный")

    print(f"\n1. {rectangle}")
    print(f"2. {circle}")
    print(f"3. {square}")

    print_colored("\n" + "=" * 60, "CYAN")
    print_colored("ДЕМОНСТРАЦИЯ ВНЕШНЕГО ПАКЕТА COLORAMA:", "YELLOW")
    print_colored("=" * 60, "CYAN")

    if COLORAMA_AVAILABLE:
        print_colored("Этот текст красного цвета", "RED")
        print_colored("Этот текст зеленого цвета", "GREEN")
        print_colored("Этот текст синего цвета", "BLUE")
        print_colored("Этот текст яркий", "WHITE", "BRIGHT")
        print_colored("Этот текст на желтом фоне (пример)", "YELLOW", "BRIGHT")
    else:
        print_colored("Пакет colorama не установлен. Установите: pip install colorama", "YELLOW")

    input("\nНажмите Enter для возврата в меню...")


def show_formulas_info():
    clear_screen()
    print_colored("=" * 60, "CYAN")
    print_colored("СПРАВОЧНАЯ ИНФОРМАЦИЯ: ФОРМУЛЫ ПЛОЩАДИ", "YELLOW", "BRIGHT")
    print_colored("=" * 60, "CYAN")

    print("\nФормулы для расчета площади:")
    print_colored("\n1. ПРЯМОУГОЛЬНИК:", "CYAN")
    print("   Площадь = ширина × высота")
    print("   S = a × b")
    print("   Пример: прямоугольник 5×3 → S = 5 × 3 = 15")

    print_colored("\n2. КВАДРАТ:", "MAGENTA")
    print("   Площадь = сторона × сторона")
    print("   S = a²")
    print("   Пример: квадрат со стороной 4 → S = 4 × 4 = 16")

    print_colored("\n3. КРУГ:", "GREEN")
    print("   Площадь = π × радиус²")
    print("   S = π × r²")
    print("   где π ≈ 3.1415926535...")
    print("   Пример: круг радиусом 3 → S = π × 3² ≈ 28.27")

    print_colored("\n4. ТРЕУГОЛЬНИК (дополнительно):", "BLUE")
    print("   Площадь = (основание × высота) / 2")
    print("   S = (a × h) / 2")

    print_colored("\nПримеры для самопроверки:", "YELLOW")
    print("1. Прямоугольник: 7 × 4 = 28")
    print("2. Квадрат: 6 × 6 = 36")
    print("3. Круг радиусом 5: π × 25 ≈ 78.54")

    print_colored("\nПроверьте себя с помощью интерактивных тестов!", "GREEN")

    input("\nНажмите Enter для возврата в меню...")


if __name__ == "__main__":
    try:
        show_main_menu()
    except KeyboardInterrupt:
        print("\n\nПрограмма завершена.")
        sys.exit(0)
    except Exception as e:
        print(f"\nПроизошла ошибка: {e}")
        sys.exit(1)
