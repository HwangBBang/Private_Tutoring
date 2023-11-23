# def dfs(s, n):
#     if len(s) == n:
#         if s.count('1') >= 3 and s.count('2') >= 3:
#             arr.append(s)
#         return
#     for i in range(1, 3):
#         dfs(s+str(i), n)


# arr = []


# def sol(n, s):

#     dfs(s, n)
#     arr.sort()
#     for a in arr:
#         print(a)


# sol(n=7, s='')
def dfs(s, n):
    if len(s) == n:
        arr.append(s)
        return
    for i in range(1, 3):
        dfs(s+str(i), n)


arr = []


def sol(n, s):

    dfs(s, n)
    arr.sort()
    for a in arr:
        print(a)


sol(n=7, s='')
