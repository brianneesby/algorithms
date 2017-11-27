# Import random functions
from random import randint, shuffle

# Function to determine number of partitions of integer i with n parts
def columns_var(x, y, i, n, r):
    d = 0
    if y == 1:
        if x == 1:
            return 1
        else:
            return 0
    elif y == 2:
        return 1
    else:
        d = 0
        for e in range(x, i + 2):
            d = d + r[y-1][e]
        return d

# Recursive function to generate a random partition
def generate_random_set(a, b, z, i, c, r):
    # Declare variables
    d = 0
    e = -1

    if b > 2:
        for x in range(a, c + 2):
            e += 1
            d = d + r[b][x]
            if d >= z:
                i.append(e)
                return generate_random_set(x, b - 1, z - d + r[b][x], i, c, r)
    else:
        i.append(z - 1)
        i.append(c - sum(i))
        return i

# Pick random set
def pick_random_set(i, n):
    # Create a matrix that has (i + 1) rows and n columns
    r = {}
    for y in range(1, n + 1):
        c = {}

        for x in range(1, i + 2):
            c[x] = columns_var(x, y, i, n, r)

        r[y] = c

    print(r)

    # Pick a random number within the range 1 to sum(rows[n].values()
    z = randint(1,sum(r[n].values()))

    # Generate a random partition
    p = []
    generate_random_set(1, n, z, p, i, r)
    shuffle(p)
    o = sum(r[n].values())

    return [o, p]

# Main procedure
def main(i, n):
    # Pick random set
    s = pick_random_set(i, n)

    # Print results
    print('Integer: ' + str(i))
    print('Number of Permutations: ' + str(n))
    print('Number of Possible Sets of Permutations: ' + str(s[0]))
    print('Partitions:')
    print(s[1])
        
# Run main procedure
i = 3 # Integer
n = 7 # Number of partitions
main(i, n)

