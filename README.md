# ANALYZING-DNA-PATHWAYS-AND-THEIR-IMPACT-ON-CANCER-DEVELOPMENT

This project demonstrates how to interact with a Neo4j graph database to analyze gene interactions and visualize the relationships between genes. The code performs the following tasks:
<br><br>
<b>Connects to a Neo4j Database:</b> Establishes a connection to a Neo4j graph database containing gene interaction data.
<br><br>
<b>Fetches Gene Interaction Data:</b> Queries the database to retrieve genes and their interactions.
<br><br>
<b>Builds a NetworkX Graph:</b> Converts the fetched data into a NetworkX graph representation.
<br><br>
<b>Visualizes the Gene Interaction Network:</b> Uses Matplotlib to visualize the gene interaction graph.
<br><br>
<b>Performs BFS and DFS Traversals:</b> Implements both Breadth-First Search (BFS) and Depth-First Search (DFS) to explore gene interaction networks.
<br><br>
<b>Analyzes Mutations:</b> Analyzes pathways affected by mutations in specific genes using BFS traversal.
<br><br>
### How to Run the Code
<br>
<b>Set up Neo4j Database:</b>
<br>
Install and configure Neo4j.
Import gene interaction data into your Neo4j database. Ensure that the nodes are labeled as Gene and the relationships are of type INTERACTS_WITH.
<br><br>
<b>Update Connection Parameters:</b>
<br>
In the script, update the uri, user, and password in the Neo4jConnection class to match your Neo4j instance.
Run the Script
<br><br>
<b>Execute the Python script to:</b>
<br>
Query the Neo4j database for gene interactions.
Build and visualize the interaction graph.
Perform BFS and DFS traversals starting from a specified gene.
Analyze pathways affected by mutations in specified genes.
<br><br>
<b>Interpret the Output:</b>
<br>
The script will display the gene interaction graph and print the visited genes during BFS and DFS traversals.
It will also analyze and print the affected pathways for the mutated genes.
