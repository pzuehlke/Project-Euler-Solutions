#################################
#  PROJECT EULER - PROBLEM 080  #
#################################
import time
from decimal import getcontext, Decimal

# The statement of the problem is somewhat ambiguous. One should also include
# the digit to the left of the decimal point in the count (i.e., the integer
# part).
start = time.time()

# One must work with somewhat greater precision to avoid rounding errors.
getcontext().prec = 102

SQUARES = [n**2 for n in range(11)]
NON_SQUARES = set(range(1, 100)).difference(set(SQUARES))

total = 0
for n in NON_SQUARES:
    n_string = str(Decimal(n).sqrt())
    total += int(n_string[0]) + sum([int(d) for d in n_string[2:101]])

print(total)

end = time.time()
print(f"Program runtime: {end - start} seconds")
