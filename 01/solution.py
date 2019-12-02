import fileinput

lines = list(fileinput.input())


def calculateFuelRequirement(x):
    return int(int(x)/3) - 2


def part1():
    return sum(map(calculateFuelRequirement, lines))


def calculateFuelRequirementRecursively(x):
    total = calculateFuelRequirement(x)
    current = calculateFuelRequirement(x)

    while current > 0:
        current = calculateFuelRequirement(current)
        # don't add negative mass
        if(current > 0):
            total += current

    return total


def part2():
    return sum(map(calculateFuelRequirementRecursively, lines))


print(part1())
print(part2())
