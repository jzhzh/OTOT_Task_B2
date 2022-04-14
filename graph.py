import networkx as nx 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

df_nodes = pd.read_csv("./graph_dataset/nodes.csv")
df_edges = pd.read_csv("./graph_dataset/edges.csv")
# df = pd.merge(df_nodes,df_edges,on='source').reset_index(drop=True)

# print(df_nodes, df_edges)

labels={}
# color_map = []

# Creating a graph from the dataframe.
G = nx.from_pandas_edgelist(df_edges, 'source', 'target', create_using=nx.Graph())
df_nodes = df_nodes.set_index('id')
df_nodes = df_nodes.reindex(G.nodes())

# Creating a dictionary of labels for the nodes.
for node in G.nodes():
    if G.degree[node] > 7:
        print(node)
        labels[node]=node
    else:
        labels[node]=''

# A layout algorithm that positions the nodes in a graph.
pos = nx.spring_layout(G)

# Creating a color map for the nodes.
cmap = matplotlib.colors.ListedColormap(['tab:blue', 'darkorange', 'lightgreen'])
# plt.figure(figsize=(8,8))

# Draw graph
nx.draw(G, pos=pos, with_labels=False, node_color=df_nodes['group'], node_size=df_nodes['size']*13, edge_color='gray', width=1.0, cmap=cmap)
nx.draw_networkx_labels(G, pos, labels, font_size=10)



# plt.savefig('marvel.png', dpi=100)
plt.scatter([],[], label='Heroes')
plt.scatter([],[], label='Villains')
plt.scatter([],[], label='Antiheroes')
plt.legend()
plt.show()



