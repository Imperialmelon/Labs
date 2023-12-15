def func():
    goods = [{'title': 'ковер', 'price': 1500, 'color': 'red'},
             {'title': 'диван', 'price': 2000, 'color': 'red'}]
    print(str(list(field(goods, 'title')))[1:-1])
    print(str(list(field(goods, 'title', 'price')))[1:-1])



def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        for item in items:
            if item[args[0]] is not None:
                yield item[args[0]]
    else:
        for item in items:
            res = {}
            for key in args:
                if key in item and item[key] is not None:
                    res[key] = item[key]
            yield res
