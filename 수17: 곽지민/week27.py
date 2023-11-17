# 중첩 for 기호 순서좀 볼 수 있게 숫자를 뽑아 냈어.
# 배열 문자열 함수 메서드

# 함수
# 주어 동사 .
# input() 함수 입력해줘~

# 메서드
# 부사 -> 동사를 꾸며줘요
# 함수에게 의존한다~
# split() 나눠서
# a, b = "123+356".split("+")  # 배열을 나누다.
# print(a, b)

# map 배열의 모든 원소에게 규칙을 적용시켜!

# def addNumOne(num): return num+1

# e1, e2, e3 = map(addNumOne, [1, 2, 3])
# print(e1, e2, e3)


# 범위, 정도 알 때.

# for _ in range(10):

# for i in range(a,b):
cnt = 0
for i in range(10):
    for j in range(i*2):
        cnt += 1
print(cnt)
