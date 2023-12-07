#!/usr/bin/python3
"""
Maria and Ben are playing a game. Given a set of
consecutive integers starting from 1 up to and
including n, they take turns choosing a prime
number from the set and removing that number and
its multiples from the set. The player that cannot
make a move loses the game.

They play x rounds of the game, where n may be
different for each round. Assuming Maria always goes
first and both players play optimally, determine who
the winner of each game is.

Prototype: def isWinner(x, nums)
where x is the number of rounds and nums is an array of n
Return: name of the player that won the most rounds
If the winner cannot be determined, return None
You can assume n and x will not be larger than 10000
You cannot import any packages in this task
Example:

x = 3, nums = [4, 5, 1]
First round: 4

Maria picks 2 and removes 2, 4, leaving 1, 3
Ben picks 3 and removes 3, leaving 1
Ben wins because there are no prime numbers left for
Maria to choose
Second round: 5

Maria picks 2 and removes 2, 4, leaving 1, 3, 5
Ben picks 3 and removes 3, leaving 1, 5
Maria picks 5 and removes 5, leaving 1
Maria wins because there are no prime
numbers left for Ben to choose
Third round: 1

Ben wins because there are no prime numbers for
Maria to choose
Result: Ben has the most wins
"""


def isWinner(x, nums):
    '''finds the winner'''
    winnerCounter = {'Maria': 0, 'Ben': 0}

    for i in range(x):
        roundWinner = isRoundWinner(nums[i], x)
        if roundWinner is not None:
            winnerCounter[roundWinner] += 1

    if winnerCounter['Maria'] > winnerCounter['Ben']:
        return 'Maria'
    elif winnerCounter['Ben'] > winnerCounter['Maria']:
        return 'Ben'
    else:
        return None


def isRoundWinner(n, x):
    '''find round winner'''
    list = [i for i in range(1, n + 1)]
    players = ['Maria', 'Ben']

    for i in range(n):
        # get current player
        currentPlayer = players[i % 2]
        selectedIdxs = []
        prime = -1
        for idx, num in enumerate(list):
            # if already picked prime num then
            # find if num is multipl of the prime num
            if prime != -1:
                if num % prime == 0:
                    selectedIdxs.append(idx)
            # else check is num is prime then pick it
            else:
                if isPrime(num):
                    selectedIdxs.append(idx)
                    prime = num
        # if failed to pick then current player lost
        if prime == -1:
            if currentPlayer == players[0]:
                return players[1]
            else:
                return players[0]
        else:
            for idx, val in enumerate(selectedIdxs):
                del list[val - idx]
    return None


def isPrime(n):
    # 0, 1, even numbers greater than 2 are NOT PRIME
    if n == 1 or n == 0 or (n % 2 == 0 and n > 2):
        return False
    else:
        # Not prime if divisable by another number less
        # or equal to the square root of itself.
        # n**(1/2) returns square root of n
        for i in range(3, int(n**(1/2))+1, 2):
            if n % i == 0:
                return "Not prime"
        return True
