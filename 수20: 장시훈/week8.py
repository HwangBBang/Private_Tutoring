# if A :
# #    -> A[ ] B[ ] C[ ] D[ ] E[ ] F[] G[]
#     if B :
#     #   -> A[ ] B[ ] C[ ] D[ ] E[ ] F[] G[]
#         if not C :
#         # -> A[ ] B[ ] C[ ] D[ ] E[ ] F[] G[]
#         else :
#         #  -> A[ ] B[ ] C[ ] D[ ] E[ ] F[] G[]
#     elif D :
#     #   -> A[ ] B[ ] C[ ] D[ ] E[ ] F[] G[]
#     else :
#     #   -> A[ ] B[ ] C[ ] D[ ]  E[ ] F[] G[]
# else :
# #    -> A[ ] B[ ] C[ ] D[ ] E[ ] F[] G[]
#      if F :
#      #  -> A[] B[ ] C[ ] D[ ] E[ ] F[] G[]
#      if G :
#      #  -> A[ ] B[ ] C[ ] D[ ] E[ ] F[] G[]
# ###############################################
# 반복문 for , while
# 제어  continue , break
# continue : 아래 것들 건너 뛰고 맨위로 가서 조건 체크
# break : 반복문을 즉시 깨부신다

# for문 / 반복 정도 및 범위를 알 때
# for i in range(시작포인트, 종결포인트(전까지), 접근방법(시작 -> 종결)) :

# while 문 / 반복 정도 및 범위를 모를 때 (실행을 통해 알 수 있을 때)
# while True/False :
# -> 반복하는 횟수를 저장하는 변수 cnt , num 을 만들어 활용가능.
# -> 반복문을 실행할지 말지를 저장하는 flag 변수를 만들어 활용가능 (feat. "continue")

# if 문
# if 조건 :

# if , if - else , if - elif - else
# 조건문을 작성하거나 해석할 때, 같은 계층을 먼저 처리합니다.

# 입력.
# input()
# map(int,input().split())

# input() 의 형 변환,  input()기본형은 str -> int,float
# str -> int / int(input())
# str -> float / float(input())

# 출력.
# print()
# 옵션들... end = "\n", sep = " "

# 소수점 컨트롤 .
# "%.1f" %(a+b) -> 1개의 인자야 ..

# 함수 어떤 동작을 모듈화

# [함수] 앞으로 움직여 (X) -> 얼만큼?

# [함수] x축의 양의 방향으로 1만큼 움직여!
def moveOnsStep(posX):
    for i in range(100):
        posX += 31415
    return "hi"
# def : 함수를 정의할 때
# moveOnsStep이라는 함수는 밑에같은 내용이야 (의미야)

# 함수의 이름 : moveOnsStep

# posX : 매개변수 = 파라미터 ,인자 = 아규먼트 / 함수한테 어떤 값을 전달하는거야 .
# 현재 X축의 위치를 전달 하는 거지 .

# return : 반환하다. (되돌려주다) 함수를 끝내고(break) 주는 기념품!

# 함수를 쓰면 뭐가좋아요?

# a = moveOnsStep(0)
# print(a)


# 문제를 풀때, "샘플링 "
# 시훈이 가 코드르 짜 그리고 검증!
# 입출력예제로 예를 들어 , 입력이 3
# a = int(input())
# a = 3
# 한줄씩 진행시켜가 옳바른 결과 도출을 해내는지?
# 정리하면 , 내가 실행코드의 결과가 뭐가나오는지 생각해라. (그냥 실행누르지말고 상상부터 해라 )

# A:3의배수
# B:3 6 9 중 하나라도 있다면..?
# if A or B: -> 조건 만족
# if A :
# else :
#     if C1:
#     elif C2:
#     elif C3:
#     elif D1:
#     elif D2:
#     elif D3:
# 3 13 33 6 66 61
# 100까지 두 자리수 _ _ , _

# C: 1의자리가 3 6 9
# C1: 1의자리가 3
# C2: 1의자리가 6
# C3: 1의자리가 9

# D: 2의자리가 3 6 9
# D1: 2의자리가 3
# D2: 2의자리가 6
# D3: 2의자리가 9

# 모르면 물어라. "3,6,9하나라도 존재한다면" ?

# 3하나 존재한다면 & 3두개 존재한다면
# 앞(2자리수)이랑 뒤(1의자리수) .

# (1,2자리수)두개 존재한다면

# 3,6,9세개 존재한다면 (X)

# <1의 자리수>
# (i % 10) == 3:
# (i % 10) == 6:
# (i % 10) == 9:

# (i % 10)%3 == 0:

# <2의 자리수>
# (i // 10) == 3:
# (i // 10) == 6:
# (i // 10) == 9:

# (i // 10)%3 == 0:


# 31//10 => 3
# 3_, 6_, 9_
