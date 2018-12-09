
INF = 1000000
G = [[[1,2], [2,3]],[[3,13],[0, 2],[2, 0]],[[3,6],[0,3]],[[2, 6],[1, 13]]] #graph
#G = [[[1,2], [2,3]],[[3,9],],[[3,6],],[[2, 6],[1, 9]]] #graph
D = [] # lenghts
U = [] # marks
P = dict() # parents


def main():
	n = 4
	global D, U
	D = [INF] * n
	U = [False] * n
	#n = int(input("input n node : "))
	find(n, 0)
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

def find(n, s):
	D[s] = 0
	for i in range(n):
		v = -1
		for j in range(n): # find min len in d[] and unmark u[]
			if (D[j] < D[v] or v == -1) and U[j] is False:
				v = j
		if D[v] == INF:
			break
		U[v] = True

		for j in G[v]:
			to = j[0] #node number
			l = j[1] #len
			#print("to {}, len {}".format(to, l))
			if D[v] + l < D[to]:
				D[to] = D[v] + l
				#print("P[to] {}, V {}".format(to, v))
				if to in P:
					P[to].append(v)
				else:
					P[to] = [v,]
	print(D)
	for j in range(n):
		print("Node {}, shortest path {}".format(j,D[j]))

	print("p ", P)


if __name__ == "__main__":
	main()