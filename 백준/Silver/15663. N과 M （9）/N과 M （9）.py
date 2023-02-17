n,m = map(int,input().split()) 
arr = sorted(list(map(int,input().split()))) #정렬해서 입력받음
arr2 = []
visited = [False]*n #방문 확인용 visited

def dfs(depth,ans,arr) :
    if (len(ans) == m) : #ans길이가 m과 같다면
        print(*ans) #출력
        return 
    
    flag=0 #중복 방지용 flag
    for i in range(0, n): #arr 탐색
        if visited[i] == False and flag != arr[i] :
            ans.append(arr[i]) #i를 ans에 채워넣음
            visited[i] = True #방문 체크
            flag=arr[i] #flag에 arr[i]를 넣어줌
            dfs(depth+1,ans,arr) #확인 후 if문 통과시 return받음
            ans.pop() #그 뒤 pop
            visited[i] = False #pop했으면 되돌려주기

dfs(0,[],arr) #실행
