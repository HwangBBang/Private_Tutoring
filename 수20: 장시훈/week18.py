
# 3÷10
# -> 몫 : 0 나머지 : 3
# 몫 • 10 + 나머지 = 3

# 13÷10
# -> 몫 : 1 나머지 : 3
# 몫 • 10 + 나머지 = 13

# 128÷2021
# -> 몫 : 0 나머지 : 128

# tmp (Temporary : 임시적인)
# tmp = 128
# a = 2021
# b = 128

# 2021 % 128 -> 101
# tmp = 101
# a = 128
# b = 101

# 128 % 101 -> 27
# tmp = 27
# a = 101
# b = 27

# 101 % 27 -> 20
# tmp = 20
# a = 27
# b = 20

# 27 % 20 -> 7
# tmp = 7
# a = 20
# b = 7

# 20 % 7 -> 6
# tmp = 6
# a = 7
# b = 6

# 7 % 6 -> 1
# tmp = 1
# a = 6
# b = 1

# 6 % 1 -> 0
# tmp = 0
# a = 1
# b = 0


# tmp = a%b
# a = b
# b = tmp

# a,b = b,a

# condition (조건)
# bool 논리 불 -> T/F

# 0 : False
# 1,-1,314,-9999 : True

# if (-9999):
#     print("3")


# 바이너리 : binary ,2개
# 0(전기가 안가),1(전기 가)

# 세제곱 = 3승 , 제곱 = 2승 , 네제곱을 = 4승
# m 의미 가 뭘까여?
# 64 = 2^6 -> 6번 반복

# 32 = 2^5 -> 5번 반복
# 16 = 2^4 -> 4번 반복 + 1번 (3* +1)

# 8 = 2^3 -> 3번 반복 + 2번 (3* +1) -> 안되네.!
# 3*(3*a+1)+1 = 8
# 5 번..

# 둘중에 하나 선택
# n이 1이 될 때 까지
# if n %2 == 0:
#     n//=2  (감소)
# else:
#     n = 3*n + 1 (증가)

# 우리는 n을 줄이는 입장이야
###########################
# 중요,
# 의미를 찾아야해 .
# m 은 반복횟수
# n을 찾아야해 .
# n을 찾기위해서 1부터 확인해봤어
# 규칙을 찾았어 . (8 = 2^3) 이되면 3번 반복하고 끝났다.!

# 2의 제곱 꼴이라면 끝나는구나~
# 2^5 되겠다!
# 더 없나? ->
# 2^5 5번이야 . 5번 / 0번
# 감소 감소 감소 감소 감소

# 2^4 4번이야 . 4번 / 1번 될 까?
# 증가 감소 감소 감소 감소
# 3*k + 1 = 16
# 3 * k = 15
# k = 5

# 2^3 3번이야 . 3번 / 2번 될 까?
# 증가 증가 감소 감소 감소
# 3*(3*k + 1)+1 = 8
# n = 4/9 -> 안되는구나 ?

# 2^3 2번이야 . 2번 / 3번 될 까?
# 증가 증가 증가 감소 감소
# 3*(3*(3*k + 1)+1)+1 = 4
# 안되는구나 ?

# 질문 ?!
