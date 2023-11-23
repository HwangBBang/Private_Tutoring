
n = int(input())

# 1단계
# for i in range(n):
#     for j in range(n-i):
#         print(" ", end="")
#     for k in range(2*i+1):
#         print("A", end="")
#     print()

# 2단계
# for i in range(n):
#     for j in range(n-i):
#         print(" ", end="")
#     for k in range(2*i+1):
#         print("A", end="")
#     print()
# for i in range(n-1, 0, -1):
#     for j in range(n-i+1):
#         print(" ", end="")
#     for k in range(2*i-1):
#         print("A", end="")
#     print()


# 3단계
arr = [chr(c) for c in range(65, 91)]


def draw(k):
    # k는 홀수 -> @@@ A@@@ 꼴
    for p in range(k//2, 0, -1):
        print(arr[p], end="")
    for p in range(0, k//2+1):
        print(arr[p], end="")


for i in range(n-1):
    for j in range(n-i):
        print(" ", end="")
    # for k in range(2*i+1):
    #     print("A", end="")
    draw(2*i+1)
    print()
for i in range(n-1, -1, -1):
    for j in range(n-i):
        print(" ", end="")
    # for k in range(2*i-1):
    #     print("A", end="")
    draw(2*i+1)
    print()
