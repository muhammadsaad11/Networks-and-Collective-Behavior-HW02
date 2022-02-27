import networkx as nx
from statistics import mean  
import matplotlib.pyplot as plt
  
# G = nx.erdos_renyi_graph(50,0.5, directed = False)
# nx.draw(G, with_labels=True)
# # plt.show()
# print(G.number_of_edges())
# print(G.nodes())
# print(G.edges())
# # for line in nx.generate_adjlist(G):
# #     print(line)
# # for v in G.nodes():
# #     print(nx.clustering(G, v))
# path_lengths = []
# degrees = []
# clustering = []

# for node in G.nodes():
#     degrees.append(G.degree(node))
#     clustering.append(nx.clustering(G, node))
#     for node2 in G.nodes():
#         if node != node2:
#             path_lengths.append(nx.shortest_path_length(G, node, node2))
            
# print(path_lengths)
# print(degrees)
# print(clustering)

# print("Average Path Length:",mean(path_lengths))
# print("Average Degree:",mean(degrees))
# print("Average Clustering:",mean(clustering))

# # print(nx.shortest_path_length(G, 2,16))
# # print(nx.shortest_path_length(G, 16,2))
# # print(nx.generate_adjlist(G))


def Erdos_Reyni_graph(n, p):
    G = nx.erdos_renyi_graph(n,p, directed = False)
    # nx.draw(G, with_labels=True)
    # plt.show()
    path_lengths = []
    degrees = []
    clustering = []

    for node in G.nodes():
        degrees.append(G.degree(node))
        clustering.append(nx.clustering(G, node))
        for node2 in G.nodes():
            if node != node2:
                path_lengths.append(nx.shortest_path_length(G, node, node2))
                
    # print(path_lengths)
    # print(degrees)
    # print(clustering)

    # print("Average Path Length:",mean(path_lengths))
    # print("Average Degree:",mean(degrees))
    # print("Average Clustering:",mean(clustering))

    return (mean(path_lengths),mean(degrees),mean(clustering))





# def Erdos_Reyni_graph(n, p):
#     G = nx.erdos_renyi_graph(n,p, directed = False)
#     # nx.draw(G, with_labels=True)
#     # plt.show()
#     path_lengths = []
#     degrees = []
#     clustering = []

#     nodes_g = G.nodes()
#     print(nodes_g)
#     for node in range(len(nodes_g)):
#         print(nodes_g[2])
#         degrees.append(G.degree(nodes_g[node]))
#         clustering.append(nx.clustering(G, nodes_g[node]))
#         for node2 in range(node, len(nodes_g)):
#             print(nodes_g[node2])
#             path_lengths.append(nx.shortest_path_length(G, nodes_g[node], nodes_g[node2]))
                
#     # print(path_lengths)
#     # print(degrees)
#     # print(clustering)

#     # print("Average Path Length:",mean(path_lengths))
#     # print("Average Degree:",mean(degrees))
#     # print("Average Clustering:",mean(clustering))

#     return (mean(path_lengths),mean(degrees),mean(clustering))




Average_path_length = []
Average_clustering = []
Average_degree_network = []

for i in range (31):
    configurations = Erdos_Reyni_graph(100, 0.2)
    Average_path_length.append(configurations[0])
    Average_degree_network.append(configurations[1])
    Average_clustering.append(configurations[2])

G1 = nx.erdos_renyi_graph(100,0.2, directed = False)
degree_distribution_lst =[]
for node in G1.nodes():
    degree_distribution_lst.append(G1.degree(node))
print("When n = 100 and p = 0.2")
print("Average Clustering:",mean(Average_clustering))
print("Average Path Length:", mean(Average_path_length))
print("Average Degree:", mean(Average_degree_network))
# plt.bar(degree_distribution_lst, degree_distribution_lst)

# plt.show()
plt.hist(degree_distribution_lst, len(degree_distribution_lst)//2)
plt.show()


Average_path_length = []
Average_clustering = []
Average_degree_network = []

for i in range (31):
    configurations = Erdos_Reyni_graph(200, 0.1)
    Average_path_length.append(configurations[0])
    Average_degree_network.append(configurations[1])
    Average_clustering.append(configurations[2])

G1 = nx.erdos_renyi_graph(200,0.1, directed = False)
degree_distribution_lst =[]
for node in G1.nodes():
    degree_distribution_lst.append(G1.degree(node))
print("When n = 200 and p = 0.1")
print("Average Clustering:",mean(Average_clustering))
print("Average Path Length:", mean(Average_path_length))
print("Average Degree:", mean(Average_degree_network))
# plt.bar(degree_distribution_lst, degree_distribution_lst)

# plt.show()
plt.hist(degree_distribution_lst, len(degree_distribution_lst)//2)
plt.show()


Average_path_length = []
Average_clustering = []
Average_degree_network = []

for i in range (31):
    configurations = Erdos_Reyni_graph(400, 0.08)
    Average_path_length.append(configurations[0])
    Average_degree_network.append(configurations[1])
    Average_clustering.append(configurations[2])

G1 = nx.erdos_renyi_graph(400,0.08, directed = False)
degree_distribution_lst =[]
for node in G1.nodes():
    degree_distribution_lst.append(G1.degree(node))
print("When n = 400 and p = 0.08")
print("Average Clustering:",mean(Average_clustering))
print("Average Path Length:", mean(Average_path_length))
print("Average Degree:", mean(Average_degree_network))
# plt.bar(degree_distribution_lst, degree_distribution_lst)

# plt.show()
plt.hist(degree_distribution_lst, len(degree_distribution_lst)//2)
plt.show()