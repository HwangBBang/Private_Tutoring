
# # 오름차순과 내림차순
# # for 1234
# #    for 1/ 2/ 3/ 4
# # *
# # **
# # ***
# # ****

# #    for 4/ 3/ 2/ 1
# # ****
# # ***
# # **
# # *

# # 규칙.
# # 홀수 짝수, 배수 , 섞여 있어.


# # 추상화(abstraction).
# # 중요한것만.
# # 복잡한 사람 얼굴 -> ㄱ- , >_< , -_-

# # 의미없는 내용 까지 기록X -> 관리가 너무어려
# # Class : class var class method

# # 다형성
# # def int_add( int + int )
# # def flaot_add( float + float )
# # def int_flaot_add( int + float )
# # def str_add( str + str )

# # -> def add()


# # initialize : 초기화
# # var : 변수
# # 왜? 변수에 값을 세팅해서 "재사용"하려고.
# # 변수에 이름을 불러줘서 "재사용"
# # [주소 영역] = [데이터 영역]

# # sh = 0x1e3f12aa234
# # 0x1e3f12aa234 = 'a'

# # sh = 'a'

# # 기본 데이터 타입
# # 숫자 : int , float
# # 문자 : str
# # 논리 : bool

# # 3.0 | '.' floating point
# # str "" , '' ,"""""", ''''''
# # escape seq : '\n','\t','\\', '\'','\"'
# print('d\\a\'d\nd\"a\tda')

# # f-string : 문자열에 변수 사용
# sh = "캡슐화"
# print(f'시훈이나이 : {sh}')

# # r-string : 이스케이프 시퀀스
# print(r'd\\a\'d\nd\"a\tda')

# # str == list

# # == , != , <= , <
# # and : & , or : |
# # print(1 | 0)

# # flow control
# # if - elif - else

# # 상위 계층

# # if b :
# #     if a:
# #     else:
# # elif v :
# #     if dad:

# # for , while
# arr = [1, 2, 3]
# sh = range(0, 5)  # [0, 1, 2, 3, 4]
# # for i in range():
# print(*arr)
# print(*sh)

# for i in arr:
#     print(i)
# for i in sh:
#     print(i)

# # (실행전) 결정난다면, 반복이나 범위의 정도를 알고 있다면 -> for
# #
# # 런타임(실행중)시 결정난다면, 실행중에 어떠한 이벤트로 반복이 멈추는 -> while

# # 프로그램을 만들었어 q 를 입력받는다면 종료


n = int(input())


# j < i

# 정사각형.
# 어떤 조건일 때는 "*" -> " "

# (1,1)(1,2)
#      (2,2)
#      j=3
# * * * * i = 0
# *     *
# * *   *
# * * * *
# for i in range(n):
#     for j in range(n):
#         if i > j or j == n-1 or i == 0:
#             print('*', end=" ")
#         else:
#             print(' ', end=" ")

#     print()

# (1,1)(1,2)(1,3)
#      (2,2)(2,3)
#           (3,3)
# * * * * *
# *       *
# * *     *
# * * *   *
# * * * * *
for i in range(n):
    for j in range(n):
        if i == 0:
            print('*', end=" ")
        else:
            if j % 2 == 1 and i <= j:
                print('*', end=" ")
            else:
                print(' ', end=" ")

    print()
# 0 1 2 3 4
# * * * * *
#   * * * *
#     * * *
#       * *
#         *
for i in range(n):
    for j in range(n):
        if (j % 2 == 1 and i <= j) or i == 0:
            print('*', end=" ")
        else:
            print(' ', end=" ")
    print()


#     *   *
#     *   *
#         *
#         *

# * * * * *
#     *   *
#     *   *
#         *
#         *
