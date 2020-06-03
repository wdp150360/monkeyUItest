import re


def bounds_to_list(bounds):
    bounds_list = re.findall(r'\d+', bounds)
    return bounds_list


if __name__ == '__main__':
    print(bounds_to_list('[22,234][12,221]'))
