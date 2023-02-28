import sys
read = lambda : sys.stdin.readline() 

n = int(input()) #노드 개수 N
tree = {} #이진 트리
for _ in range(n): #입력받기
    a,b,c = read().split()
    tree[a] = [b,c]

def pre(root): #전위
    if root != '.':
        print(root,end='')
        pre(tree[root][0])
        pre(tree[root][1])

def inorder(root): #중위
    if root != '.':
        inorder(tree[root][0])
        print(root,end='')
        inorder(tree[root][1])

def post(root): #후위
    if root != '.':
        post(tree[root][0])
        post(tree[root][1])
        print(root,end='')

pre('A')
print()
inorder('A')
print()
post('A')