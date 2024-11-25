def gcd(list):
    max = len(list) - 1
    if max > 0:
        while list[max - 1] != list[max]:
            if list[max - 1] > list[max]:
                list[max - 1] -= list[max]
            else:
                list[max] -= list[max - 1]
        return gcd(list[:-1])
    else:
        return list[max]

list = [2,16,4]
print(gcd(list))