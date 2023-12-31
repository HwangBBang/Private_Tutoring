# # # 분기 -> 나누는 것 (divided and conquer)

# # # 여러 문제들
# # # 논리 -> 논리적 파싱  분석

# # # 케이스를 나눈다. + 문법
# # # 모든 케이스에서 성립할 수 있도록 만든다. + 문법

# # # ex)
# # # i == 2    | *: 8 번 반복! -> 0 8- (2//2 -1)
# # # i == 4    | *: 7 번 반복 -> 1 4//2 -1
# # # i == 6    | *: 6 번 반복 -> 2 6//2 -1
# # # i == 8    | *: 5
# # # i == 10   | *: 4
# # # i == 12   | *: 3
# # # i == 14   | *: 2
# # # i == 16   | *: 1


# # # if a and b:
# # #     pass

# # # if a:
# # #     if b:
# # #         pass
# # #     else:
# # #         pass
# # # else:
# # #     if b:
# # #         pass
# # #     else:
# # #         pass

# # n = 8
# # for i in range(1, n+1):
# #     if i == 1:
# #         for j in range(n):
# #             print("", end=" ")
# #         print()
# #         continue
# #     else:
# #         for k in range(1, n+1):
# #             if i <= j and j % 2 == 0:
# #                 print("*", end=" ")
# #             else:
# #                 print("@", end=" ")
# #         print()

# a = 1
# print(f"({a})")


# map()
# # 함수 DO
# # 메서드 How
# input().split(" ")
# 나누어서 입력받아.
# 한 줄에 여러개를 입력 받아요 -> X
# 한개만 입력

# 문자열 = 문자열 + 문자열
# string = subString + subString

# "abc 지민 12 @@" /string -> subString , subString
def addFive(elem):
    elem += 5
    return elem


arr = "13 14 12 15".split(" ")
print(arr)
# arr 있는 각 원소들한테 일정한 규칙을 적용시켜주고 싶어
# map
arr_1, arr_2, arr_3, a4 = map(int, arr)

arr = [arr_1, arr_2, arr_3, a4]

print(arr_1, arr_2, arr_3, a4)

arr_1, arr_2, arr_3, a4 = map(addFive, arr)
print(arr_1, arr_2, arr_3, a4)
