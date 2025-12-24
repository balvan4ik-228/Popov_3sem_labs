from tkinter import *
import re
import math
from functools import partial

DIV_SYMBOL = '÷'

def center_window(win, width, height):
    win.update_idletasks()
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    win.geometry(f"{width}x{height}+{x}+{y}")

class RoundedButton(Canvas):
    def __init__(self, parent, diameter, text, command=None,
                 border_color="#4a4a4a", bg_color="#f0ead8", fg_color="#5b4636",
                 hover_color="#e0d8c8", active_color="#d0c8b8",
                 font=("Arial", 32, "bold"), **kwargs):
        super().__init__(parent, width=diameter, height=diameter,
                         highlightthickness=0, bg=parent['bg'], **kwargs)
        self.command = command
        self.diameter = diameter
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.active_color = active_color

        self.circle = self.create_oval(
            2, 2, diameter - 2, diameter - 2,
            fill=border_color, outline=border_color
        )
        self.inner_circle = self.create_oval(
            6, 6, diameter - 6, diameter - 6,
            fill=bg_color, outline=bg_color
        )
        self.text_item = self.create_text(
            diameter // 2, diameter // 2,
            text=text, fill=fg_color, font=font
        )

        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.bind("<ButtonPress-1>", self.on_press)
        self.bind("<ButtonRelease-1>", self.on_release)

    def on_enter(self, event):
        self.itemconfig(self.inner_circle, fill=self.hover_color)

    def on_leave(self, event):
        self.itemconfig(self.inner_circle, fill=self.bg_color)

    def on_press(self, event):
        self.itemconfig(self.inner_circle, fill=self.active_color)

    def on_release(self, event):
        self.itemconfig(self.inner_circle, fill=self.hover_color)
        if self.command:
            self.command()

class Calculator:
    OPERATORS_EXCEPT_MINUS = '+*/'

    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        window_width = 650
        window_height = 780
        center_window(root, window_width, window_height)
        self.root.resizable(False, False)
        self.root.configure(bg="#f8f4d8")

        self.expression = ""  # для вычислений (с символом '/')
        self.display_expression = ""  # для отображения (с символом '÷')
        self.input_text = StringVar()

        main_frame = Frame(root, bg="#f8f4d8")
        main_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        entry_border = Frame(main_frame, bg="#fffafa", height=110)
        entry_border.pack(fill=X, pady=(0, 20))

        self.input_field = Entry(
            entry_border, textvariable=self.input_text,
            font=('Arial', 42), bd=0, relief=FLAT,
            justify=RIGHT, state="readonly",
            readonlybackground="#f0ead8", fg="#5b4636"
        )
        self.input_field.pack(fill=BOTH, expand=True, padx=6, pady=6)

        button_frame = Frame(main_frame, bg="#f8f4d8")
        button_frame.pack(fill=BOTH, expand=True)

        buttons = [
            ('C', self.clear), ('(', self.add_char), (')', self.add_char), (DIV_SYMBOL, self.add_division),
            ('7', self.add_char), ('8', self.add_char), ('9', self.add_char), ('*', self.add_char),
            ('4', self.add_char), ('5', self.add_char), ('6', self.add_char), ('-', self.add_binary_minus),
            ('1', self.add_char), ('2', self.add_char), ('3', self.add_char), ('+', self.add_char),
            ('±', self.toggle_sign), ('0', self.add_char), ('.', self.add_char), ('=', self.calculate)
        ]

        for i, (text, cmd) in enumerate(buttons):
            action = partial(cmd, text)
            btn = RoundedButton(
                button_frame, 120, text, command=action,
                border_color="#fffafa", bg_color="#f0ead8",
                fg_color="#5b4636", hover_color="#e0d8c8",
                active_color="#d0c8b8", font=("Arial", 32, "bold")
            )
            row, col = divmod(i, 4)
            btn.grid(row=row, column=col, padx=8, pady=8, sticky="nsew")
            button_frame.grid_columnconfigure(col, weight=1)
            button_frame.grid_rowconfigure(row, weight=1)

        self.root.bind("<BackSpace>", self.backspace)
        self.root.bind("<Return>", self.calculate)
        self.root.bind("<Delete>", self.clear)
        self.root.bind("<Escape>", self.clear)
        self.root.bind("<Key>", self.key_input)

    def clear(self, event=None):
        self.expression = ""
        self.display_expression = ""
        self.input_text.set(self.display_expression)

    def close_open_brackets_if_needed(self):
        open_brackets = self.expression.count('(')
        close_brackets = self.expression.count(')')
        if open_brackets > close_brackets:
            self.expression += ')'
            self.display_expression += ')'

    def add_char(self, char):
        if self.expression == "Ошибка":
            self.expression = ""
            self.display_expression = ""

        # Блокируем ввод оператора сразу после "(-"
        if self.display_expression.endswith('(-') and char in self.OPERATORS_EXCEPT_MINUS:
            return

        if char in self.OPERATORS_EXCEPT_MINUS:
            if not self.expression:
                if char != '+':
                    return
            else:
                if self.expression[-1] in self.OPERATORS_EXCEPT_MINUS:
                    return
                self.close_open_brackets_if_needed()

        if char == '0':
            if not self.expression or self.expression[-1] in self.OPERATORS_EXCEPT_MINUS + '(-':
                self.expression += '0.'
                self.display_expression += '0.'
                self.input_text.set(self.display_expression)
                return
            elif self.expression[-1] == '0' and (len(self.expression) == 1 or self.expression[-2] in self.OPERATORS_EXCEPT_MINUS + '('):
                return

        if char == '.':
            if not self.expression:
                return
            if self.expression[-1] in self.OPERATORS_EXCEPT_MINUS + '(-.':
                return
            parts = re.split(r'[+\-*/()]', self.expression)
            if parts and '.' in parts[-1]:
                return

        self.expression += char
        self.display_expression += char
        self.input_text.set(self.display_expression)

    def add_division(self, char=None, from_colon=False):
        if self.expression == "Ошибка":
            self.expression = ""
            self.display_expression = ""

        # Блокируем ввод оператора сразу после "(-"
        if self.display_expression.endswith('(-'):
            return

        if not self.expression:
            return
        if self.expression[-1] in self.OPERATORS_EXCEPT_MINUS + '/':
            return
        self.close_open_brackets_if_needed()
        self.expression += '/'
        self.display_expression += DIV_SYMBOL
        self.input_text.set(self.display_expression)

    def add_binary_minus(self, char=None):
        if self.expression == "Ошибка":
            self.expression = ""
            self.display_expression = ""

        # Блокируем ввод оператора сразу после "(-"
        if self.display_expression.endswith('(-'):
            return

        if not self.expression:
            return
        last_char = self.expression[-1]
        if last_char.isdigit() or last_char == ')':
            self.close_open_brackets_if_needed()
            self.expression += '-'
            self.display_expression += '-'
            self.input_text.set(self.display_expression)
        else:
            return

    def toggle_sign(self, char=None):
        if self.expression == "Ошибка":
            self.expression = ""
            self.display_expression = ""

        if not self.expression or self.expression[-1] in self.OPERATORS_EXCEPT_MINUS + '(':
            self.expression += '(-'
            self.display_expression += '(-'
            self.input_text.set(self.display_expression)
            return

        if self.expression[-1].isdigit() or self.expression[-1] == ')':
            return

        self.expression += '(-'
        self.display_expression += '(-'
        self.input_text.set(self.display_expression)

    def calculate(self, event=None):
        if not self.expression:
            return

        try:
            expr = self.expression
            open_brackets = expr.count('(')
            close_brackets = expr.count(')')
            expr += ')' * (open_brackets - close_brackets)
            expr = expr.replace('(-', '(0-')

            result = eval(expr, {"__builtins__": None},
                          {"math": math, "sqrt": math.sqrt, "sin": math.sin,
                           "cos": math.cos, "tan": math.tan, "log": math.log})

            if isinstance(result, float):
                if result.is_integer():
                    result = int(result)
                else:
                    result = round(result, 10)

            self.expression = str(result)
            self.display_expression = str(result)
        except Exception:
            self.expression = "Ошибка"
            self.display_expression = "Ошибка"

        self.input_text.set(self.display_expression)

    def backspace(self, event=None):
        if self.expression and self.expression != "Ошибка":
            if self.expression.endswith('(-'):
                self.expression = self.expression[:-2]
                self.display_expression = self.display_expression[:-2]
            else:
                self.expression = self.expression[:-1]
                self.display_expression = self.display_expression[:-1]
            self.input_text.set(self.display_expression)

    def key_input(self, event):
        char = event.char
        keysym = event.keysym

        if char == ':':
            self.add_division(from_colon=True)
            return

        match char, keysym:
            case char, _ if char in '0123456789+*/().':
                self.add_char(char)
            case '/', _:
                self.add_division()
            case '-', _:
                self.add_binary_minus(char)
            case _, keysym if keysym in ('Return', 'KP_Enter'):
                self.calculate()
            case _, keysym if keysym == 'BackSpace':
                self.backspace()
            case _, keysym if keysym in ('Delete', 'Escape'):
                self.clear()
            case char, _ if char in ('~', '±'):
                self.toggle_sign()
            case char, _ if char == '=':
                self.calculate()
            case _:
                pass


if __name__ == "__main__":
    root = Tk()
    calc = Calculator(root)
    root.mainloop()
