import random

Question_Ans = {
    '': [''],
    '': [''],
    '': [''],
    '': [''],
    '': [''],
    '': [''],
    '': [''],
    '': [''],
    '': [''],
    '': [''],
    '': [''],
}


Question = list(Question_Ans.keys())
random.shuffle(Question)
while Question:

    current_question = Question[0]
    print(f'\n{current_question}')
    print()

    user_answer = input("answer: ").strip().lower()

    if user_answer in Question_Ans[current_question]:
        print("Correct!")
        print(Question_Ans[current_question])

        Question.pop(0)
    else:
        print("Incorrect!")
        print(Question_Ans[current_question])

        Question.append(Question.pop(0))

    print("-----------------------------------------------------------------------")

n = int(input())

# 소수란 약수가 1과 자기자신만 있는수를 말한다(단 소수!=1)
cnt = 0  # O(1)

for i in range(2, n+1):  # O(n)
    cnt = 0
    for j in range(1, i+1):  # O(n)
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        print(i, end=" ")


# A ,B
# BIG-O 시간 복잡도  O(1) O(n) O(log n) O(n)

# n1 = 9999...999
# n2 = 9999...998


print()  # O(1)

for i in range(2, n+1):  # O(n)
    cnt = 0  # O(1)


for i in range(2, n+1):  # O(n^2)
    for i in range(2, n+1):  # O(n)
        cnt = 0  # O(1)


for i in range(2, n+1):  # O(n)
    cnt = 0  # O(1)
for i in range(2, n+1):  # O(n)
    cnt = 0  # O(1)

# O(n)

for i in range(2, n+1):  # O(n^3)
    for i in range(2, n+1):  # O(n^2)
        for i in range(2, n+1):  # O(n)
            cnt = 0  # O(1)
