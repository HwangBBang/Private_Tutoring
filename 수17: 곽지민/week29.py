import math
# import urllib
import numpy


# 1*1  1*2
# 1*3  1*4
# 1*5  1*6
# 1*7  1*8
# 1*9  1*10
# 1*11 1* 12
# 1*13 1* 14
# 1*15 1* 16
# 1*17 1* 18
# 1*19

# 2 X (10 * 19 )


# 관점 : 추상화
# 어떤 사람의 얼굴을 표현.
# >_<

# divide & conquer 나눠서 하나씩 정복해나가자
# -> 치환
# x*f(x^4)/x^4
# √^3/4t*f(t)/t

# 1:a 2:b 3:c

# ㅁ
# ㅁㅁㅁㅁㅁ
# ㅁㅁ
# ㅁㅁㅁㅁ
# ㅁㅁㅁ
# ㅁㅁㅁ
# ㅁㅁㅁㅁ
# ㅁㅁ
# ㅁㅁㅁㅁㅁ
# ㅁ


# 버블 정렬
# n개 가 있어요
# arr = [3, 1, 2, 4, 32, 3, 241, 4, 14, 12, 41, 5, 3125, 3, 53, 54, 35, 5, 15, 4, 143, 24,
#        124, 124, 214, 2, 412, 4, 14, 12, 42, 5, 32, 43, 6543, 745, 8, 458, 68, 48, 48, 8, 8]

# # O(n^2)
# for i in range(len(arr)):
#     for j in range(len(arr)-i-1):
#         if arr[j] < arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]

# i 를 길이 만큼 반복해 i : 0 1 2 3
# j 3 2 1 0
# print(arr)

# len()  : 길이
# print(pow(2, 4))
# print(2**4)
# max()
# min()
arr = [1, 34, 2, 7]
# print(max(arr))
# print(sum(arr))

# for i in arr:
#     print(i, end=" ")


# print(sorted(arr))
# arr = [1, 34, 2, 7]

# arr.sort()
# print(arr)


# print(int(math.log2(16)))
# print(math.pi)

print(math.ceil(3.141556))   # 올림
print(math.floor(3.141556))  # 내림
print(round(3.741556))  # 반올림

# 절대값 |-2| == 2
print(abs(-2), abs(2))  # 절대값

# 책 : 모듈 module (관련된 데이터 정보들을 묶어놓은것)
