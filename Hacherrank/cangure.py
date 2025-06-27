def kangaroo(x1, v1, x2, v2):
    for i in range(10000):
        pos1 = x1 + v1 * i
        pos2 = x2 + v2 * i
        if pos1 == pos2:
            return "YES"
        return "NO"