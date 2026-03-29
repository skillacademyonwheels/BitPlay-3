def isPowerofEight(n):
###  Using bit manipulation to check if a number is a power of 8
    if n <= 0:
        return False
    if (n & (n - 1)) != 0:
        return False
    count = 0
    while n > 1:
        n >>= 1
        count += 1
    return count % 3 == 0


print(isPowerofEight(1))  # True
print(isPowerofEight(8))  # True
print(isPowerofEight(64)) # True
print(isPowerofEight(45))  # False