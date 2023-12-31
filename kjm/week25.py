#  type / var / print,input / if / for,while

# 2중 for 문 ..
# 문제를 풀때는 분석,,,

# 0.  샘플링해라. i = 0일 때  1일 때  -> j ?? -> for 이 뭔지 파악 할 수 있다.!
# 1.  그림 혹은 갯수를 (패턴)파악한다. (가로 단위로) (우리 찍어 낼때 ->)
# 2.  내림 오름 차순을 파악한다. (for 문을 간단하게 설계하기위해서 )
# 3.  세로에 대한 규칙 파악한다. (밖 for 문)
# 4.  가로에 대한 규칙 파악한다. (안 for 문)


# ************
# *          *
# *          *
# *          *
# *          *
# ************

# n = 8

# i == 2    | *: 8 번 반복! -> 0 8- (2//2 -1)
# i == 4    | *: 7 번 반복 -> 1 4//2 -1
# i == 6    | *: 6 번 반복 -> 2 6//2 -1
# i == 8    | *: 5
# i == 10   | *: 4
# i == 12   | *: 3
# i == 14   | *: 2
# i == 16   | *: 1


# *
# **
# ***
# ****

# ****
# ***
# **
# *


# for i in range(1,n+1):
#     for j in range(i):
#     for j in range(n- (i-1)):

# for i in range(1, n*2+1):
#     for j in range(i//2+1):
#     for k in range(n - (i//2-1)):

# *

# * *
# - *

# * * *
# - * -
# - - -

# * * * *
# - * - *
# - - - *
# - - - *

# * * * * *
# - * - * -  i = 2
# - - - * -
# - - - * -  i = 4
# - - - - -

# * * * * * *
# - * - * - * i = 2
# - * - * - *
# - * - * - * i = 4
# - * - * - *
# - * - * - * i = 6

n = int(input())

for i in range(1, n+1):
    for j in range(1, n+1):
        if j % 2 == 0:  # 짝수
            if i <= j:
                print("*", end=" ")
            else:
                print("-", end=" ")
        else:  # 홀수
            if i == 1:
                print("*", end=" ")
            else:
                print("-", end=" ")
    print()


# * * * *
# * * * *
# * * * *
# * * * *

# ???????

# * * * *
# - * - *
# - * - *
# - * - *

# ???????

# * * * *
# - * - *
# - - - *
# - - - *