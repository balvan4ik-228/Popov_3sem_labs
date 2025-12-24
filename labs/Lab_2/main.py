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


def print_colored(text, color=Fore.WHITE, style=Style.NORMAL):
    if COLORAMA_AVAILABLE:
        print(f"{style}{color}{text}{Style.RESET_ALL}")
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
            print_colored("Ошибка: введите корректное число!", Fore.RED)
        except KeyboardInterrupt:
            print("\n\nПрограмма прервана пользователем.")
            sys.exit(0)


def test_rectangle_interactive():
    clear_screen()
    print_colored("=" * 60, Fore.CYAN)
    print_colored("ИНТЕРАКТИВНАЯ ПРОВЕРКА: ПРЯМОУГОЛЬНИК", Fore.YELLOW, Style.BRIGHT)
    print_colored("=" * 60, Fore.CYAN)

    print("\nВведите параметры для проверки:")
    print("(или введите 'выход' для возврата в меню)")

    width = get_user_input("Ширина прямоугольника: ")
    if width is None: return

    height = get_user_input("Высота прямоугольника: ")
    if height is None: return

    color = input("Цвет прямоугольника (например: синий): ").strip()
    if color.lower() in ['выход', 'exit', 'quit']: return

    print_colored("\n" + "-" * 60, Fore.MAGENTA)
    user_area = get_user_input("Ваше предположение о площади прямоугольника: ")
    if user_area is None: return

    rectangle = Rectangle(width, height, color)
    program_area = rectangle.area()

    print_colored("\n" + "=" * 60, Fore.CYAN)
    print_colored("РЕЗУЛЬТАТЫ СРАВНЕНИЯ:", Fore.YELLOW)
    print_colored("=" * 60, Fore.CYAN)

    print(f"Параметры: {width} × {height}, цвет: {color}")
    print(f"Ваш ответ: {user_area:.2f}")
    print(f"Ответ программы: {program_area:.2f}")

    if math.isclose(user_area, program_area, rel_tol=1e-9):
        print_colored(f"✓ ВЕРНО! Площадь прямоугольника: {program_area:.2f}", Fore.GREEN)
    else:
        print_colored(f"✗ НЕВЕРНО. Правильный ответ: {program_area:.2f}", Fore.RED)
        difference = abs(user_area - program_area)
        print(f"Разница: {difference:.2f}")

    input("\nНажмите Enter для продолжения...")


def test_circle_interactive():
    clear_screen()
    print_colored("=" * 60, Fore.CYAN)
    print_colored("ИНТЕРАКТИВНАЯ ПРОВЕРКА: КРУГ", Fore.YELLOW, Style.BRIGHT)
    print_colored("=" * 60, Fore.CYAN)

    print("\nВведите параметры для проверки:")
    print("(или введите 'выход' для возврата в меню)")

    radius = get_user_input("Радиус круга: ")
    if radius is None: return

    color = input("Цвет круга (например: зеленый): ").strip()
    if color.lower() in ['выход', 'exit', 'quit']: return

    print_colored("\n" + "-" * 60, Fore.MAGENTA)
    user_area = get_user_input("Ваше предположение о площади круга: ")
    if user_area is None: return

    circle = Circle(radius, color)
    program_area = circle.area()

    print_colored("\n" + "=" * 60, Fore.CYAN)
    print_colored("РЕЗУЛЬТАТЫ СРАВНЕНИЯ:", Fore.YELLOW)
    print_colored("=" * 60, Fore.CYAN)

    print(f"Параметры: радиус {radius}, цвет: {color}")
    print(f"Ваш ответ: {user_area:.2f}")
    print(f"Ответ программы: {program_area:.2f}")

    if math.isclose(user_area, program_area, rel_tol=1e-9):
        print_colored(f"✓ ВЕРНО! Площадь круга: {program_area:.2f}", Fore.GREEN)
    else:
        print_colored(f"✗ НЕВЕРНО. Правильный ответ: {program_area:.2f}", Fore.RED)
        difference = abs(user_area - program_area)
        print(f"Разница: {difference:.2f}")

    input("\nНажмите Enter для продолжения...")


def test_square_interactive():
    clear_screen()
    print_colored("=" * 60, Fore.CYAN)
    print_colored("ИНТЕРАКТИВНАЯ ПРОВЕРКА: КВАДРАТ", Fore.YELLOW, Style.BRIGHT)
    print_colored("=" * 60, Fore.CYAN)

    print("\nВведите параметры для проверки:")
    print("(или введите 'выход' для возврата в меню)")

    side = get_user_input("Длина стороны квадрата: ")
    if side is None: return

    color = input("Цвет квадрата (например: красный): ").strip()
    if color.lower() in ['выход', 'exit', 'quit']: return

    print_colored("\n" + "-" * 60, Fore.MAGENTA)
    user_area = get_user_input("Ваше предположение о площади квадрата: ")
    if user_area is None: return

    square = Square(side, color)
    program_area = square.area()

    print_colored("\n" + "=" * 60, Fore.CYAN)
    print_colored("РЕЗУЛЬТАТЫ СРАВНЕНИЯ:", Fore.YELLOW)
    print_colored("=" * 60, Fore.CYAN)

    print(f"Параметры: сторона {side}, цвет: {color}")
    print(f"Ваш ответ: {user_area:.2f}")
    print(f"Ответ программы: {program_area:.2f}")

    if math.isclose(user_area, program_area, rel_tol=1e-9):
        print_colored(f"✓ ВЕРНО! Площадь квадрата: {program_area:.2f}", Fore.GREEN)
    else:
        print_colored(f"✗ НЕВЕРНО. Правильный ответ: {program_area:.2f}", Fore.RED)
        difference = abs(user_area - program_area)
        print(f"Разница: {difference:.2f}")

    input("\nНажмите Enter для продолжения...")


def comprehensive_test():
    clear_screen()
    print_colored("=" * 60, Fore.CYAN)
    print_colored("КОМПЛЕКСНАЯ ПРОВЕРКА ВСЕХ ФИГУР", Fore.YELLOW, Style.BRIGHT)
    print_colored("=" * 60, Fore.CYAN)

    print("\nВведите общий параметр N для всех фигур:")
    print("(или введите 'выход' для возврата в меню)")

    N = get_user_input("Значение N: ")
    if N is None: return

    print_colored("\n" + "=" * 60, Fore.CYAN)
    print_colored("ВАШИ ПРЕДПОЛОЖЕНИЯ:", Fore.MAGENTA)
    print_colored("=" * 60, Fore.CYAN)

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

    print_colored("\n" + "=" * 60, Fore.CYAN)
    print_colored("РЕЗУЛЬТАТЫ ПРОВЕРКИ:", Fore.YELLOW)
    print_colored("=" * 60, Fore.CYAN)

    results = []

    print("\n1. Прямоугольник (синий):")
    print(f"   Размеры: {N} × {N}")
    print(f"   Ваш ответ: {rect_guess:.2f}")
    print(f"   Правильный ответ: {rect_area:.2f}")
    if math.isclose(rect_guess, rect_area, rel_tol=1e-9):
        print_colored("   ✓ ВЕРНО", Fore.GREEN)
        results.append(True)
    else:
        print_colored(f"   ✗ НЕВЕРНО, разница: {abs(rect_guess - rect_area):.2f}", Fore.RED)
        results.append(False)

    print("\n2. Круг (зеленый):")
    print(f"   Радиус: {N}")
    print(f"   Ваш ответ: {circle_guess:.2f}")
    print(f"   Правильный ответ: {circle_area:.2f}")
    if math.isclose(circle_guess, circle_area, rel_tol=1e-9):
        print_colored("   ✓ ВЕРНО", Fore.GREEN)
        results.append(True)
    else:
        print_colored(f"   ✗ НЕВЕРНО, разница: {abs(circle_guess - circle_area):.2f}", Fore.RED)
        results.append(False)

    print("\n3. Квадрат (красный):")
    print(f"   Сторона: {N}")
    print(f"   Ваш ответ: {square_guess:.2f}")
    print(f"   Правильный ответ: {square_area:.2f}")
    if math.isclose(square_guess, square_area, rel_tol=1e-9):
        print_colored("   ✓ ВЕРНО", Fore.GREEN)
        results.append(True)
    else:
        print_colored(f"   ✗ НЕВЕРНО, разница: {abs(square_guess - square_area):.2f}", Fore.RED)
        results.append(False)

    correct_count = sum(results)
    total_count = len(results)
    percentage = (correct_count / total_count) * 100

    print_colored("\n" + "=" * 60, Fore.CYAN)
    print_colored("ИТОГОВЫЙ РЕЗУЛЬТАТ:", Fore.YELLOW)
    print_colored("=" * 60, Fore.CYAN)

    print(f"\nПравильных ответов: {correct_count} из {total_count}")
    print(f"Процент правильных ответов: {percentage:.1f}%")

    if percentage == 100:
        print_colored("Отличный результат! Все ответы верны!", Fore.GREEN, Style.BRIGHT)
    elif percentage >= 70:
        print_colored("Хороший результат!", Fore.GREEN)
    elif percentage >= 50:
        print_colored("Удовлетворительный результат.", Fore.YELLOW)
    else:
        print_colored("Нужно больше практики!", Fore.RED)

    input("\nНажмите Enter для продолжения...")


def show_main_menu():
    if COLORAMA_AVAILABLE:
        init(autoreset=True)

    while True:
        clear_screen()
        print_colored("=" * 60, Fore.CYAN)
        print_colored("ГЛАВНОЕ МЕНЮ: ИНТЕРАКТИВНАЯ ПРОВЕРКА ГЕОМЕТРИЧЕСКИХ ФИГУР", Fore.YELLOW, Style.BRIGHT)
        print_colored("=" * 60, Fore.CYAN)

        print("\nВыберите режим работы:")
        print_colored("1. Демонстрация программы (по заданию)", Fore.GREEN)
        print_colored("2. Проверка прямоугольника", Fore.CYAN)
        print_colored("3. Проверка круга", Fore.MAGENTA)
        print_colored("4. Проверка квадрата", Fore.BLUE)
        print_colored("5. Комплексная проверка всех фигур", Fore.YELLOW)
        print_colored("6. Информация о формулах", Fore.WHITE)
        print_colored("0. Выход", Fore.RED)

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
            print_colored("\nДо свидания!", Fore.CYAN)
            break
        else:
            print_colored("\nНеверный выбор. Попробуйте снова.", Fore.RED)
            input("Нажмите Enter для продолжения...")


def run_demo():
    clear_screen()
    print_colored("=" * 60, Fore.CYAN)
    print_colored("ДЕМОНСТРАЦИЯ ПРОГРАММЫ (ПО ЗАДАНИЮ)", Fore.YELLOW, Style.BRIGHT)
    print_colored("=" * 60, Fore.CYAN)

    N = get_user_input("\nВведите номер вашего варианта (N): ")
    if N is None: return

    print_colored(f"\nСоздание фигур для N = {N}:", Fore.GREEN)

    rectangle = Rectangle(N, N, "синий")
    circle = Circle(N, "зеленый")
    square = Square(N, "красный")

    print(f"\n1. {rectangle}")
    print(f"2. {circle}")
    print(f"3. {square}")

    print_colored("\n" + "=" * 60, Fore.CYAN)
    print_colored("ДЕМОНСТРАЦИЯ ВНЕШНЕГО ПАКЕТА COLORAMA:", Fore.YELLOW)
    print_colored("=" * 60, Fore.CYAN)

    if COLORAMA_AVAILABLE:
        print(Fore.RED + "Этот текст красного цвета")
        print(Fore.GREEN + "Этот текст зеленого цвета")
        print(Fore.BLUE + "Этот текст синего цвета")
        print(Back.YELLOW + Fore.BLACK + "Этот текст на желтом фоне")
        print(Style.BRIGHT + "Этот текст яркий")
    else:
        print("Пакет colorama не установлен. Установите: pip install colorama")

    input("\nНажмите Enter для возврата в меню...")


def show_formulas_info():
    clear_screen()
    print_colored("=" * 60, Fore.CYAN)
    print_colored("СПРАВОЧНАЯ ИНФОРМАЦИЯ: ФОРМУЛЫ ПЛОЩАДИ", Fore.YELLOW, Style.BRIGHT)
    print_colored("=" * 60, Fore.CYAN)

    print("\nФормулы для расчета площади:")
    print_colored("\n1. ПРЯМОУГОЛЬНИК:", Fore.CYAN)
    print("   Площадь = ширина × высота")
    print("   S = a × b")
    print("   Пример: прямоугольник 5×3 → S = 5 × 3 = 15")

    print_colored("\n2. КВАДРАТ:", Fore.MAGENTA)
    print("   Площадь = сторона × сторона")
    print("   S = a²")
    print("   Пример: квадрат со стороной 4 → S = 4 × 4 = 16")

    print_colored("\n3. КРУГ:", Fore.GREEN)
    print("   Площадь = π × радиус²")
    print("   S = π × r²")
    print("   где π ≈ 3.1415926535...")
    print("   Пример: круг радиусом 3 → S = π × 3² ≈ 28.27")

    print_colored("\n4. ТРЕУГОЛЬНИК (дополнительно):", Fore.BLUE)
    print("   Площадь = (основание × высота) / 2")
    print("   S = (a × h) / 2")

    print_colored("\nПримеры для самопроверки:", Fore.YELLOW)
    print("1. Прямоугольник: 7 × 4 = 28")
    print("2. Квадрат: 6 × 6 = 36")
    print("3. Круг радиусом 5: π × 25 ≈ 78.54")

    print_colored("\nПроверьте себя с помощью интерактивных тестов!", Fore.GREEN)

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