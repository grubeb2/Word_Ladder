import networkx as nx


def makeGraph():
	file inputWords = open('words.txt', 'r')
	wordsList = set()
	for line in inputWords.readlines():
		if line.startswith('*'):
			continue;
		line = line.translate(None, '`1234567890-=~!@#$%^&*()_+[]\;'+"',./{}|:"+'"<>?')
		line = line.lower()
		wordsList.add(line)
	G = Graph(name='words')
	G.add_nodes_from(wordsList)
		



if __name__ == '__main__':
