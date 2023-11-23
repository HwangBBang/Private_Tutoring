# n = int(input())
# arr = [0]*n

# for i in range(n):
#     arr[i] = list(map(int, input().split()))
# r1, c1 = map(int, input().split())
# r2, c2 = map(int, input().split())

# res = 0
# for i in range(r1-1, r2):
#     for j in range(c1-1, c2):
#         res += arr[i][j]
# print(res)
# n = int(input())


# n = int(input())
# arr = [0]*n
# for i in range(n):
#     arr[i] = list(map(int, input().split()))

# arr = [0, 12, 3, 34, 5]
# for i, a in enumerate(arr):
#     print(i, a)
# print(arr)
# # 2
# # 3

# ```py

# ```

# ?
# ________________________________
# num1 = int(input()) # 472
# num2 = int(input()) # "385"

# f = num2//100
# s = (num2//10)%10
# t = num2%10

# for a in range(2,-1,-1):
#     print((num1 * int(num2[a])))

# print(num1*int(num2))

# 472 * 3
# 472 * 8
# 472 * 5

# fake = 0
# fun = 1
# fun1 = 1
# for i in range(3):
#     for j in range(i):
#         fun *= 10
#     for k in range(i+1):
#         fun1 *= 10
#     print(fun, fun1, sep="\n")
#     res = 0
#     print((num2//fun)-(num2//fun1))
#     print(res)
#     fake = res
#     res = 0
#     fun, fun1 = 1, 1
# _______________________________

# print('|\_/|',"|q p| /}",'( 0 )"""\',sep="\n")
# print(f'|"^"` |',"||_/=\__|")

# print('|\_/|')
# print("|q p| /}")
# print('( 0 )\"\"\"|"^"` |')
# print("||_/=\__|")

# print('''|\_/|
# |q p| /}
# ( 0 )"""\
# |"^"` |
# ||_/=\\__|''')
# print("""|\_/|
# |q p| /}
# ( 0 )\"\"\"\
# |"^"` |
# ||_/=\\__|""")
# _________________________
# hour, m = map(int, input().split(" "))
# m -= 45
# if m < 0:
#     m += 60
#     hour -= 1
# if hour < 0:
#     hour += 24
# print(hour, m)
# _____________
# M,N=map(int,input().split())
# cnt=0
# cnt1=0
# for i in range(M,N+1):
#     for j in range(1,i+1):
#         if i%j==0:
#             cnt+=1
#     if cnt==2:
#         cnt1+=i
# if cnt1>=1:
#     print(cnt1,,sep="\n")
# else:
#     print("-1")


# 다중 입력
# a, b = map(int, input().split())
# # 배열
# a, b = map(int, input().split())
print((type([1])))


a = list(map(int, input().split()))
print(a)
