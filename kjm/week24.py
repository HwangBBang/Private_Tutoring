# 문제를 풀때는 분석,,,

# 1.  갯수를 파악한다. (행 단위로) (우리 찍어 낼때 ->)
# 2.  내림 오름 차순을 파악한다.
# 3.  세로에 대한 규칙 파악한다. (밖 for 문)
# 4.  가로에 대한 규칙 파악한다. (안 for 문)

" "" ""*"
" ""*""*""*"


# def f(n==4)
# ********************** 24
# ***********            12
# *****                   6
# ***                     3

# def f(n==3)
# ***********            12
# *****                   6
# ***                     3

# def f(n==2)
# *****                   6
# ***                     3

# def f(n==1)
# ***                     3

# for i in range(4, 0, -1):
#     f(i)


# 홀 수 행 에서 는
# 1 2 3 4 순으로 n 까지 오름 차순
# 열을 만드는법(가로를 생성)

# i: 1 //2 +1 -> 1
# i: 3 //2 +1 -> 2
# i: 5 //2 +1 -> 3
# i: 7 //2 +1 -> 4

# for j in range(i//2 +1):
#     print("*",end=" ")
# 짝 수 행 에서 는
# n 3 2 1 순으로 0 까지 내림 차순


# n = int(input())

# for i in range(1, n + 1):
#     for _ in range(i):
#         print("* ", end="")
#     print()
#     for _ in range(n - i + 1):
#         print("* ", end="")
#     print()