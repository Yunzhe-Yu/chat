
# Read function
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

# Convert function
def convert(lines):
	person = None # none 
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_pics = 0
	viki_pics = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count +=1
			elif s[2] == '圖片':
				allen_pics += 1
			else:
				for msg in s[2:]:
					allen_word_count += len(msg)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_pics += 1
			else:
				for msg in s[2:]:
					viki_word_count += len(msg)
	print('The total word number of Allen is', allen_word_count, 'and he has', allen_sticker_count, 'stickers and', allen_pics, 'pictures!')
	print('The total word number of Viki is', viki_word_count, 'and he has', viki_sticker_count, 'stickers and', viki_pics, 'pictures!')
		#print(s)

# Write function
def write_file(filename, lines):
	with open(filename, 'w', encoding = 'utf-8') as f:
		for line in lines:
			f.write(line + '\n')

# Main function
def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)
	# write_file('output.txt', lines)

main()

# n = [0, 1, 2, 3, 4, 5]
# n[:3] = [0, 1, 2]
# n[2:4] = [2, 3]
# n[-2:] = [4, 5] 