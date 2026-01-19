import math


def frequency_test(bits):
    zeros = bits.count("0")
    ones = bits.count("1")
    return zeros, ones


def calculate_entropy(bits):
    total = len(bits)
    zeros = bits.count("0")
    ones = bits.count("1")

    entropy = 0.0
    for count in [zeros, ones]:
        if count == 0:
            continue
        p = count / total
        entropy -= p * math.log2(p)

    return entropy


def runs_test(bits):
    if not bits:
        return 0

    runs = 1
    for i in range(1, len(bits)):
        if bits[i] != bits[i - 1]:
            runs += 1

    return runs
