
def is_subsequence(s, t):
    s_index, t_index = 0, 0
    while s_index < len(s) and t_index < len(t):
        if s[s_index] == t[t_index]:
            s_index += 1
        t_index += 1
    return s_index == len(s)

try:
    while True:
       
        line = input().strip()
        if not line: 
            break
        s, t = line.split()

        if is_subsequence(s, t):
            print("Yes")
        else:
            print("No")
except EOFError:
    pass
