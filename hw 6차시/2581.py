M = int(input())
N = int(input())
box = []

def prime_number_range(M, N):
    for num in range(M, N + 1):
        if num > 1:
            is_prime = True
            for i in range(2, int(num**0.5) + 1): 
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                box.append(num)

prime_number_range(M, N)

if box:
    a = sum(box)
    b = min(box)
    print(a)
    print(b)
else:
    print(-1)
