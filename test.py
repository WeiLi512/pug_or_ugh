# Python program to solve 
# Gold Mine problem 

MAX = 100

def getMaxGold(gold):
    n = len(gold)
    goldTable = [[{'golds': 0} for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if gold[i][j] == -1:
                goldTable[i][j]['golds'] = -1
                continue

            goldTable[i][j]['golds'] = gold[i][j]
            if i != 0 and j != 0:
                if goldTable[i-1][j]['golds'] > goldTable[i][j-1]['golds']:
                    goldTable[i][j]['golds'] += goldTable[i-1][j]['golds']
                    if goldTable[i-1][j]['golds'] == -1:
                        goldTable[i][j]['golds'] = -1
                    goldTable[i][j]['prev_node'] = (i-1, j)
                else:
                    goldTable[i][j]['golds'] += goldTable[i][j-1]['golds']
                    if goldTable[i][j-1]['golds'] == -1:
                        goldTable[i][j]['golds'] = -1
                    goldTable[i][j]['prev_node'] = (i, j-1)
            elif i == 0 and j != 0:
                goldTable[i][j]['golds'] += goldTable[i][j-1]['golds']
                if goldTable[i][j-1]['golds'] == -1:
                    goldTable[i][j]['golds'] = -1
                goldTable[i][j]['prev_node'] = (i, j-1)
            elif i != 0 and j == 0:
                goldTable[i][j]['golds'] += goldTable[i-1][j]['golds']
                if goldTable[i-1][j]['golds'] == -1:
                    goldTable[i][j]['golds'] = -1
                goldTable[i][j]['prev_node'] = (i-1, j)
            else:
                goldTable[i][j]['prev_node'] = (-1, -1)

    return goldTable


def update(gold, goldTable):
    n = len(gold)
    prev_i, prev_j = n-1, n-1
    while True:
        gold[prev_i][prev_j] = 0
        prev_i, prev_j = goldTable[prev_i][prev_j]['prev_node']
        if prev_i == -1:
            break

        print(prev_i, prev_j)
    return gold


def print_array(arr):
    for i in range(len(arr)):
        print(arr[i])


# Driver code
gold = [[0, 1, 1],
        [1, 0, 1],
        [1, 1, 1]]

# gold = [[0, 1, 1],
#         [1, 0, -1],
#         [1, 1, -1]]


n = len(gold)

goldTable = getMaxGold(gold)
print_array(goldTable)

golds = goldTable[n-1][n-1]['golds']

if golds == -1:
    print('no path')
else:
    update(gold, goldTable)
    print_array(gold)
    goldTable = getMaxGold(gold)
    golds += goldTable[n-1][n-1]['golds']
    print(f'golds: {golds}')


# This code is contributed 
# by Soumen Ghosh.			 
