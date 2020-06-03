import re


def bounds_to_list(bounds):
    bounds_list = re.findall(r'\d+', bounds)
    if len(bounds_list) == 4:
        bounds_list = list(map(int, bounds_list))
    else:
        bounds_list = []
    return bounds_list


if __name__ == '__main__':
    print(bounds_to_list('[22,234][12,221]'))
