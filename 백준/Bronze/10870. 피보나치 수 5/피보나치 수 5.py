def fb(n):
    ans = 1
    if n == 0 :
        ans = 0
    elif n == 1 :
        ans = 1
    elif 1 < n :
        ans = fb(n-2)+fb(n-1)
    return ans

n = int(input())
print(fb(n))