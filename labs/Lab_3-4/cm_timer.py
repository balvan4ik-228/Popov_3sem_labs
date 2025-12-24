from time import perf_counter, sleep
from contextlib import contextmanager


class cm_timer_1:
    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, *args):
        end = perf_counter()
        print(f'time: {end - self.start:.1f}')


@contextmanager
def cm_timer_2():
    start = perf_counter()
    try:
        yield
    finally:
        end = perf_counter()
        print(f'time: {end - start:.1f}')


if __name__ == '__main__':
    with cm_timer_1():
        sleep(1)
    with cm_timer_2():
        sleep(1)
