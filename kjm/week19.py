# 지난 주..
# 문제를 보고 분류연습? 이런걸 했는데
# 1. 조건파악 . -> 우리가 도출해내야하는 답..
# 2. 그 답을 만족하게하는 조건 파악.
# 3. 조건을 분류.. -> 분기  A 니? B 니?
# 4. 복잡함.
# 5. 중첩. (중첩이라는 것은 굉장히 강력.)
# a = int(input())
# if a%2==0 and a>10 and a%10 == 8 and a <100 and (a//10)%2 == 0:
# -> 중첩시켜 .
# if a % 2 == 0:
#     if a > 10:
#         if a % 10 == 8:
#             if a < 100:
#                 if (a//10) % 2 == 0:
#                     print("we want it")


# 변수 -> 초기화
#     -> 타입(자료형)

# 출력 -> 옵션 2개 (end ,sep)

# 입력 -> 타입 변환
#     -> 다중 입력 (map, split)

# 분기(조건)문
# if -> else
#    -> elif
# 블럭 개념 (연관성을 기준으로 ...)

# 반복문
# 반복과정의 관계를 관찰하고 그 관계를 코드화.
# 소트.. (축약(의미를))
# for ,while + break,continue (조건문.) + flag를 도입해서 반복문 통제
#

# A not
#    B not
#        C not
#           -> ABC not

#!( A ? ?)
#    !(A B ?)
#       !(A B C)
#        print()
#      !C A B
#   !B A ?
#!A ? ?


# -> !A !B !C


# while 1 :
#     if :  -> 20 대? ->cnt,res ++
#     else : -> 20 아니니? -> 반복문 깨 ->break


# realRes = res / cnt
# cnt = 0
# n = 1

# while True:

#     if n == 1:
#         print(cnt)
#         break

#     cnt += 1
#     if n % 2 == 0:
#         n = n//2
#     else:
#         n = (n*3)+1


# 급해. 빨리 해결하고(문제 파악)
# 문제만드는방법 <- 여러개를 썪어

# 1개 혹 2개 (단번)파악할 수 있어 .
# 3개 혹 4이상 (절대로)단 번에 파악할 수 없어 .
# 분기. 쪼개가며 . 하나를 고정해가며..

# 32 -> 16(0) -> 8(1) -> 4(2) -> 2(3) -> 1(4)
# 5 -> 16(0) -> 8(1) -> 4(2) -> 2(3) -> 1(4)

# m == cnt @
# flag != 1 @ -> 의미

# 5번 시행시 1되는거요!

# 그럼 1은 어떻게 만들고있니?
#  *2,  복잡한연산
#   1
# 2 , X
# 4 , X
# 8 , X
# 16 , X
# 32 , 5
