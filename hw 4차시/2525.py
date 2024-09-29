a, b = map(int, input().split())
c = int(input())
if b + c < 60:
    print(a, b+c)
elif a+(b+c)//60 > 23:
    print(a+(b+c)//60-24, b + c - (b+c)//60*60)
elif (b + c) // 60 >0:
    print(a+(b+c)//60, b + c - (b+c)//60*60)
