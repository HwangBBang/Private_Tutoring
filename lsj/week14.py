# map() , split()

# 출력
# print() / # 옵션 end= "\n"  sep = " "

# 문자열 : 배열

# 입력
# input() / 기본 자료형이 str / 형변환 int(input()) 1줄에 한개.

# 5 3 7
a, b, c = input().split()
a, b, c = "5 3 7".split(" ")
a, b, c = "5", "3", "7"


# map(type , input().split( ))

# 5,3,7
a, b, c = map(int, input().split())
a, b, c = map(int, "5 3 7".split())
a, b, c = map(int, "5", "3", "7")
a, b, c = int("5"), int("3"), int("7")
a, b, c = 5, 3, 7


# 조건문 (분기문)

# if - elif - else


# 반에 A,B,C,D

# if A:
#     pass
# elif B:
#     pass
# elif C:
#     pass
# else:
#     pass


# 반에 A,B,C,D 동아리를 가입한 친구들이 있어요
# 여러개 가입한 친구도 있어요

# if A:
#    pass
# if B:
#    pass
# if C:
#    pass
# if D:
#    pass


# 증상,온도 세명의 사람
# str , int
# a_1, a_2 = map(str, input().split())
# a_2 = int(a_2)

# b_1, b_2 = map(str, input().split())
# b_2 = int(b_2)

# c_1, c_2 = map(str, input().split())
# c_2 = int(c_2)

# a가 클때 ,
# b가 클때 ,
# c가 클때,
