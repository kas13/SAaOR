"""Требуется найти наксимальный путь из s в t """
from queue import Queue

Q = Queue()
#G = [[[1,2], [2,3]],[[3,13],[0, 2],[2, 0]],[[3,6],[0,3],[1, 0],[4,7]],[[2, 6],[1, 13],[4,12]],[[3,12], [2, 7]]] #graph
#G = [[[1,2], [2,3]],[[3,9],],[[3,6],],[[2, 6],[1, 9]]] #graph
G = [[[1,5], [2,2]],[[2,3],[3,3]],[[4, 5]],[[2,4],[4,7]],[[]]]
D = [] # lenghts
U = [] # marks
P = dict() # path to node



def main():
	n = 5
	global D, U
	D = [0] * n
	U = [False] * n
	#n = int(input("input n node : "))
	find_max_path(n, 0)
	# for i in range(int(n)):
	# 	m = input("n({}) input m how many nodes from this node: ".format(i))
	# 	G.append([])
	# 	for j in range(int(m)):
	# 		v = int(input("input v node : "))
	# 		l = int(input("input l lenght : "))
	# 		G[i].append([v,l])
	# for i in range(int(n)):
	# 	print("node {}".format(i))
	# 	for j in G[i]:
	# 		print("  node {}, lenght {} ".format(j[0],j[1]))

def find_max_path(n, s):
	"""from s to t """
	Q.put(G[s])
	P[s] = "0"
	while Q.empty() is False:
		node = Q.get()
		cur_node = G.index(node)
		U[cur_node] = True
		if node != [[]]:
			for j in node:
				to = j[0] #node number
				l = j[1] #len
				#print("to {}, cur {}".format(to, cur_node))
				if D[cur_node] + l > D[to]:
					#print("Cur_n {}, cur + l {}, D[to] {}, to {}, U[to] {}".format(cur_node, D[cur_node] + l, D[to], to, U[to]))
					D[to] = D[cur_node] + l
					U[to] = False
					P[to] = P[cur_node] + " " + str(to)
				if U[to] is False:
					#print("put ", G[to])
					Q.put(G[to])
	for i in range(n):
		print("Node {}, max path {}, path {}".format(i, D[i], P[i]))


if __name__ == "__main__":
	main()