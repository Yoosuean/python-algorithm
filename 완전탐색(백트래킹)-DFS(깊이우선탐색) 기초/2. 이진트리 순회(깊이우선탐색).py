#전위순회(부,왼,오)
def DFS1(v):
    if v>7:
        return
    else:
        print(v, end=" ")
        DFS1(v*2)
        DFS1(v*2+1)

#중위순회(왼,부,오)
def DFS2(v):
    if v>7:
        return
    else:
        DFS2(v*2)
        print(v, end=" ")
        DFS2(v*2+1)

#후위순회(왼,오,부)
def DFS3(v):
    if v>7:
        return
    else:
        DFS3(v*2)
        DFS3(v*2+1)
        print(v, end=" ")
DFS1(1)
print()
DFS2(1)
print()
DFS3(1)