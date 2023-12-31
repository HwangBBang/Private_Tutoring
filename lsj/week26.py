# # 조건문 if
# # 특정 조건에 따라 코드를 실행 : 조건문
# condition = True

# if condition:
#     # 실행
#     print()
# else:  # not, 여사건.
#     # codition 이 True 가 아닐 때 실행되는 곳.
#     print()

# # elif else + if

# name = input()
# h = input()
# if name == "kim":
#     print('kim')
# if name == "lee":
#     print('lee')

# # -----------가독성-----------

# if name == "kim":
#     print('kim')
# elif name == "lee":
#     print('lee')

# # nest : 둥지
# # nested : 둥지화(된) == 중첩된


# if name == "kim" and h >= 180:
#     print('kim')

# if name == "kim":
#     if h >= 180:
#         print('kim')


# if name == "kim" or name == "lee":
#     print('hi')

# if name == "kim":
#     print('hi')
# if name == "lee":
#     print('hi')

# # -----다중조건-------

# # A,B,C,D,F
# grade = input()
# if grade == "A":
#     print("A")
# elif grade == "B":
#     print("B")
# elif grade == "C":
#     print("C")
# elif grade == "D":
#     print("D")
# elif grade == "F":
#     print("F")
# else:
#     print("Not vaild grade")

# a = int(input()) #10
# #7
# if a % 2 == 0:
#     print(a//2) # 10 / 5
# if a % 2 == 1: #
#     print((a+1)//2)


# a = 5
# # 5
# if a % 2 == 0:
#     a = (a//2)

# if a % 2 == 1:
#     a = (a+1)//2

# else:
#     a = (a+1)

# # | 계산,초기화 | 출력 |


a, b = map(int, input().split())

# a 크니
# b 크니
# a b 가 같니

# a
# b

# ---

# a == b

# 정수 a가 3의 배수라면 YES를,
# 아니라면 NO를 출력하고,

# 또 5의 배수라면 YES를,
# 아니라면 NO 출력하는 프로그램을 작성해보세요.
