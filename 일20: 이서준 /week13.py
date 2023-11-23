
# # print()  # () : 버튼
# # # 프린트 함수의 인자를 터미널출력
# # print(1)  # 인자는 type:int 과 value:1 , 1개
# # print(7, "2")  # 인자는 type:int,str 과 value:7,"2" , 2개
# # # 옵션 sep = " "
# # print(7, "2", sep="sep")
# # # 옵션 end = "\n" (new line)

# # # type 을 왜 알아야하고 왜 필요 할까?
# # # 관리, 연산의 범위를 제한함으로써 규칙성 및 정형성
# # # 1 + True (x)

# # # 문자열 = 문자열 + 문자열
# # # 문자열 = 문자(열) + 문자(열) +문자(열) + 문자(열)

# # # "d"+"f"+"o"+"uia"+"hfiehf"
# # # print("32"*3) # 곱셈은 더하기의 반복 연산이야!


# # # 1+1 : 2        / 2
# # # "1"+"1" : "11" / 11
# # print(1+1)  # : 2        / 2
# # print("1"+"1")  # : "11" / 11

# # # 인자란 함수에 전달되는 값
# # print("13123", 2132, 2*1, 2+2, sep="||")

# # 입력 input() 은 디폴트 타입이 : str
# # 터미널을 통해서 소스코드로
# # 그래서 정수쓰려면 int 형 변환을 해줘야해요

# # print("99"+"99") # 9999
# # print(int("99")+int("99"))

# a = input("입력해줘 :")

# # 다중 입력..? map , split
# v1, v2 = map(int, input().split())
# # map(type, 입력과 구분방법)

# # 정수 k,h,m,n 각 변수에 입력을 한줄에 받고
# # 이들 모두를 더한값 과 모두 곱한값을 | 을 구분해서 출력하시오

# # 연산
# # + , - , * , //, % , / , **

# # if 분기문

# # if - else
# condition = True

# if condition:
#     print("true")
# else:
#     print("false")

# # if - else
# # condition = 1

# # if condition == 1:
# #     print(1)
# # elif condition == 2:
# #     print(2)
# # else:
# #     print("false")


# # if 1 :
# #     pass
# # if 1 :
# #     pass

# a = 32
# # and : 하면서,이면서 (동시에)

# if a % 4 == 0 and a > 30:
#     print("짱")

# if a % 4 == 0:
#     if a > 30:
#         print("짱")

# # or : 이거나 (하나라도~ )


# # =========================================

# if A :
# #    -> A[ ] B[ ] C[ ] D[ ] E[ ] F[] G[]
#     if B :
#     #   -> A[ ] B[ ] C[ ] D[ ] E[ ] F[] G[]
#         if not C :
#         # -> A[ ] B[ ] C[ ] D[ ] E[ ] F[] G[]
#         elif not G and not F:
#         # -> A[ ] B[ ] C[ ] D[ ] E[ ] F[] G[]
#         else :
#         #  -> A[ ] B[ ] C[ ] D[ ] E[ ] F[] G[]
#     elif D and E:
#     #   -> A[ ] B[ ] C[ ] D[ ] E[ ] F[] G[]
#     else :
#     #   -> A[ ] B[ ] C[ ] D[ ]  E[ ] F[] G[]
# else :
# #    -> A[ ] B[ ] C[ ] D[ ] E[ ] F[] G[]
#      if F :
#      #  -> A[] B[ ] C[ ] D[ ] E[ ] F[] G[]
#      if G :
#      #  -> A[ ] B[ ] C[ ] D[ ] E[ ] F[] G[]

# # ============================================
# # 조건 | - 짝수니? 홀수니?
# # 조건 | - 8의배수니? 그렇지않니?
# # 조건 | - 1의자리가 3이니? 그렇지않니?
# # 조건 | - 홀수이면서 1의 자리가 5 이니?
# # 조건 | - 짝수이면서 5의 배수이니?
# # 조건 | - 10의 자리가 7이니?


# # 조건 | - 소수이니?
flag = True
num = 50
for i in range(2, num, 1):
    if num % i == 0:
        flag = False
        break

if flag:
    print("소수야")
else:
    print("소수가아니야")
