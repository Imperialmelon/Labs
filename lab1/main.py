import sys
import math


def get_coef(index, prompt):
    try:
        flag = False
        coef_str = sys.argv[index]
        while not flag:
            try:
                tmp_coef = float(sys.argv[index])
                coef_str = sys.argv[index]
                flag = True
            except:
                sys.argv[index] = input(f'Коэффициент номер {index} введен некорректно. Повторите ввод ')

    except:
        print(prompt)
        flag = False
        coef_str = input()
        while not flag:
            try:
                coef_ = float(coef_str)
                flag = True
            except:
                coef_str = input()
    coef = float(coef_str)
    return coef


def get_roots(a, b, c):
    result = []
    if a == 0:
        if c < 0:
            return result
        elif c == 0:
            root = 0
            result.append(root)
            return result
        else:
            root1 = - math.sqrt(-c)
            root2 = math.sqrt(-c)
            result.append(root1)
            result.append(root2)
            return result

    D = b * b - 4 * a * c
    if D == 0.0:
        root = -b / (2.0 * a)
        if root >= 0:
            result.append(math.sqrt(root))
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        root2 = (-b - sqD) / (2.0 * a)
        if root1 >= 0:
            if root1 == 0 :
                result.append(math.sqrt(root1))
            else:
                result.append(math.sqrt(root1))
                result.append(-math.sqrt(root1))
        if root2 >= 0:
            if root2 == 0 :
                result.append(math.sqrt(root2))
            else:
                result.append(math.sqrt(root2))
                result.append(-math.sqrt(root2))
    return result


def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    roots = get_roots(a, b, c)
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {}, {}, {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        # print(roots)
        print('Четыре корня: {}, {}, {}, {}'.format(roots[0], roots[1], roots[2], roots[3]))


if __name__ == "__main__":
    main()
