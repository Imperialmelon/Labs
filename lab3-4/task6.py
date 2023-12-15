import time
from contextlib import contextmanager

def func():
    with timer1():
        time.sleep(5.5)
    with timer2():
        time.sleep(5.5)
class timer1():
    def __enter__(self):
        self.start = time.time()
    def __exit__(self, exc_type, exc_val, exc_tb):
        time_ = time.time() - self.start
        print(f'time = {time_}')

@contextmanager
def timer2():
    start = time.time()
    yield
    time_ = time.time() - start
    print(f'time = {time_}')

