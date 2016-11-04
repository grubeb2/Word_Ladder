import networkx as nx
import time
start_time = time.time()

def editDistance(a, b):
	if len(a) != len(b):
		return -1
	dist = 0
	for k in range(len(a)):
		if a[k] != b[k]:
			dist = dist + 1
	return dist

def editDistance2(a,b):
	if len(a) != len(b):
		return -1
	A = list(a)
	B = list(b)
	
	if cmp(A, B) == 0:
		return 0
	i = 0
	j = 0
	while (i <len(A)):
		j = 0
		while (j < len(B)):
			if A[i] == B[j]:
				A.pop(i)
				B.pop(j)
				i-=1
				break
			j+=1
		i+=1
	return len(A)


def makeGraph():
	input = open('words.txt', 'r')
	wordsList = []
	g = nx.Graph(name='words')
	for line in input.readlines():
		if line.startswith('*'):
			continue;
		line = line.translate(None, '`1234567890-=~!@#$%^&*()_+[]\;'+"',./{}|:"+'"<>?')
		line = line.lower()
		line = line.strip()
		wordsList.append(line)
	g.add_nodes_from(wordsList)
	for k in range(len(wordsList)):
		i = wordsList[k]
		for l in range(k+1, len(wordsList)):
			j = wordsList[l]
			if editDistance2(i, j) == 1:
				g.add_edge(i, j)
	return g



if __name__ == '__main__':
	from networkx import *
	
	g = makeGraph()
	print "Loaded words_dat.txt containing 5757 five-letter English words."
	print "Two words are connected if they differ in one letter."
	print "graph has %d nodes with %d edges" % (number_of_nodes(g),number_of_edges(g))

	sp=shortest_path(g, 'chaos', 'order')
	print "shortest path between 'chaos' and 'order' is:\n", sp

	sp=shortest_path(g, 'nodes', 'graph')
	print "shortest path between 'nodes' and 'graph' is:\n", sp

	sp=shortest_path(g, 'moron', 'smart')
	print "shortest path between 'moron' and 'smart' is:\n", sp

	sp=shortest_path(g, 'pound', 'marks')
	print "shortest path between 'pound' and 'marks' is:\n", sp
	
	print number_connected_components(g),"connected components"
	
	print "--- %s seconds ---" % (time.time() - start_time)

