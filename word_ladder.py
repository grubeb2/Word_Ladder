import networkx as nx


def makeGraph():
	file inputWords = open('words.txt', 'r')
	wordsList = set()
	#symbols = '`1234567890-=~!@#$%^&*()_+[]\;'+"',./{}|:"+'"<>?'
	for line in inputWords.readlines():
		if line.startswith('*'):
			continue;
		line = line.translate(None, '`1234567890-=~!@#$%^&*()_+[]\;'+"',./{}|:"+'"<>?')
		line = line.lower()
		wordsList.add(line)


if __name__ == '__main__':
