def hanoi_algorithm(n, from_, with_, to_):
    if n == 1 :
        print(from_,to_)
    else :
        hanoi_algorithm(n-1, from_, to_, with_)
        print(from_,to_)
        hanoi_algorithm(n-1, with_, from_, to_)

n = int(input())
print(2**n-1)
hanoi_algorithm(n,1,2,3)
