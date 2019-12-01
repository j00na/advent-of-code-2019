def read_data(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    return [int(x) for x in lines]


def sum_of_masses(lst):
    return sum([(x//3)-2 for x in lst])


if __name__ == "__main__":
    data = read_data('../mass.txt')
    result = sum_of_masses(data)
    print("The sum of modules is: {:d}".format(result))
