from collections import defaultdict
from itertools import combinations

def build_relationships(keywords):
    edges = set()

    for a, b in combinations(keywords, 2):
        pair = tuple(sorted([a, b]))
        edges.add(pair)

    return list(edges)


def build_graph(all_keywords):
    graph = defaultdict(set)

    for kws in all_keywords:
        for a, b in combinations(kws, 2):
            graph[a].add(b)
            graph[b].add(a)

    return graph