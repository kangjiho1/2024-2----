a, b, c = map(int, input().split())
if a == b == c:
    print(10000+1000*a)
elif a == b:
    print(1000+100*a)
elif a==c:
    print(1000+100*a)
elif b==c:
    print(1000+100*b)
elif a!=b!=c:
    d = max(a,b,c)
    print(d*100)
