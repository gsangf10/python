# 구구단은 n단 ~ m단 중 홀수단만 1 ~ limit 까지 곱 중 짝수곱만 출력해주세요.

n = 4;
m = 19;
limit = 11;

'''  출력 예시

5 * 2 = 10
5 * 4 = 20
5 * 6 = 30
5 * 8 = 40
5 * 10 = 50

7 * 2 = 14
7 * 4 = 28
7 * 6 = 42
7 * 8 = 56
7 * 10 = 70
...
...
19 * 2 = 38
19 * 4 = 76

'''

i = n
while i <= m:
  j = 1
  while j <= limit:
    print("{} * {} = {}".format(i, j, i*j))
    j += 1
  print()
  i += 1
