# # 큐
# from collections import deque
# n=int(input())
# word=deque()
# for _ in range(n):
#     word.append(input())

# for _ in range(n-1):
#     w=input()
#     for _ in range(len(word)):
#         if word[0]==w:
#             word.popleft()
#         else:
#             word.append(word.popleft())
# print(word[0])

# 해쉬
n=int(input())
p=dict()
for i in range(n):
    word=input()
    p[word]=1
for i in range(n-1):
    word=input()
    p[word]=0
for key, val in p.items():
    if val==1:
        print(key)
        break