goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
]


def generator(items, *args):
    for item in items:
        if len(args) > 1:
            new_item = {arg: item.get(arg) for arg in args}
            if any(new_item.values()):
                yield new_item
        else:
            key = args[0]
            if key in item:
                value = item[key]
                if value is not None:
                    yield value

def field(items, *args):
    for i in generator(items, *args):
        print(i)


field(goods, 'title', 'price')