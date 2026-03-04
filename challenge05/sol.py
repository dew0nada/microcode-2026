import sys
import math

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(n ** 0.5) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True

stbc = 0
bits = []

with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        
        left, right = line.split('|')
        value = int(left.strip())
        ml , mr = right.strip().split(':')
        ml = ml.strip()
        mr = mr.strip()
        if ml == mr:
            stbc += 1
            abs_val = abs(value)
            if abs_val == 0:
                continue
            
            if is_prime(abs_val):
                bits.append(1)
            else:
                bits.append(0)

N = len(bits)
if N == 0:
    print(0)
else:
    shift = stbc % 7
    power = 0
    
    for i in range(1, N + 1):
        E = ((i + shift - 1) % N) + 1
        
        if bits[i - 1] == 1:
            power += E * E
        else:
            power -= math.gcd(E, N)
    
    print("part 1:" + str(power))


#part 2

N = len(bits)

if N < 5:
    print(0)
else:
    mutated = []
    
    for i in range(N - 4):
        window = bits[i:i+5]

        W = (
            window[0] * 16 +
            window[1] * 8 +
            window[2] * 4 +
            window[3] * 2 +
            window[4]
        )
        
        if W % 3 == 0:
            mutated.append(1)
        elif W % 5 == 0:
            mutated.append(0)
        else:
            mutated.append(sum(window) % 2)

    M = mutated
    length = len(M)

    def find_period(arr):
        n = len(arr)
        for L in range(1, n + 1):
            if n % L == 0:
                valid = True
                for i in range(n):
                    if arr[i] != arr[i % L]:
                        valid = False
                        break
                if valid:
                    return L
        return n

    L = find_period(M)

    position_sum = 0
    for i in range(length):
        if M[i] == 1:
            position_sum += (i + 1)

    entropy = position_sum * L

    print("part 2:" + str(entropy))
