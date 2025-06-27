def compareTriplets(a, b):
    PuntAlice = 0
    PuntBob = 0

    for i in range(3): 
        if a[i] > b[i]:
            PuntAlice += 1 
        elif a[i] < b[i]:
            PuntBob += 1 
    
    return [PuntAlice,PuntBob]