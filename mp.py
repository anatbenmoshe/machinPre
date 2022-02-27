

print(abs(3.0 * (4.0 / 3.0 - 1) - 1))  # print inaccurate result


def machineEpsilon():  # find and return machine epsilon
    epsilon = 0.5
    while (1 + epsilon) != 1:  # while it is accurate
        epsilon = epsilon / 2  # find smaller epsilon
    return epsilon  # return machine epsilon


print(machineEpsilon())  # print machine epsilon
print(abs(3.0 * (4.0 / 3.0 - 1) - 1)+machineEpsilon())
print("aaaaa")