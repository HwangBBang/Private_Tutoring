
# i가 (M~N 까지) 소수 인지 확인하고 싶어해
# j 는 각각 i 가 소수인지 확인하기위해 나누는 수 .
# cnt 각각의 i가 소수인진 판별하기위해서  cnt

# 소수를 판별 -> 소수들의 합 ,소수들의 최솟값

# 예를 들어 (X)

def isPrime(k):  # k가 소수인지 아닌지 판단하는 함수
    cnt = 0  # 약수의 갯수를 카운팅
    for i in range(1, k+1):  # 2~n-1
        if k % i == 0:
            cnt += 1
    if cnt == 2:
        return True
    else:
        return False


# def isPrime(k): # k가 소수인지 아닌지 판단하는 함수
#     for i in range(2, k):  # 2~n-1
#         if k % i == 0:
#             return False
#     return True

M = int(input())
N = int(input())
arr = []
for i in range(M, N+1):
    # i 소수인지 궁금해
    if isPrime(i):
        arr.append(i)

if len(arr) != 0:  # length : 길이
    print(sum(arr))
    print(arr[0])
else:
    print(-1)
