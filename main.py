def f21():
    x = [2003, 'terra', 2016, 1983, 1989]

    def firstlvl():
        if x[1] == 'terra' or x[1] == 'edn':
            print('1')
            secondlvl()
        else:
            return 9
    def secondlvl():
        if x[2] == 2006:
            return 2
        elif x[0] == 2003 or x[0] == 2001 or x[2] == 2016:
            print('2')
            thirdlvl()

    def thirdlvl():
        if x[4] == 1972:
            return 0
        elif x[4] == 1989:
            return 1
        elif x[3] == 1983:
            return 5
        elif x[4] == 1972:
            return 6
        elif x[3] == 2010 or x[4] == 1989:
            fourthlvl()

    def fourthlvl():
        if x[4] == 1972:
            return 3
        elif x[4] == 1989:
            return 4
        elif x[2] == 2016:
            return 7
        elif x[2] == 2006:
            return 8

    firstlvl()

print(f21())