def func():
    test1()
    test2()
    test3()
    test4()


def print_result(func):
    def wrapper():
        res = func()
        if isinstance(res, list):
            for item in res:
                print(item)
        elif isinstance(res, dict):
            for key, value in res.items():
                print(f'{key} = {value}')
        else:
            print(res)
        return res

    return wrapper


@print_result
def test1():
    return 1


@print_result
def test2():
    return 'iu5'


@print_result
def test3():
    return {'a': 1, 'b': 2}


@print_result
def test4():
    return [1, 2]
