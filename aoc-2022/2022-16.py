import networkx as nx
from parse import parse

G = nx.Graph()

with open("day16.txt") as f:
    for line in f.readlines():
        p = parse("Valve {} has flow rate={:d}; {} to {} {}",
                    line.strip())

        node, flow_rate, _, _, connections = p.fixed

        G.add_node(node, flow=flow_rate)
        for conn in connections.split(", "):
            G.add_edge(node, conn)


start = "AA"