# 정수를 하나 입력받고
# 그 수가 짝수라면 1 홀수라면 0을 출력하세요

###########################################

# 한 줄 정수를 두개를 입력받고
# 모든수가 짝수라면 1 하나라도 홀수라면 0을 출력하세요

###########################################

# 한 줄 정수를 두개를 입력받고
# 두수의 합이 짝수라면 "합이 짝수" 그렇지 않다면 "합이 홀수"
# 두수의 곱이 홀수라면 "곱이 홀수" 그렇지 않다면 "곱이 짝수"
# 을 공백을 사이에 두고 출력하시오


###########################################

# if 영어
# elif 수학
# elif 체육
# elif 도덕
# -> 4개 중 하나만 결론이되고싶어
# 도덕

# if 영어 elif 수학
# -> 2개 중 하나만 결론이되고싶어
# 영어
# if 도덕 elif 체육
# -> 2개 중 하나만 결론이되고싶어
# 체육
###########################################


# print(인자1,인자2,... ,end ,sep)
a, b = 2, 2

c = a+b
d = a*b
# 합이 홀수 곱이 짝수

# 합이 짝수
# 곱이 짝수
if c % 2 == 0:
    print("합이 짝수")
else:
    print("합이 홀수", end=" ")
# ---------45-----------
if d % 2 == 1:
    print("곱이 흡수")
else:
    print("곱이 짝수")

#
# "합이 짝수 곱이 흡수\n"
# "합이 홀수 곱이 짝수\n"


#############
# if 거짓
#  code1 실행
# else
#  code2 실행

#############
# 한 줄씩 정수 두 개를 입력받고
# 각 수의 1의 자리수를 출력하시오
# ","으로 구분해서
# 단, 출력함수를 하나만 사용하시오

# print(1, 1, end=",")
# print(1,32,"325w34","5231`34",end="\n")
# print(1,322,"w1234","1312`34",end="\n")
################################
# 한 줄에 정수 두 개와 문자 하나를 입력받고
# 문자 가 "a","b","c" 중 하나라면
# 두정수의 합의 1의자리수를 출력

# 문자 가 "d","e" 중 하나라면
# 두정수의 곱의 1의자리수를 출력

# 위의 문자가 모두 아닌 경우
# 두정수의 합과 곱의 합 의 10의 자리수를
################################

# "1 3 a"
a, b, c = "1", "3", "a"
# input().split(" ") #
map(int, input().split(" "))
# map(함수, 인자1,인자2,인자3)
# 변수들과 함수를 묶어주는것!
# map(int, "1", "3", "a")
# a,b,c = int("1"), int("3"), int("a")

# 문자c가 "a","b","c" 중 하나라면
# if c == "a" or c == "b" or c == "c":
