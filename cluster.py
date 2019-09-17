"""
Cluster data.
"""
import networkx as nx
from helper import json_loader, hashtags, fprint, draw_network_graph

def return_unique_user(tweets):
    user=set()
    uid=set()
    for i in tweets:
        user.add(i['screen_name'])
        uid.add(i['userid'])
    return list(user), list(uid)

def plot_graph(names):
    all_team = list(names.keys())
    graph = nx.Graph()
    for i in range(len(all_team)):
        for j in range(i+1, len(all_team)):
            all_data = list(set(names[all_team[i]]) & set(names[all_team[j]]))
            for each_node in all_data:
                graph.add_edges_from([(all_team[i],each_node)])
                graph.add_edges_from([(all_team[j],each_node)])
    return graph

def girvan_newman(graph, minimum, maximum):
    if graph.order() == 1:
        return [graph.nodes()]
    components = [each for each in nx.connected_component_subgraphs(graph)]
    edge_to_remove = sorted(nx.edge_betweenness_centrality(graph).items(), key=lambda x: x[1], reverse=True)
    count = 0
    while len(components) == 1:
        graph.remove_edge(*edge_to_remove[count][0])
        count += 1
        components = [c for c in nx.connected_component_subgraphs(graph)]
    result = []
    for c in components:
        if c.order() > maximum:
            result.extend(girvan_newman(c, minimum, maximum))
        elif (c.order() >= minimum and c.order() <= maximum):
            result.append(c.nodes())
    return result

def main():
    print("--------------------------------- Started Clustering -----------------------------------")   
    tweets=[]
    names={}
    open('cluster.txt', 'w')
    f = open('cluster.txt', 'a')
    for tags in hashtags:
        tweets= json_loader(tweets,tags)
        tweeter_names,_= return_unique_user(tweets)
        names[tags]=tweeter_names
    teams = list(names.keys())
    for i in range(len(teams)):
        for j in range(i+1,len(teams)):
                a =list(set(names[teams[i]] ) & set(names[teams[j]]))
                fprint("Common number of followers for the team "+teams[i]+" and "+teams[j] + " : "+ str(len(a)), f)
    graph = plot_graph(names)
    g = draw_network_graph(graph, names, "clusters.png")
    fprint('Graph has %d nodes and %d edges' %(graph.order(), graph.number_of_edges()), f)
    result = girvan_newman(g, 5, 20)
    for i in range(1, len(result)):
        fprint('Cluster %d  Number of nodes or followers %d' %(i, len(result[i])), f)
        draw_network_graph(graph.subgraph(result[i]), result[i], "cluster_"+str(i)+".png")
        print("Cluster %d nodes" %i, result[i], file=f)
    f.close()
    print("---------------------------------- Finished Clustering -----------------------------------")

if __name__ == '__main__':
    main()