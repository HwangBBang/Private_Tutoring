
# # iteration : 반복
# # iterate : 반복하다
# # print(list(range(1, 5)))
# # enumerate 낱낱이 세다.

# # 초기화 =
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # empty list
# for _ in range(2):
#     a += ([i for i in range(1, 11)])  # list comprehension
# print(a)
# # print(a[1])  # 2 , 0부터 카운팅하니까.
# print(f'length: {len(a)}')  # len() : length : 길이


# for i in a:
#     print(i)


# # for i in range():
# for e, i in enumerate(a):
#     print(e, i)
#     print(e, a[e])

# # nest : 둥지
# # Nested if
# # if
# #     if
# #     elif
# #     elif
# # Nested list

# b = [[1], [2, 3], 6, 1, 1, 1, 1, 1, [3, 1, 4]]
# print(f'b\'length: {len(b)}')  # len() : length : 길이
# print(b[-1])
# print()

# # list append 덧붙이다

# print(f'length: {len(a)}')
# a.append('지민')
# print(a)
# print(f'length: {len(a)}')
# a.pop()
# # list pop ,remove
# # print(f'length: {len(a)}')
# # a.pop(4) # index
# # print(a)
# # print(f'length: {len(a)}')

# print(f'length: {len(a)}')
# a.remove(4)
# print(a)
# print(f'length: {len(a)}')

# # sort
# print(f'length: {len(a)}')

# a.sort(reverse=True)
# print(a)

# a = sorted(a, reverse=False)
# print(a)
# print(f'length: {len(a)}')

# # list slicing

# print(a[15:])
# print(a[:15])
# print(a[14:17])

# # sum
# print(sum(a[14:17]))

list_A = list(map(int, input().split()))

for i in range(9, -1, -1):
    print(list_A[i])

print(list_A)
print(sum(list_A))
