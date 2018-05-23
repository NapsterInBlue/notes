def getValues(items, pocket):
    val = 0
    weight = 0
    for item in pocket:
        weight += items.get(item, [0])[0]
        val += items.get(item, [0,0])[1]
    return weight, val

def knapsack(items, sack_size):
    sack = [[set() for x in range(sack_size)] for y in range(len(items))]

    for i, item in enumerate(items):
        weight, value = getValues(items, [item])

        for w in range(1, sack_size+1):
            # up = [i-1][j] if not the first row, else empty
            if i != 0:
                up = sack[i-1][w-1]
            else:
                up = set()
            up_v = getValues(items, up)

            # get topLeft cell [i-1][j-weight], empty if off grid
            newC = w - weight - 1
            tl = set()
            if newC >= 0:
                tl = tl.union(sack[i-1][newC])
            tl_v = getValues(items, tl)

            # if up is empty, make it this item
            if up == set():
                sack[i][w-1].add(item)

            # comparing up against topLeft
            tlWorthMore = up_v[1] < tl_v[1] + value
            tlFitsWeight = weight + tl_v[0] <= w
            if tlWorthMore and tlFitsWeight:
                tl.add(item)
                sack[i][w-1] = tl

            # all else fails, inherit from up
            else:
                sack[i][w-1] = up.copy()
    optBundle = sack[-1][-1]
    print getValues(items, optBundle)[1], ':', optBundle

if __name__ == '__main__':
    items = {}
    items['water'] = [3, 10]
    items['book'] = [1, 3]
    items['food'] = [2, 9]
    items['jacket'] = [2, 5]
    items['camera'] = [1, 6]

    knapsack(items, 6)

    items = {}
    items['guitar'] = [1, 1.5]
    items['laptop'] = [3, 2]
    items['stereo'] = [4, 3]
    items['ipod'] = [1, 2]
    items['kindle'] = [1, 1]

    knapsack(items, 4)