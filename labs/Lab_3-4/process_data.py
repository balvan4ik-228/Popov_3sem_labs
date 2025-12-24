import json
import sys
import os
from field import field
from gen_random import gen_random
from unique import Unique
from print_result import print_result
from cm_timer import cm_timer_1

def find_data_file():
    candidates = ['data_light.json']
    for path in candidates:
        if os.path.exists(path):
            return path
    return None

path = sys.argv[1] if len(sys.argv) > 1 else find_data_file()

if not path:
    print("❌ data_light.json не найден!")
    print("Запустите: python generate_data.py")
    sys.exit(1)

with open(path, encoding='utf-8') as f:
    data = json.load(f)

@print_result
def f1(arg):
    return sorted(Unique(field(arg, 'profession'), ignore_case=True), key=str.lower)

@print_result
def f2(arg):
    return list(filter(lambda x: x and x.startswith('программист'), arg))

@print_result
def f3(arg):
    return list(map(lambda x: f'{x} с опытом Python', arg))

@print_result
def f4(arg):
    salaries = list(gen_random(len(arg), 100000, 200000))
    return [f'{prof}, зарплата {salary:.0f} руб.'
            for prof, salary in zip(arg, salaries)]

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
