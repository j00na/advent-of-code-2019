def calculate_fuel(mass):
    fuel = (mass//3)-2
    if fuel <= 0:
        return 0
    else:
        return fuel + calculate_fuel(fuel)


def read_data(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    return [int(x) for x in lines]


if __name__ == "__main__":
    data = read_data('../mass.txt')
    result = sum([calculate_fuel(x) for x in data])
    print("The sum of modules is: {:d}".format(result))
