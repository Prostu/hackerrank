## Use this function to write data to socket
## write_string_to_socket(connection, message) where connection is the socket object and message is string

## Use this function to read data from socket
## def read_string_from_socket(connection) where connection is the socket object

## All global declarations go here
N = 0
graph = []

## This function is called only once before any client connection is accepted by the server.
## Read any global datasets or configurations here
def init_server():
    print "Reading training set"
    sys.stdout.flush()
    filename = "training.txt"
    global N, graph    
    with open( filename ) as f:
        # file read can happen here
        # print "file exists"
        N = int(f.readline())
        graph = [[] for i in xrange(N+1)]
        for i in xrange(1, N):
            [u, v] = map(int, f.readline().split(","))
            print "u=", u, " v=", v
            graph[u].append(v)
            graph[v].append(u)
            
def _distance_between_banks(u, v):
    global N, graph
    visited = [False for i in xrange(N+1)]
    
    def dfs(k):
        if k == v: return 1
        if visited[k]: return N
        visited[k] = True
        for node in graph[k]:
            dist = dfs(node)
            if dist < N: return 1 + dist
        return N
    
    return dfs(u)

## This function is called everytime a new connection is accepted by the server.
## Service the client here
def process_client_connection(connection):

    while True:
        # read message 
        message = read_string_from_socket(connection)
        
        if message == "END":
            write_string_to_socket(connection, message)
            break

        [a, b, q] = map(int, message.split(","))
        
        response = "YES" if _distance_between_banks(a, b) <= q else "NO"

        # write response
        write_string_to_socket(connection, response)
