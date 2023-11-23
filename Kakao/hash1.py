from collections import Counter, defaultdict


def solution(phone_book):
    answer = True
    d = defaultdict(int)
    for idx, i in enumerate(phone_book):
        d[i] += idx


# 해시를 돌면서 해당 값의 벨류와 조사하고자하는 벨류가 다를때
    for p in phone_book:
        a = ''
        for i in p:
            a += i
            if i in d and a != p:
                return False
    return answer


print(solution(phone_book=["119", "97674223", "1195524421"]))
print(solution(phone_book=["123", "456", "789"]))

# phone_book = ["119", "97674223", "1195524421"]

# print(phone_book[0] in phone_book[-1])
