
a = 1.12345678

print('%.3f' % a)
print('%3.f' % a)
# def add1(num):
#     return num+1

# 1.123
#   1
# split('-')
# '1-2 3-4'
# split('p')
# 'dpoap3q13pi12 5w:hjpo fd1:"25+qrf'
# 'd', 'oa', '3q13', 'i12 5w:hj', 'o fd1:"25+qrf'

# split('/')
# 'dpo/ap3q13  pi  /./12 5w/:hj/po fd1':"25+/qr/f'
'dpo', 'ap3q13  pi  ', '.', '12 5w', ':hj', 'po fd131:"25+', 'qr', 'f'


'1', '2 3', '4'
a, b, c, d = '1', '2', '3', '4'
a, b, c, d = map(int, ['1', '2', '3', '4'])
a, b, c, d = map(int, '1', '231', '32', '2')

map(int, input().split())
print(type(a), b, c, d)


# a = int(a); b = int(b); c = int(c); d = int(d);

# a += 1
# b += 1


# split : 입력받은것을 분리시키는 것
front, second = map(int, input().split('-'))
