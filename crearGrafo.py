import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import sys

FILE = sys.argv[1]
OUTPUT_FILE = sys.argv[2]
comments =pd.read_csv(FILE,index_col=0)

print(comments.count())

comments = comments[comments["user"] != "[deleted]"]
comments["parent"] = comments["parent"].map(lambda x: x[3:])
comments = comments[comments["parent"].str.contains("c")]

commentsNulos = "__NOT__"

userParents = [comments[comments["id"] == x]["user"] for x in comments["parent"].tolist()]
userParents = [x.values[0] if 0 < len(x.values) else commentsNulos for x in userParents]

comments["padre"] = userParents
comments = comments[comments["padre"] != commentsNulos]

print(comments.count())
users = comments["user"].unique()

M=nx.from_pandas_edgelist(comments, "user", 'padre', create_using=nx.MultiGraph())
g=nx.Graph()
for u,v in M.edges():
    if g.has_edge(u,v):
        g[u][v]['weight'] += 1
    else:
        g.add_edge(u, v, weight=1)
g.remove_edges_from(g.selfloop_edges())
E=g.edges
nx.write_gml(g, OUTPUT_FILE+".gml")