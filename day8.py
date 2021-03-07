# s = int(input())
# e = int(input())
# w = int(input())

# def calculateTemp(s):
# 	c = int((s - 32) / 1.8)
# 	print(f"{s} \t {c}")

# while s < e:
# 	calculateTemp(s)
# 	s += w

# n = int(input())

# for i in range(n):
# 	for k in range(n - i - 1):
# 		print(' ', end = '')
# 	for j in range(i + 1):
# 		print(j + i + 1, end = '')
# 	print()

# for i in range(1, n + 1):
# 	for k in range(n - i):
# 		print(' ', end = '')
# 	for j in range(2 * i - 1):
# 		print('*', end = '')
# 	print()


# Ceaser Cipher

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def find_pos(char):
	pos_of_char = 0
	for i in alphabet:
		if i == char:
			return pos_of_char
		else:
			pos_of_char += 1
	return pos_of_char

def encode(word, pos):
	cur_pos = 0
	encoded_list = []
	encoded_word = ''
	for i in word:
		new_pos = (find_pos(i) + pos) % len(alphabet)
		encoded_list.append(alphabet[new_pos])
	for i in encoded_list:
		encoded_word += i
	return encoded_word

def decode(word, pos):
	decoded_list = []
	decoded_word = ''
	cur_pos = 0
	for i in word:
		new_pos = (find_pos(i) - pos) % len(alphabet)
		decoded_list.append(alphabet[new_pos])
	for i in decoded_list:
		decoded_word += i
	return decoded_word

word = input("Enter a word: ")
pos = int(input("Enter encoding pos: "))
encoded_word = encode(word, pos)
decoded_word = decode(encoded_word, pos)
print(encoded_word)
print(decoded_word)