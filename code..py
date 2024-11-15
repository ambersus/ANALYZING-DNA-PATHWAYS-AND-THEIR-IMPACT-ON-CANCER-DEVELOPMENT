from neo4j import GraphDatabase
import networkx as nx
import matplotlib.pyplot as plt

class Neo4jConnection:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        if self.driver:
            self.driver.close()

    def query(self, query, parameters=None, db=None):
        session = None
        response = None
        try:
            session = self.driver.session(database=db) if db is not None else self.driver.session()
            response = list(session.run(query, parameters))
        except Exception as e:
            print(f"Query failed: {e}")
        finally:
            if session:
                session.close()
        return response

# Connect to Neo4j database
neo4j_conn = Neo4jConnection(uri="bolt://localhost:7687", user="neo4j", password="Rishi@2006")

# Query to fetch genes and their interactions from Neo4j
cypher_query = """
MATCH (g1:Gene)-[:INTERACTS_WITH]->(g2:Gene)
RETURN g1.name AS gene1, g2.name AS gene2
"""

# Run the query
results = neo4j_conn.query(cypher_query)

# Build the graph from Neo4j data
def build_graph_from_neo4j(results):
    G = nx.Graph()

    # Add nodes and edges based on the Neo4j query results
    for record in results:
        gene1 = record['gene1']
        gene2 = record['gene2']
        G.add_edge(gene1, gene2)

    return G

# Visualize the graph
def visualize_graph(G):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=2000, font_size=12)
    plt.show()

# Build and visualize the graph from Neo4j data
G = build_graph_from_neo4j(results)
visualize_graph(G)

# BFS Traversal
def bfs_traversal(graph, start_node):
    visited = set()
    queue = [start_node]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(f"Visited: {node}")
            visited.add(node)
            # Add neighbors to queue
            neighbors = list(graph.neighbors(node))
            queue.extend([n for n in neighbors if n not in visited])

# DFS Traversal
def dfs_traversal(graph, node, visited=None):
    if visited is None:
        visited = set()

    if node not in visited:
        print(f"Visited: {node}")
        visited.add(node)

        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                dfs_traversal(graph, neighbor, visited)

# Perform BFS starting from 'BRCA1'
print("BFS Traversal from BRCA1:")
bfs_traversal(G, 'BRCA1')

# Perform DFS starting from 'BRCA1'
print("\nDFS Traversal from BRCA1:")
dfs_traversal(G, 'BRCA1')

# Example: Identify mutation in a gene
mutated_genes = ['BRCA1', 'TP53']

def analyze_mutations(graph, mutated_genes):
    for gene in mutated_genes:
        print(f"\nAnalyzing pathways affected by mutation in {gene}:")
        bfs_traversal(graph, gene)

# Analyze mutations in the graph
analyze_mutations(G, mutated_genes)

# Close the connection to Neo4j
neo4j_conn.close()
