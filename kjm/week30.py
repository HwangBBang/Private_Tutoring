
# # # # 한번에 2 개의 정수를 입력받아

# # # # 모두 3의 배수 일때 나 모두 5의 배수 일때 "sj3","sj5" 를 출력하고
# # # # 3,5 순서 대로 우선순위야
# # # # 그렇지 않을 때 FALSE 를 출력하고

# # # if 조건에 중복되는 부분을 함수화 시키세요

# # # 모두 3의 배수 일때 /모두 K==3의 배수 일때
# # # 모두 5의 배수 일때 /모두 K==5의 배수 일때

# # # 모두 K==3의 배수 일때

# # a, b = map(int, input().split())


# # def sj(a, b, c):
# #     return a % c == 0 and b % c == 0


# # if sj(a, b, 3):
# #     print(1)
# # elif sj(a, b, 5):
# #     print(2)
# # else:
# #     print(3)


# # ASCII ?

# # ASCII
# # + I O E  -> 2진수
# # 128
# #  ,a~z,A~Z


# for i in range(65, 123, 1):
#     print(f"{i} : {chr(i)}")


# 65 : A : 0100 0001
# 66 : B : 0100 0010

chr(65)  # -> A
ord('A')  # -> 65

n = 314


cnt = 65
for i in range(1, n+1):
    for j in range(i):
        print(chr(cnt), end=" ")
        cnt += 1
        if cnt > 90:
            cnt = 65
    print()

# for i
#     for j
