from random import shuffle

class Deck:
    SUITE = 'H D S C'.split()
    RANKS = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']

    print(SUITE)

    li = []
    for r in RANKS:
        for s in SUITE:
            li.append((r,s))
    
    print(len(li))


deck = Deck()
