
import math
# c 언어 <- 근본, OS , System infra , DBMS(mysql, postgreSQL, Oracle)
# 컴파일 언어.

# C : SW 개발 어려움.
# overhead : 기회비용 , 쓸데없는 낭비 , (한정된 자원) ,즉 오버헤드를 줄여야해.
# C++ (OOP) <- 게임, 자동차, 그래픽, 항공
# C# (OOP) <- 게임 + Unity


# OOP : 객체지향언어  Class, Object, Instance, method, member variable
# arr = list(1,2,3,5)
# arr.remove(1)
# Class -> Object (Instance)
# 사투리 라는 메서드
# 서울놈을 없이
# 대한민국 -> 부산 , 서울 -> private 마포 , public 강동

# python <- AI, 크롤링 , 데이터 분석
# 인터프리트 언어 (스크립트 언어)

# JAVA <- 90% (백 엔드)


# Memory  : RAM (주 기억 장치)
# Storage :  SSD ,HDD (보조 기억장치 )

x = 27  # 선언 + 초기화

# [__________________________________________________________]
# [________________|X______|_________________________________]

# [________________X=27_______________________________________]

# [________________X=27_______________________________________]


# a,b,c,d,e,f ... a1,a2
# list  , []

# "1 2 3 4 2 1 0 3" -> input()
# "1 2 3 4 2 1 0 3" -> input().split()
# "1","2","3","4","2","1","0","3"-> map(int,input().split())
# 1,2,3,4,2,1,0,3 -> map(int,input().split())
# [1,2,3,4,2,1,0,3] -> list(map(int,input().split()))

arr = [1, 2, 3, 4, 2, 1, 0, 3]
# arr.sort()
# arr.reverse()
# arr.pop()
# arr.clear()

# res = sum(arr)
# res = len(arr)
# res = max(arr)
# res = min(arr)

# print(res)


# arr.reverse()


print(arr)
print(*arr, sep="")
# for e in arr:
#     print()

# int , float ,str
# ------------------
# list

# 문자(배)열.

a = input()
a = list(a)
a.reverse()

print(a)


a = input()

for i in range(len(a)-1, -1, -1):
    print(i, sep="")
