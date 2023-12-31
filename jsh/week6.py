# # 조건문 (분(나눌)기)
# # -> if elif else + and or

# # if A and B
# # if A
# #   if B

# # if A or B

# # if A
# # if B


# # 반복문 (for , while)
# # for 변수 in range(시작포인트 , 종료바로다음포인트 , 도달하는방법)  : 횟수가 명확할때.
# # for i in range(0,10,1): #10 번.!

# # while : 횟수가 명확하지않을때,
# flag = True

# while flag:
#     n = int(input("숫자를 입력하세요 : "))
#     if n == 0:
#         # flag = False
#         # continue
#         break
#     print(f"입력한 숫자 :{n} / 반복문이 가동중입니다. ")

# # break : 깨부시다

# # continue : 다음으로,, 다음스텝으로 ,,


# # while 문 작성
# # 반복해서 입력을 받아요
# # 입력받는 문구는 : 정수를 입력하세요

# # 1입력받았을때 ~게임시작~ 이라는 문구출력
# # 2입력받았을때 ~게임옵션~ 이라는 문구출력
# # 3입력받았을때 ~게임중지~ 이라는 문구출력
# # 4입력받았을때 ~게임종료~ 이라는 문구출력
# # -1입력받았을때 ~강제종료~ 이라는 문구출력
# # break


# 매반복문 끝에는 ~게임 실행중~ 이라는 문구출력
flag = True
num = 10
while flag:
    if num == 26:
        flag = False
    print(num, end=" ")
    num += 1
