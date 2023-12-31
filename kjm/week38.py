
# # map 각 원소들을 형변환
# # int('1'), int('2'), int('3'), int('4')

# # input 기본 str
# # a,b,c = map(int,input().split())

# # a = int(a) b = int(b) c = int(c)

# # arr = list(input().split())
# # for i in range(len(arr)-1, -1, -1):
# #     print(arr[i], end=" ")
# # print()

# # for i in range(1, len(arr)+1):
# #     print(arr[-i], end=" ")
# # print()

# # for elem in reversed(arr):
# #     print(elem, end=" ")
# # print()


# # 숫자 받는데, 250 종료 조건 . -> 평균, 합.

# # 배열  append, pop , arr[ :i] , sum(arr[ :i])
# arr = list(map(int, input().split()))
# for i, elem in enumerate(arr):  # elem = arr[i]
#     if elem >= 250:
#         arr = arr[:i]
#         break
# # 3 4 2 1 250 23 4 1 45 5
# # 3 , 4, 2, 1,
# sum = sum(arr)
# avg = sum/len(arr)
# print(sum, avg)


# N 가지
# 10, 5이상
# 50, 15이상
# 80, 5이상
# 1000 5이상

# 적게 돌려 주고 싶다? 비싼 동전을 많이 돌려주면 되네??
# 욕심 그득 그득 -> 그리디(욕망, 탐욕적) 알고리즘
# 현재 의 최고의 선택이 최고의 결과를 만들거라는 오만함
# 냅색 혹은 백트랙킹 알고리즘 활용


n, s = map(int, input().split())
value = [0]*n
least = [0]*n

# n 가지 동전 ,S 액수
# 입력[0]  :동전 얼마짜리인지
# 입력[1]  :최소한 이 만큼은 써라

for _ in range(n):
    v, l = map(int, input().split())
    value.append(v)
    least.append(l)

cnt = 0

# 21 줘야되는데,  each least 쓰라며.
for v, l in zip(value, least):
    s -= l*v

cnt += sum(least)

value.sort(reverse=True)


# 21 - 15
# 6

print(cnt)
