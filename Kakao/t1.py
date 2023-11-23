# str = 'aBcDeFg'

# res = []
# for i, s in enumerate(str):
#     if chr(65) <= s and s <= chr(65+25):
#         res.append(chr(ord(s)+32))
#     elif chr(97) <= s and s <= chr(97+25):
#         res.append(chr(ord(s)-32))

# print(*res, sep="")


# 문자열 메서드
# swapcase()로 대소문자 변경
# isupper() 대문자니? 리턴 boolen
# islower() 소문자니? 리턴 boolen
# upper() 대문자로. 리턴
# lower() 소문자로. 리턴

# 아스키 관련 func
# chr ㅣ int to ascii
# ord ㅣ ascii to int


# 배열앞에 * 을 붙힘으로 unpacking

# !@#$%^&*('"<>?:;
# !@#$%^&*(\'"<>?:;
# 특수 문자가 많을 때는 문자열 앞에 r을 붙인다.

# def solution(my_string, overwrite_string, s):
#     answer = ''
#     m = len(my_string)
#     o = len(overwrite_string)

#     answer = my_string[:s] + overwrite_string + my_string[o+s:]
#     # print(answer)
#     return answer


# solution("Program29b8UYP", "merS123", 7)

# import collections


# def solution(participant, completion):
#     answer = ''
#     # for c in completion:
#     #     participant.remove(c)
#     # answer = participant[0]

#     print(*list((collections.Counter(participant) -
#           collections.Counter(completion)).keys()))

#     return answer


# solution(["mislav", "stanko", "mislav", "ana"],	["stanko", "ana", "mislav"])


# collections 클래스의 Counter 객체
# Counter 객체는 편하고 빠르게 개수를 셀 수 있도록 지원하는 객체이다.


# from collections import Counter
