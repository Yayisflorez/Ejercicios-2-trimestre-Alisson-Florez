def countApplesAndOranges(s, t, a, b, apples, oranges):
    man=0
    nar=0
    for i in apples:
        manp = i + a
        if s <= manp <= t:
            man += 1
    for j in oranges:
        narp = j + b
        if s <= narp <= t:
            nar += 1
    print(man)
    print(nar)
   