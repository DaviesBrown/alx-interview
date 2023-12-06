#!/usr/bin/python3
"""
prime game
"""


def isPrime(num):
    """ return if a num is prime"""
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def isWinner(x: int, nums: list):
    """Returns winner of prime game"""
    player1 = "Maria"
    player2 = "Ben"
    player1_score = 0
    player2_score = 0

    # for each round in x
    for round in range(x):
        # list of consecutive numbers
        num_list = [i for i in range(1, nums[round] + 1)]
        # list of prime numbers in num_list
        prime = [i for i in num_list if isPrime(i)]
        # player's turn - even: Maria, odd: Ben
        player = 0
        # first player Maria
        for p in prime:
            for n in num_list:
                # compare each player prime number and remove factors
                if n % p == 0:
                    num_list.remove(n)
            # next player's turn
            player += 1
        # if player has only 1(no other prime) in num_list he loses
        if len(num_list) == 1 and 1 in num_list:
            if player % 2 == 0:
                player2_score += 1
            else:
                player1_score += 1

    # picking the winner
    if player1_score == player2_score:
        return None
    elif player1_score > player2_score:
        return player1
    else:
        return player2
