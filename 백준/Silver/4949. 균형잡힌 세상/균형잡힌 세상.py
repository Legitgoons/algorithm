import sys

while True :
    line = input()
    stact = []
    
    if line == '.' :
        break

    for i in line :
        if i == '(' or i == '[' or i == ')' or i == ']' :
            if i == '(' or i == '[' :
                stact.append(i)
            elif i == ')' :
                if len(stact) == 0 :
                    stact.append(i)
                elif stact[-1] == '(' :
                    stact.pop()
                else :
                    stact.append(i)
            elif i == ']' :
                if len(stact) == 0 :
                    stact.append(i)
                elif stact[-1] == '[' :
                    stact.pop()
                else :
                    stact.append(i)

    if i == '.' :
        if len(stact) == 0 :
            print('yes')
        else :
            print('no')