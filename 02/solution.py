import fileinput
import operator

lines = list(fileinput.input())
opcodes = list(map(int, lines[0].split(",")))


def compute(noun, verb):
    local = opcodes.copy()
    local[1] = noun
    local[2] = verb

    position = 0
    opcode = local[position]

    while opcode != 99:
        if opcode == 1:
            instruction = operator.add
        if opcode == 2:
            instruction = operator.mul

        param1 = local[position + 1]
        param2 = local[position + 2]
        param3 = local[position + 3]

        local[param3] = instruction(local[param1], local[param2])
        position = position + 4

        opcode = local[position]

    return local[0]


def part1():
    return compute(12, 2)


def part2():
    target = 19690720

    for noun in range(0, 99):
        for verb in range(0, 99):
            result = compute(noun, verb)
            if result == target:
                return noun, verb


print(part1())
print(part2())
