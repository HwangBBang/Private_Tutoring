# # 한 줄에 정수 두 개와 문자 하나를 입력받고
# # 문자 가 "a","b","c" 중 하나라면
# # 두정수의 합의 1의자리수를 출력

# # 문자 가 "d","e" 중 하나라면
# # 두정수의 곱의 1의자리수를 출력

# # 위의 문자가 모두 아닌 경우
# # 두정수의 합과 곱의 합 의 10의 자리수를 출력하시오

# # = : 초기화
# # == : 같다.

# # 10의 나머지 0~9
# # c 의 1 자리수 가 궁금해 ?
# # c 의 10 자리수 가 궁금해 ?
# # num1, num2 = int(num1), int(num2)
# #
# ############################################
# a, b = 1, 1
# # # 한번에 2 개의 정수를 입력받아
# # 모두 3의 배수 일때 "sj3"
# # 모두 5의 배수 일때 "sj5" 를 출력하고
# # # 그렇지 않을 때 FALSE 를 출력하고

# # 3,5 순서 대로 우선순위야

# # if - elif - else ->

# # if if -> ->


# def sj(num1, num2, t):
#     return num1 % t == 0 and num2 % t == 0


# if sj(3):
#     pass
# elif sj(5):
#     pass

# # bool
# # 공통부분 : a % t == 0 and b % t == 0
# # 다르부분 : t

# # 리팩토링 / 반복되는 것을 -> 변수, 함수 로 만들어 재사용!

# # 함수?
# # a -> add1함수 -> a+1


# def add1(a):
#     a = a+1
#     return a


# # a // 10 == 2

# # 20대? 19 < a and 30 > a


# add , cnt = 0,0
# while True:
#     a = int(input())
#     if a//10==2:
#         cnt += 1
#         add += a
#     else:
#         print("%.2f"%(add/cnt))

# and,or
# and : 하면서 ,이면서 , 동시에
# or  : 하거나 ,이거나 , 여러개


# 40대니?
# 이름이 boo 거나 goo 거나 woo 면은 pass 하세요

# 8 배수 면서  1의자리가 6 이면좋겠어~

# 7배수 거나 10의자리가 3이면 좋겠어~

# if a % 3 == 0 and a % 5 == 0:
#     pass

# if a % 15 == 0:
#     pass
