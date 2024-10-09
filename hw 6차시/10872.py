N = int(input())
def factorial(N):
    if N == 1 or N ==0:
        print(1)
    elif N >1:
        a = N * (factorial(N) - 1)
    return a
print(factorial(N))
