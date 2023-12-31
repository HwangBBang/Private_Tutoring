# # n, m = map(int, input().split())
# # num = list(map(int, input().split()))
# # b_num = list(map(int, input().split()))
# # # print(bnum,num,sep="\n")
# # # num=n의 수열
# # # b_num=m의 수열
# # # num.extend(b_num)
# # n_num = num + b_num
# # num.sort()
# # # print(num)
# # print(n_num)


# # # ________________________________________
# # 2

# # # ________________________________________
# # 3
# # n, m, k = map(int, input().split(' '))
# # # arr = [0]*n # ---> [0,0,0..n]
# # arr = [input() for _ in range(n)]
# # for _ in range(k):
# #     for line in range(n):
# #         for elem in arr[line]:
# #             print(elem*k, end="")
# #         print()
# # '***.'
# # '*..*'
# # '***.'
# # '*..*'
# # '***.'
# # # ________________________________________
# # 4
# # # 49 26 27 28 29 30 31
# # # 48 25 10 11 12 13 32
# # # 47 24  9  2  3 14 33
# # # 46 23  8  1  4 15 34
# # # 45 22  7  6  5 16 35
# # # 44 21 20 19 18 17 36
# # # 43 42 41 40 39 38 37

# # ㅁ ㅁ ㅁ ㅁ ㅁ
# # ㅁ ㅁ 2 3 ㅁ
# # ㅁ 0 1 4 ㅁ
# # ㅁ 7 6 5 ㅁ
# # ㅁ ㅁ ㅁ ㅁ ㅁ

# # 2,2 - > 1,2
# # -1,0 위

# # 1,2 - > 1,3
# # 0,1 오른쪽

# # 1,3 - > 2,3
# # 1,0 아래
# # 2,3 - > 3,3
# # 1,0 아래

# # 3,3 - > 3,2
# # 0,-1 왼쪽
# # 3,2 - > 3,1
# # 0,-1 왼쪽

# # 위 오 아아 왼왼 위위위 오오오 아아아아 왼왼왼왼 위위위위(위break)
# n = int(input())
# graph = [[0]*n for _ in range(n)]
# d_x = [-1, 0, 1, 0]
# d_y = [0, 1, 0, -1]
# # start point
# s_i, s_j = n//2, n//2
# cnt = 1
# graph[s_i][s_j] = cnt
# i, j = 0, 0
# while True:
#     cnt += 1
#     cur_i, cur_j = s_i + d_x[(i) % 4], s_j+d_y[(j) % 4]
#     next_i, next_j = s_i + d_x[(i+1) % 4], s_j+d_y[(i+1) % 4]
#     if graph[next_i][next_j] != 0:  # 갈 수 없다면
#         graph[cur_i][cur_j] = cnt
#     else:  # 갈 수 있다면
#         graph[next_i][next_j] = cnt
#     if next_i == 0 and next_j == 0:
#         break


# print(graph)
# # # ________________________________________
# # print("\\ /\\")
# # print(") ( ')")
# # print("( / )")
# # print("\\(__)|")
# # # _________________________________________
# # t_list=테스트할때 중복확인용list
# # tast_all=적용할 조건 확인용함수


# def tast_all(num1, num2, num3):
#     t_list = [num1, num2, num3]
#     t_list = list(set(t_list))
#     if len(t_list) == 1:
#         res = 10000+t_list(0)*1000
#         return res
#     elif len(t_list) == 2:
#         if num1 == num2:
#             res = 1000+num1*100
#             return res
#         elif num1 == num3:
#             res = 1000+num3*100
#             return res
#         elif num3 == num2:
#             res = 1000+num3*100
#             return res
#     else:
#         return False


# a, b, c = map(int, input().split())

# res1 = tast_all(a, b, c)
# if tast_all == False:
#     L_list = list(a, b, c)
#     L_list.sort()
#     res = L_list(2)*100
# print(res1)

# local 지역
a = 0
# global 전역
global b
b = 0


def set5():
    return 5
# UnboundLocalError: cannot access local variable 'a' where it is not associated with a value


a = set5()
print(a)
print(b)
