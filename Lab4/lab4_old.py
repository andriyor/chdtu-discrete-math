import random
from string import ascii_uppercase


def prima(W, city_labels=None):
    _ = float('inf')
    cities_count = len(W)
    # перевірка на розмірність таблиці звязку
    for weights in W:
        assert len(weights) == cities_count
    # генерація імен вершин
    if not city_labels:
        city_labels = [ascii_uppercase[x] for x in range(cities_count)]
    assert cities_count <= len(city_labels)
    # вибір початкової вершини
    free_vertexes = list(range(0, len(city_labels)))
    starting_vertex = random.choice(free_vertexes)
    tied = [starting_vertex]
    free_vertexes.remove(starting_vertex)
    print('Починаючи з %s' % city_labels[starting_vertex])
    road_length = 0
    # поки є вільні вершини
    while free_vertexes:
        min_link = None  # З'єднання, створююче мінімальний шлях
        overall_min_path = _  # мінімальний шлях серед всих можливих
        # прохід по всім вже зв'язаним шляхом вершинам
        for current_vertex in tied:
            weights = W[current_vertex]  # зв'язок вершини з другими
            min_path = _
            free_vertex_min = current_vertex
            # прохід по зв'язаним точкам
            for vertex in range(cities_count):
                vertex_path = weights[vertex]
                if vertex_path == 0:
                    continue
                if vertex in free_vertexes and vertex_path < min_path:
                    free_vertex_min = vertex
                    min_path = vertex_path

            if free_vertex_min != current_vertex:
                if overall_min_path > min_path:
                    min_link = (current_vertex, free_vertex_min)
                    overall_min_path = min_path
        try:
            path_length = W[min_link[0]][min_link[1]]
        except TypeError:
            print('Неможливо знайти шлях')
            return
        print('З\'єднання %s до %s [%s]' % (city_labels[min_link[0]], city_labels[min_link[1]], path_length))

        road_length += path_length
        free_vertexes.remove(min_link[1])
        tied.append(min_link[1])
    print('Вага мінімального остовного дерева становить: %s' % road_length)


W = []
if __name__ == '__main__':
    W = [[0] * 5 for i in range(5)]

    for i in range(5):
        for j in range(5):
            if i != j:
                r = random.randint(1, 20)
                W[i][j] = r
                W[j][i] = r

    for row in W:
        print(', '.join([str(elem) for elem in row]) + ',')

prima(W)
