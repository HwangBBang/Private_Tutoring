from collections import Counter, defaultdict


# def solution(genres, plays):
#     answer = []
# #    장르별로 종합.
#     union = Counter()
#     playlist = list()

#     for ip, (g, p) in enumerate(zip(genres, plays)):
#         union.update({g: p})
#         playlist.append([g, p, ip])
#     union = union.most_common()

#     order = {i[0]: idx for idx, i in enumerate(union)}

#     playlist.sort(key=lambda x: (order[x[0]], -x[1], x[2]))
#     # answer = [play[2] for play in playlist] /  2번까지 조건이없다면. 이거

#     group = defaultdict(list)
#     for play in playlist:
#         group[play[0]].append(play)

#     for genre in group:
#         answer.extend([s[2] for s in group[genre][:2]])
#     # print(answer)
#     return answer


# solution(["classic", "pop", "classic", "classic", "pop"],
#          [500, 600, 150, 800, 2500])
# solution(["classic", "classic", "classic"],
#          [150, 800, 2500])
# solution(["classic",
#           'classic',
#           "classic",
#           "zazzi",
#           "kim",
#           "kpop",
#           'zazzi',
#           'zazzi'
#           ],
#          [4400,
#           4400,
#           4400,
#           4400,
#           150,
#           800,
#           2500,
#           4400,
#           4400])


# # genre 별로 그룹화 한 후  그 값의 길이의 한계를 2로 정해주자 .


# arr = []
# print(arr[:2])
# arr = [1]
# print(arr[:2])
# arr = [1, 2]
# print(arr[:2])
# arr = [1, 2, 3]
# print(arr[:2])


# defaultdict 은 dict 의 하위 클래스이다.
# 존재하지않는 키에 대해 기본값을 제공하는 특수 dict 이다.

# defaultdict 을 생성할 때 기본값을 생성하는 함수를 전달해야해 !
a1 = defaultdict(list)  # 리스트 기반 새로운 키가 정해지면, 빈리스트를 벨류 값을 세팅한다.
a1['a'].append(1)
a1['a'].append(2)
a1['b'].append(4)

a2 = defaultdict(int)  # int 기반
a2['a']
a2['b']
a2['c'] += 1

a3 = defaultdict(set)  # 셋 기반
# a2{'a'}.add(1)
# a2{'a'}.add(1)
# a2{'b'}.add(1)
# a2{'b'}.add(2)
print(a1, *a2, a3, sep='\n')
