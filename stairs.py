def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 1:
        return 1
    else:
        return pow(2, n - 2) + 1
        


print(climbStairs(4))

