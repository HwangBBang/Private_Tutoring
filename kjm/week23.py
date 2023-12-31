# if A :
# #    -> A[ ] B[ ] C[ ] D[ ] E[ ] F[ ] G[ ]
#     if B :
#     #   -> A[ ] B[ ] C[ ] D[ ] E[ ] F[ ] G[ ]
#         if not C :
#         # -> A[ ] B[ ] C[ ] D[ ] E[ ] F[ ] G[ ]
#         elif not G and not F:
#         # -> A[ ] B[ ] C[ ] D[ ] E[ ] F[ ] G[ ]
#         else :
#         #  -> A[ ] B[ ] C[ ] D[ ] E[ ] F[ ] G[ ]
#     elif D and E:
#     #   -> A[ ] B[ ] C[ ] D[ ] E[ ] F[ ] G[ ]
#     else :
#     #   -> A[ ] B[ ] C[ ] D[ ]  E[ ] F[ ] G[ ]
# else :
# #    -> A[ ] B[ ] C[ ] D[ ] E[ ] F[ ] G[ ]
#      if F :
#      #  -> A[ ] B[ ] C[ ] D[ ] E[ ] F[ ] G[ ]
#      if G :
#      #  -> A[ ] B[ ] C[ ] D[ ] E[ ] F[ ] G[ ]


# 중첩 반복문

for i in range(5):
    for l in range(5-i):
        print(" ", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()

for i in range(5):
    for j in range(5-i):
        print("*", end=" ")
    print()

# 문제를 풀때는 분석,,,
# 원칙1.  갯수를 파악한다. (행 단위로) (우리 찍어 낼때 ->)
# 원칙2.  내림 오름 차순을 파악한다.
# 원칙3.  세로에 대한 규칙 파악한다. (밖 for 문)
# 원칙4.  가로에 대한 규칙 파악한다. (안 for 문)

" "" ""*"
" ""*""*""*"
