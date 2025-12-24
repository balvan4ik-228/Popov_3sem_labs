def sort_by_abs(data):
    return sorted(data, key=abs, reverse=True)

def sort_by_abs_lambda(data):
    return sorted(data, key=lambda x: abs(x), reverse=True)

if __name__ == '__main__':
    data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]
    print('sort_by_abs:', sort_by_abs(data))
    print('sort_by_abs_lambda:', sort_by_abs_lambda(data))
