def romanToNum(x):
	l = len(x)
	num = 0
	flag = False
	dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
	priority = {"I": 1, "V": 2, "X": 3, "L": 4, "C": 5, "D": 6, "M": 7}

	if(l > 0):
		for i in range(0, l):
			if(flag):
				flag = False
			elif((i + 1 < l) and priority[x[i]] < priority[x[i+1]]):
				num = num + (dict[x[i+1]] - dict[x[i]])
				flag = True
			else:
				num = num + dict[x[i]]
		
	print("The number is: " + str(num))

if __name__ == "__main__":
        y = input("Enter a roman numeral: ")
        print(y)
        romanToNum(str(y))

