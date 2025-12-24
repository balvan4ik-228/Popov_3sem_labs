import sys
import math


class BiquadraticSolver:

    def __init__(self, a=None, b=None, c=None):
        self.a = a
        self.b = b
        self.c = c
        self.roots = []

    def get_valid_input(self, prompt, value):
        while True:
            if value is not None:
                try:
                    return float(value)
                except (ValueError, TypeError):
                    print(f"Некорректное значение: {value}")
            value = input(prompt)
            try:
                return float(value)
            except ValueError:
                print("Ошибка: введите действительное число.")

    def input_coefficients(self, args):
        self.a = self.get_valid_input(
            "Введите коэффициент A: ",
            args[0] if len(args) > 0 else None
        )
        self.b = self.get_valid_input(
            "Введите коэффициент B: ",
            args[1] if len(args) > 1 else None
        )
        self.c = self.get_valid_input(
            "Введите коэффициент C: ",
            args[2] if len(args) > 2 else None
        )

    def solve(self):
        if self.a == 0:
            raise ValueError("Коэффициент A не может быть нулем.")

        D = self.b ** 2 - 4 * self.a * self.c

        if D < 0:
            return []
        elif D == 0:
            y = -self.b / (2 * self.a)
            return self._process_y_value(y)
        else:
            sqrt_D = math.sqrt(D)
            y1 = (-self.b + sqrt_D) / (2 * self.a)
            y2 = (-self.b - sqrt_D) / (2 * self.a)
            roots1 = self._process_y_value(y1)
            roots2 = self._process_y_value(y2)
            return sorted(list(set(roots1 + roots2)))

    def _process_y_value(self, y):
        roots = []
        if y > 0:
            roots.extend([math.sqrt(y), -math.sqrt(y)])
        elif y == 0:
            roots.append(0)
        return roots

    def display_equation(self):
        return f"{self.a}*x^4 + {self.b}*x^2 + {self.c} = 0"

    def display_roots(self, roots):
        if not roots:
            print("Действительных корней нет.")
        else:
            print("Действительные корни:",
                  ", ".join(f"x{i + 1} = {x}" for i, x in enumerate(roots)))


def main():
    print("Решение биквадратного уравнения A*x^4 + B*x^2 + C = 0")

    solver = BiquadraticSolver()

    solver.input_coefficients(sys.argv[1:4])

    print(f"\nУравнение: {solver.display_equation()}")

    D = solver.b ** 2 - 4 * solver.a * solver.c
    print(f"Дискриминант D = {D}")

    try:
        roots = solver.solve()
        solver.display_roots(roots)
    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()