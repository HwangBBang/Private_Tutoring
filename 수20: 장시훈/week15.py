# print(1,2,end = "\n",sep = "+") 내장 함수
# 1+2
# input() 내장 함수 , 리턴 타입 str ,형변환
# int(input())

# def change_num_9(num):
#     num = 9
#     return num

# if 조건문, 분기문

# -------------
# if 2배수:
#   code
# elif 3배수:
#   code
# else:
#   code
# -------------

# -------------
# if 2의배수:
#   code
# -------------
# -------------
# if 3의배수:
#   code
# -------------
# for ,while
# 반복문 제어 .

# code2를 3번 반복하게되면 더 이상 컨티뉴를 하지마!
# while 1:
#     code1 | (3)
#     code2 | (3) -> 조건을 바로 확인해줘 / continue
#     code3 | (1)
#     code4 | (1)
#     code5 | (1)
#     code6 | (1)
#     code7 | (1) -> 반복문을 끝내버리렴. / break

# for _ in range(10): -> 10 / 단순반복.
# for i in range(10): -> 10
# for _ in range(sp, ep ,d): -> 10
# for _ in range(sp = 0, ep ,d = 1): -> 10


# while True:
#     a, b, c = map(str, input().split())
#     # a, b, c = map(str, input().split())
#     a = int(a)
#     b = int(b)
#     s = a*b
#     print(s)
#     if c == "c":
#         break
while True:
    a, b, c = map(str, input().split())
    a = int(a)
    b = int(b)
    s = a*b
    print(s)
    if c == "c":
        break


# if a >= 20 and 30 > a:
#    pass
# else
