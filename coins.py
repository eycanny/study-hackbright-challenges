def coins(num_coins):
    """Find change from combinations of `num_coins` of dimes and pennies.

    This should return a set of the unique amounts of change possible.
    """

    possible_change = set()

    for amount in range(1, (10 * num_coins + 1)):
        for coin in range(0, num_coins + 1):
            if amount % (coin + 10 * (num_coins-coin)) == 0:
                possible_change.add(amount)

    return possible_change
