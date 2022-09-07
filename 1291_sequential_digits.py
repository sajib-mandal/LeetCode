def sequential_digits(low, high):
    digits = "123456789"
    res = []
    nl = len(str(low))
    nh = len(str(high))

    for i in range(nl, nh + 1):
        for j in range(0, 10 - i):
            num = int(digits[j: j + i])
            if num >= low and num <= high:
                res.append(num)
    return res

print(sequential_digits(1000, 12000))
