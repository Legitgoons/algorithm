while 1 :
    try : 
        a,b = map(int,input().split())
        if 0 < a and b < 10 :
            print(a+b)
    except :
        break