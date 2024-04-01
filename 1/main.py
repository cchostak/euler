# Find the sum of all the multiples of 3 or 5 below 1000.
def sum_of_multiples(n):
    return sum(x for x in range(n) if x % 3 == 0 or x % 5 == 0)

print(sum_of_multiples(1000))
# 233168