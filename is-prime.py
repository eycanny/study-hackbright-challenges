def is_prime(num):
    """Is a number a prime number?"""

    divisible_nums = set()

    for i in range(1, num+1):
        if num < 2:
            return False
        else:
            if num % i == 0:
                divisible_nums.add(i)
        if len(divisible_nums) > 2:
            return False
    
    return len(divisible_nums) <= 2