s = int(input())
e = int(input())
w = int(input())

def calculateTemp(s):
	c = int((s - 32) / 1.8)
	print(f"{s} \t {c}")

while s < e:
	calculateTemp(s)
	s += w

n = int(input())

for i in range(n):
	for k in range(n - i - 1):
		print(' ', end = '')
	for j in range(i + 1):
		print(j + i + 1, end = '')
	print()

for i in range(1, n + 1):
	for k in range(n - i):
		print(' ', end = '')
	for j in range(2 * i - 1):
		print('*', end = '')
	print()


