# 반복문 (for, while)
# 왜 필요했지?
# -> 귀찮아..
# -> 코드를 관리하기 어려워 (유지,보수)


# print() -> C++ "fprint()" -> Assembly -> 레지스터의 작동을 제어하는

# ALU + Reg + CU

#     CU
# ALU <-> Reg


# for -> 유한한 개수일 때 ,,

# # for i in range (0,5,1): -> 5번

# var = 5

# for i in range(var):
#     print(i, end=" ")


# while -> 언제 까지 반복하는 지 모를때,,,


# if condi:
#     pass

# while condi: -> break -> continue

# 수행1
# 수행2
# 수행3
# condi
# 수행1
# 수행2
# 수행3
# condi

# cnt = 0
# flag = True


# while flag:
#     if cnt == 101:
#         flag = False
#         continue
#         # break

#     cnt += 1

#     if cnt % 2 == 0:
#         print(cnt)
#     else:
#         continue


# # condition 을 확인하고 다 수행해 ,, 그러고 condition


# for i in range(5, 18, 2):
#     print(i, end=" ")

# n = int(input())

# # (시작 , 끝점 + 1 , 증가폭)
# for i in range(n, (n*5)+1, n):
#     print(i, end=" ")


i = 10
while True:
    print(i, end=" ")
    if i == 26:
        break
    i += 1
