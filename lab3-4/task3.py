

class Unique(object):
    def __init__(self, items, **kwargs):
        self.it = iter(items)
        self.ignore_case = kwargs.get('ignore_case', False)
        self.res = set()
    def __next__(self):
        while True:
            item = next(self.it)
            item_ = item.lower() if self.ignore_case else item
            if item_ not in self.res:
                self.res.add(item_)
                return item_
    def __iter__(self):
        return self

def func():
    data = [1,4,5,7, 'int', 'char*', 1,4,7, 'char*']
    data_ = Unique(data)
    print(list(data_))


