
# _ _ _
# 1~9 구성된 세자리 숫자.
# 123, 111, 999 -> 전체 9 * 9 * 9 = 729 가지

# 적어도 하나는 1을 포함하는 경우 는 217

# -> 반대는 1을 하나도 포함하지않는 경우
# 2~9 2~9 2~9
# 222 -> 8*8*8 = 512

# 729 - 512 = 217

# 원하는거 ! : 사건

# 원하는거의 반대 ! : 여사건

# 전체 - 원하는거의 반대 ! = 원하는거 !

# 전체 - 여사건 = 사건 !

# if
# 만약에 연휴라면 -> 수업하지말아줘
# 만약에 생일이라면 -> 수업하지말아줘


# a 를 입력받아
# 1~a 까지 확인해주세요. -> 뭘 확인할까?
# 뭘 확인하나면, 모두 조건을 만족 하지 않는 경우 -> 무슨 조건인데?
# 조건이 뭐냐면,

# 짝수 and 4배수가아님
# 8로 나눈 몫이 짝수
# 7로 나눈 나머지가 4보다 작은 수


# 분할(나눠서) 정복(마스터 해버려!)

# 문제 = 문제 1 + 문제 2 + 문제 3

# 모든 공부는 내 자신의 언어로 바꿔봐!


# if - elif - else
# 조건 1 -> 버려!~(continue)

# 조건 2 -> 버려!~(continue)

# 조건 3 -> 버려!~(continue)

# 여기까지온다면 세 조건 모두 만족하지 않는거야


# i//8 : 어떤수를 8로 나눈 몫

# (i//8) 짝수니?
# (i//8) % 2 == 0

# w 짝수니?
# w % 2 == 0

# 어떤수를 8로 나눈 몫이 짝수


# continue 문 실력체크 다시풀기!

# n == 6
# i를 올려가면서 생각해봐


# n = int(input())

# div_cnt = 0
# i = 1

# while True:
#     n //= i
#     div_cnt += 1

#     if n <= 1:
#         print(div_cnt)
#         break
#     i += 1


# 무한 루프 ..


# flag = True
# i = 1
# while flag:
#     print(i, end=" ")
#     i *= 2


flag = True
# 어떤 수를 입력을 받건 0 이 포함 되어 있다면. 멈춰줘
while flag:
    # a = "103192748912745902379050915" # input()
    a = input()

    for elem in a:
        if elem == "0":
            flag = False
            break

    if flag == True:
        print(a)
