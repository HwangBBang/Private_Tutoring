# # 1
# n, m = map(int, input().split())
# A = list(map(int, input().split()))

# 곽지순 : 여자
# 곽지순 = 남자(곽지순)

# A = list((1, 3, 4, 532, 131))
# B = list(map(int, input().split()))
# A.extend(B)
# A.sort()
# print(*A)

# 2차원을 초기화 해
# 2차원을 입력 .
# a = [[1, 2, 3, 4], [4, 5, 6, 7], [-1, -2, -3, -4]]
# print(a[2][1])

# for elem in reversed(A):
#     print(elem, end=" ")
# # [0, 1, 2, 4, 5, 6, 8]
# # 0 1 2 4 5 6 8

# 2
# M -> 0~M-1
n, m = map(int, input().split(' '))

# n : M진법으로 이뤄진 수
# M -> 10 / 진법
# 2 -> 10  / ?
# 01 -> 1
# 00 -> 0
# 10 -> 2
# 1(4) 1(2) 1(1) -> 7


# 3
# N, M, K = map(int, input().split())
# # N  : 세로
# # M  : 가로

# # 5 4 2
# # ABBA
# # BBBA
# # BBBB
# # AAAA
# #

# arr = [0]*N # [0,0,0,0,0]

# for i in range(N):
#     arr[i] = input().split()

# print(N*M)


# 4


# 5
# print("\ /\\")
# print(") ( ')")
# print("( / )")
# print("\(__)|")

# print('''\ /\\
# ) ( ')
# ( / )
# \(__)|''')

# print(r'''\ /\
# ) ( ')
# ( / )
# \(__)|''')


# 6
a, b, c = map(int, input().split())
if a == b:
    if a == c:
        print(10000+a*1000)
    else:
        print(1000+a*100)
else:
    if a > c:
        if a > b:
            print(a*100)
    elif b > c:
        if b > a:
            print(b*100)
    else:
        print(c*100)
