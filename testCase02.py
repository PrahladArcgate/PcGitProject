def myfunction(data):
    data = data.iloc[:, [0, 1]].values
    for x, y in enumerate(data):
        if (x-y).all() >= 80 and x < y:
            return -10
        else:
            return 0