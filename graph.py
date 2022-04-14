import networkx as nx 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

df_nodes = pd.read_csv("./graph_dataset/nodes.csv")
df_edges = pd.read_csv("./graph_dataset/edges.csv")

# print(df_nodes, df_edges)

labels={}


G = nx.from_pandas_edgelist(df_edges, 'source', 'target', create_using=nx.Graph())

for node in G.nodes():
    if G.degree[node] > 7:
        print(node)
        labels[node]=node
    else:
        labels[node]=''

pos = nx.spring_layout(G)
cmap = matplotlib.colors.ListedColormap(['tab:blue', 'darkorange', 'lightgreen'])
# plt.figure(figsize=(8,8))

nx.draw(G, pos=pos, with_labels=False, node_color=df_nodes['group'], node_size=df_nodes['size']*13, edge_color='gray', width=1.0, cmap=cmap)
nx.draw_networkx_labels(G, pos, labels, font_size=10)



# plt.savefig('marvel.png', dpi=100)
plt.scatter([],[], label='Heroes')
plt.scatter([],[], label='Villains')
plt.scatter([],[], label='Antiheroes')
plt.legend()
plt.show()



