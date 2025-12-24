def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        for item in items:
            value = item.get(args[0])
            if value is not None:
                yield value
    else:
        for item in items:
            result = {k: item.get(k) for k in args if item.get(k) is not None}
            if result:
                yield result

if __name__ == '__main__':
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'}
    ]
    print('field(goods, "title"):', list(field(goods, 'title')))
    print('field(goods, "title", "price"):', list(field(goods, 'title', 'price')))
