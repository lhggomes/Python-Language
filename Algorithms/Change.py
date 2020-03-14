coins = [
    100,
    50,
    25,
    5,
    1
]
total = 0
change = 75

for i in range(len(coins)):
    numCoins = change // coins[i]
    change -= numCoins * coins[i]
    total += numCoins

print(total)



'''
numCoins = 75 // 100 = 0
change = change - 0 * 100
change = change 
'''