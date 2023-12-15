
def func():
    data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
    res = sorted(data, key = abs, reverse=True)
    print(res)
    res_ = sorted(data, key = lambda x: abs(x), reverse=True)
    print(res_)