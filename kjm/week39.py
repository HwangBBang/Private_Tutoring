# # variable , initialize(set), data type
# # f-string , r-string ,escape squence \n \t \\ \'\"
# # such as print , input , split , options
# # what is function  & method?
# # if - else - elif / flow control
# # for , while
# # ------
# # Data Structure / data 어떻게 보관 할꺼야? : list

# # Big-O

# # Stack / FILO : First In Last Out
# # bot [000000000000000] top  -> OverHead
# # ----------------------
# # |1 2 3 4 5 6 7 8 9 0
# # ----------------------
# #  0123456
# #   000000000000000
# #  00000000000000
# # stack pop() : O(1)
# # stack append() : O(1)

# # stack pop(0) : O(n) (X)

# # Queue / FIFO : First In First Out
# # ----------------------
# # 1 2 3 4 5 6 7 8 9 0
# # ----------------------
# # 000000000000000
# # 00000000000000
# # queue popleft() : O(1)

# from collections import deque

# arr = []  # stack
# for i in range(5):
#     arr.append(i)
#     print(arr)
# arr.pop(0)
# print(arr)

# que = deque()
# for i in range(5):
#     que.append(i)
#     print(que)
# print(que)
# que.popleft()
# print(que)


# arr = [] *
# function
# 머리를 .

# 정리 시대.
# 정리.
# 문제를 정리.


arr = []
print(arr)

arr = [0]
print(arr)

arr = [[]]
print(arr)

arr2 = [1, 2, 3, 4]
print(arr)

arr = [elem**2 for elem in arr2 if elem > 2]  # 리스트 컴프리핸션 'list Comprehension'
print(arr)

arr = []
for elem in arr2:
    if elem > 2:
        arr.append(elem**2)
print(arr)

# -------------------------------
# print(type(arr))

# arr[0] = 1
# arr[-1] = 1
# print(arr)

# arr.append(1)  # 리스트에 1을 넣어준다.
# arr.remove()  # 리스트 -> 딕셔너리 (해시)
# arr.sort()  # 리스트의 원소들을 정렬 (오름차순)
# arr.reverse() # 리스트의 원소들을 꺼꾸로 만들기 O(n)
# arr.extend() # 리스트를 통째로 리스트에 붙일때.
arr = arr + [9, 9, 9, 9, 1]  # list(1)
# list = list + list(int)
print(arr)
# arr.insert()
# arr.clear() # O(n)
# print(arr.count(9)) # O(n)
# arr.index()
a = arr.pop()
# [9, 16, 9, 9, 9, 9, 1]

arr.append([1, 3, 2, 4])
print(arr)

print(arr[-1][1])


# python 리스트 메소드

# 3 2 5 6 1 4
# 4 1 6 5 2 3


# 흐름을 구조를 분석 -> 이런 행위 list 가장 큰놈을 찾는 행위 . ->  make function

# def fName(args): return max(args)


# clean code 함수는 1가지 일만해라.
