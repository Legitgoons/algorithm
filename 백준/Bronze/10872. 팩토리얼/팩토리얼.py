def fct(n):
    ans = 1
    if n > 0 :
        ans = n * fct(n-1)
    return ans

n = int(input())
print(fct(n))