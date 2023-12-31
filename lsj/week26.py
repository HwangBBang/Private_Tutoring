# 조건문 if
# 특정 조건에 따라 코드를 실행 : 조건문
condition = True

if condition:
    # 실행
    print()
else:  # not, 여사건.
    # codition 이 True 가 아닐 때 실행되는 곳.
    print()

# elif else + if

name = input()
h = input()
if name == "kim":
    print('kim')
if name == "lee":
    print('lee')

# -----------가독성-----------

if name == "kim":
    print('kim')
elif name == "lee":
    print('lee')

# nest : 둥지
# nested : 둥지화(된) == 중첩된


if name == "kim" and h >= 180:
    print('kim')

if name == "kim":
    if h >= 180:
        print('kim')


if name == "kim" or name == "lee":
    print('hi')

if name == "kim":
    print('hi')
if name == "lee":
    print('hi')

# -----다중조건-------

# A,B,C,D,F
grade = input()
if grade == "A":
    print("A")
elif grade == "B":
    print("B")
elif grade == "C":
    print("C")
elif grade == "D":
    print("D")
elif grade == "F":
    print("F")
else:
    print("Not vaild grade")
