# # 2. # 90
# # a = int(input())
# # b = int(input())

# # d = a*(b % 10)  # 1의자리
# # e = a*(((b % 100)//10))  # 10의자리
# # f = a*((b//100))  # 100의자리
# # g = d+e*10+f*100
# # print(d, e, f, g, sep="\n")

# # # 3. # 100
# # print("|\_/|")
# # print("|q p| /}")
# # print('''( 0 )"""\ ''')
# # print('''|"^"` |''')
# # print('''||_/=\\__|''')


# # # 4. 90
# # H, M = map(int, input().split())
# # if (M-45) < 0:
# #     M = (M-45)+60
# #     H = H-1
# #     if H <= 0:
# #         H += 24
# #         print(H, M, sep=" ")
# #     else:
# #         print(H, M, sep=" ")
# # else:
# #     print(H, M-45, sep=" ")

# # # 5.
# def isPrime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False  # 소수아니야
#     return True  # 소수야


# res_1 = 0

# M, N = map(int, input().split())
# for i in range(M, N+1):  # i 소수니?
#     if isPrime(i):
#         res_1 += i
# print(res_1)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# # # # ???
# # # 5
# # # 2, 3, 5, 7, 11
# # # cnt = 0
# # # num = 0

# # # def prime_Number(a):
# # #     for i in range(2, a):
# # #         if a % i == 0:
# # #             return (1) # 소수가 아니다.
# # #
# # #     return (0) # 소수다

# # # M = int(input())
# # # N = int(input())
# # # for i in range(M, N+1):
# # #     for j in range(2, i):
# # #         if i % j == 0:
# # #             pass
# # #         else:
# # #             prime_Number(i)
# # #             if prime_Number == 1:
# # #                 cnt += i
# # # print(cnt)

# # def isPrime(k):
# #     for i in range(2, k):
# #         if k % i == 0:
# #             # k 소수 아님
# #             return False
# #     # k 소수
# #     return True

# # # 소수의 합과 최소값.


# # M = int(input())
# # N = int(input())

# # primes = []

# # for i in range(M, N+1):  # i? 가 소수인지 판단해야해 .
# #     if isPrime(i):
# #         primes.append(i)

# # print(sum(primes), min(primes))


# # # 배열 , list

# # # arr = []
# # # arr = list()

# # # 큰 상자야. 끝이 없어. 니가 넣는 만큼 크기가 커져.
# # arr = []  # 주머니(배열)의 크기. ? 0
# # print(len(arr))
# # arr = [1]  # 주머니(배열)의 크기. ? 1
# # print(len(arr))
# # arr = [1, 3]  # 주머니(배열)의 크기. ? 2
# # print(len(arr))
# # # 배열의 크기를 어캐 확인하죠? -> length : 길이

# # # 문자열은 문자로만 이뤄진 배열
# # s = "13124"
# # print(s[3], s[-2])

# # # index  0    1    2    3    4
# # # index  -5  -4   -3   -2    -1


# arr1 = [1, 3, -1, 5, 4]
# print(arr1)

# # len : 요소들의 갯수
# # sum : 총합.
# # min : 최소값
# # max : 최대값

# print(f'sum : {sum(arr1)}')
# print(f'min : {min(arr1)}')
# print(f'max : {max(arr1)}')
# print(f'avg : {sum(arr1)/len(arr1)}')

# # append , pop
# # append : 추가하다
# # pop : 제거하다
# arr1.append('시훈')
# print(arr1)
# arr1.append('병훈')
# print(arr1)
# arr1.pop(4)
# print(arr1)

# 주소 , 구조체 , 포인터 , 타입 ,
# 자료구조. DS type
# data를 어떻게 저장해두는지
# list()  # 배열 !!!!

# a = [1, 1, 2, 1, 1, 2, 1, 1, 1, 2]
# print(a)
# print(len(a))
# a = set(a)
# print(*a)
# # print(len(a))

# visited = []
# # 효율성.... big-O 이코드효율성 어떻니???? 수치화
# for i in a:
#     if a in visited:
#         continue
#     else:
#         print(i, end=" ")
#         visited.append(i)


# set 집합 중복을 허용하지않아.

# dic1 = {
#     1: 0,
#     2: 1}  # 해시 == 전화번호 부 .
# print(dic1[1])
# 1 <-----------> 0
# 2 <-----------> 1
# '시훈' <-----------> '010-1111-1111',
# '병훈' <-----------> '010-9542-3738',

# 메서드 , 함수
# 함수
# 너소수니?()
# 너짝수니?()
# over200()

# 메서드
# obj.moreFast()
# 얼굴.예쁜()
# 코.예쁜()
# 꽃.예쁜()
# 배열.추가합니다.
# 배열.제거합니다.
# 배열.append()
# 배열.pop()


# 변수 ,타입, 내장함수 ,조건문 <-> 함수 <-> 반복문 <-> 배열
# 언어는 도구 ,언제든지 갈아 끼울 수 있어요
# 논리는 갈아끼울 수 없어요
# 반복문 <-> 배열

# arr = [i for i in range(1, 99999) if i % 2]
# print(arr)


for i in range(10):  # 세로
    for j in range(10-i):  # 가로
        print((i, j), end=" ")
    print()
for i in range(10):  # 세로
    for j in range(i+1):  # 가로
        print((i, j), end=" ")
    print()

# for i in arr:
#     print(i, end=" ")
# print()
# for i in range(1, 9):
#     print(i,  end=" ")
