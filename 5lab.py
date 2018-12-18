# G = [
# 	[[1,2], [2,3]],
# 	[[3,13], [0, 2], [2, 0]],
# 	[[3,6], [0,3], [1, 0], [4,7]],
# 	[[2, 6], [1, 13], [4,12]],
# 	[[3,12], [2, 7]]
# ]
#[0] end node number 
#[1] capacity
#[2] max flow
#[3] flow
#[4] weight

G = [
	[[1, -2, 20]],
	[[2, 5, 13], [3, 2, 2]],
	[[3,-5], [4,6]],
	[[4, 5]],
	[[4, 0]]
]
INF = 100000
D = []
U = []
M = []
P = dict()

def add_weight_edge():
	global G
	for start, node in enumerate(G):
		for edge in node:
			finish = edge[0]
			edge[4] = edge[1] + U[start] - U[finish]
	print(G)


def bellman():
	global G, U
	for start, node in enumerate(G):
		for edge in node:
			finish = edge[0]
			if U[start] + edge[1] < U[finish]:
				U[finish] = U[start] + edge[1]


def dejkstra():
	global P, D, M
	D[0] = 0
	n = len(G)
	for i in range(n):
		v = -1
		for j in range(n): # find min len in d[] and unmark u[]
			if (D[j] < D[v] or v == -1) and M[j] is False:
				v = j
		if D[v] == INF:
			break
		M[v] = True

		for j in G[v]:
			to = j[0] #node number
			l = j[4] #weight
			#print("to {}, len {}".format(to, l))
			if D[v] + l < D[to]:
				D[to] = D[v] + l
				#print("P[to] {}, V {}".format(to, v))
				if to in P:
					P[to] = v
				else:
					P[to] = v

	for j in range(1,n):
		print("Node {}, shortest path {}  Parent: ".format(j,D[j]))
		prev_parent = ""
		for p in range(1,j+1):
			parent = P[p]
			if parent != prev_parent:
				print("{}   ".format(parent))
			prev_parent = parent


def main():
	global U, G, M, D
	U = [INF] * (len(G) + 1)
	M = [False] * (len(G) + 1)
	D = [INF] * (len(G) + 1)
	U[0] = 0
	for node in G:
		for edge in node:
			edge.append(0)
			edge.append(0)

	bellman()
	add_weight_edge()
	dejkstra()

if __name__ == "__main__":
	main()

