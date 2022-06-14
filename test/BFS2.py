graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}


def BFS(graph, s):
    queue = []
    queue.append(s)
    seen = set()
    seen.add(s)
    parent = {s: None}

    while queue:
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for m in nodes:
            if m not in seen:
                queue.append(m)
                seen.add(m)
                parent[m] = vertex
        print(vertex)
    return parent


if __name__ == "__main__":
    result = BFS(graph, "A")
    print(result)

    path=[]
    parent='D'
    while parent!=None:
        print(parent)
        path.append(parent)
        parent=result[parent]
    path.reverse()
    print(path)
# ————————————————
# 版权声明：本文为CSDN博主「HDD615」的原创文章，遵循CC
# 4.0
# BY - SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https: // blog.csdn.net / Sir666888 / article / details / 121612735