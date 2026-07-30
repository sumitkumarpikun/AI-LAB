
def bfs(graph,start_node):
    visited=[]
    queue=[start_node]
       
    while queue:
        current_node=queue.pop(0)
        if current_node not in visited:
            print(f"exploring_node:{current_node}")
            visited.append(current_node)
            #.get()prvents error if a node has no outgoing edges
        for neighour in graph.get(current_node,[]):
                if neighour not in visited and neighour not in queue:
                        queue.append(neighour)
                return visited
#_ _ _ user input section _ _ _
print("_ _ _ build your group _ _ _")
student_graph={}
#get the total number of connections
num_edges =int(input("how many edges(connecton) does your graph have?"))
print("enter each edge separate by a space (e.g.,A B):")
for i in range (num_edges):
    #readd the input and split it into two variables
    u,v = input (f"edge{i+1}:").split()
    #initialize the lists if the nodes don't exist yet
    if u not in student_graph:
        student_graph[u]=[]
    if v not in student_graph:
        student_graph[v]=[]
      #add the connection (undirected graph)      
    student_graph[u].append(v)
    student_graph[v].append(u)
       #get the starting piont
start =input("enter your strting node for bfs:")
print(f"\nyour graph dictionary: {student_graph}")
print("starting bfs traversal . . .")
bfs(student_graph,start)
