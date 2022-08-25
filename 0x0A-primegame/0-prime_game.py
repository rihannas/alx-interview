def isWinner(x, nums):
    """Prime game"""
    if x < 1 or not nums:
        return None
    n = max(nums)
    primes = [True for _ in range(max(n + 1, 2))]
    for i in range(2, int(pow(n, 0.5)) + 1):
        if not primes[i]:
            continue
        for j in range(i * i, n + 1, i):
            primes[j] = False
    primes[0] = primes[1] = False
    c = 0
    for i in range(len(primes)):
        if primes[i]:
            c += 1
        primes[i] = c
    turns = 0
    for n in nums:
        turns += primes[n] % 2 == 1
    if turns * 2 == len(nums):
        return None
    if turns * 2 > len(nums):
        return "Maria"
    return "Ben"
