n,m = map(int,input().split()) 
arr = sorted(list(set(map(int,input().split())))) #중복 제거 후, 정렬해서 입력받음

def dfs(depth,ans,arr) :
    if (len(ans) == m) : #ans길이가 m과 같다면
        print(' '.join(map(str, ans))) #출력
        return #후 return

    for i in arr: #arr 탐색
        ans.append(i) #i를 ans에 채워넣음
        dfs(depth+1,ans,arr) #확인 후 if문 통과시 return받음
        ans.pop() #그 뒤 pop

dfs(0,[],arr) #실행