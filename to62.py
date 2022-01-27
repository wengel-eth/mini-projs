base62 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
lib62 = [char for char in base62]
lib62[2]

def to62(num):
	if type(num) != type(5):
		return 'Not an integer'
	tempNum = num
	result = [0]
	while tempNum >= 62:
		tempNum -= 62
		try:
			for i in range(len(result)):
				if result[i] < 62:
					result[i] += 1
				else:
					continue
		except:
			result.append(0)

	result[len(result)-1] += tempNum
	return result

print(to62(3906))
