import random
def func():
    print(str(list(field(4,7,17)))[1:-1])


def field(cnt , min , max):
    ans = []
    for i in range(cnt):
        ans.append(random.randint(min, max))
    yield ans
