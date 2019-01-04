import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


ARCHIVOGRAFO = "grafos/" + "argentina"

g = nx.read_gml(ARCHIVOGRAFO + ".gml")
g.number_of_nodes()


posiciones = nx.fruchterman_reingold_layout(g)
len(posiciones)


def plotear(g,posicion, titulo):
    grado = [sum(g.get_edge_data(x,y)["weight"] for y in g.neighbors(x))+1 for x in nx.nodes(g)]
    #plt.figure()
    #nx.draw(g, node_size=grado,node_color=grado , width=1.0,
    #    cmap="plasma",pos=posicion)
    nodes = g.nodes()
    ec = nx.draw_networkx_edges(g, posicion, alpha=0.2)
    nc = nx.draw_networkx_nodes(g, posicion, nodelist=nodes, node_size=grado,node_color=grado,
                                with_labels=False, cmap="plasma")
    plt.colorbar(nc)
    plt.axis('off')
    plt.savefig(ARCHIVOGRAFO+titulo+'.svg', format='svg', dpi=2400)
    plt.show()
    
plotear(g,posiciones, "")


print(nx.average_clustering(g),
nx.number_connected_components(g),
nx.density(g))


# In[ ]:


componentesConexas = sorted(nx.connected_components(g), key = len, reverse=True)
laMayor = componentesConexas[0]
print([len(x) for x in componentesConexas][:3])


# In[ ]:


mayorComponente = g.subgraph(laMayor)
posiciones = nx.kamada_kawai_layout(mayorComponente)
posiciones = nx.fruchterman_reingold_layout(mayorComponente, pos=posiciones)
plotear(mayorComponente,posiciones,"mayorComponente")


# In[ ]:


print(nx.density(mayorComponente))