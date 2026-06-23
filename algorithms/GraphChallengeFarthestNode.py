def find_farthest_nodes(input_p: str):
    global farthest_node_length, farthest_path
    path_list = [path.replace('-', '') for path in input_p]
    # print('path_list:', path_list)
    # All points
    node_list = list(set(''.join(path_list)))  # ['b', 'd', 'f', 'a', 'c', 'e']
    # print('node_list:', node_list)
    node_list.sort()  # ['a', 'b', 'c', 'd', 'e', 'f']
    # print('node_list:', node_list)

    # Search all one step paths to a point
    def search_one_step_path(node: str):
        one_step_paths_list = []
        for path in path_list:
            if node in path:
                if node == path[1]:
                    path = path[1] + path[0]
                one_step_paths_list.append(path)
        return one_step_paths_list

    # Search all N-step path of a point
    def search_n_step_path(node_degree_list: list):
        n_step_path_list = []
        for path in node_degree_list:
            # Search for all first-order paths of the n + 1 point
            # For example: search the first order path of the 3rd point
            one_step_paths_list = search_one_step_path(path[-1])
            # Delete the path containing the previous order (n-th point)
            # For example: delete the path to the second point based on the 2-step path
            one_step_paths_list = [p for p in one_step_paths_list if path[-2] not in p]
            #  The original n-step path + all steps in this node, get all the N + 1-stage path under this node
            n_step_path_part_list = [path[:-1] + p for p in one_step_paths_list]
            #  The path to all nodes is added together to form all N + 1-stage paths of origin
            n_step_path_list.extend(n_step_path_part_list)
        return n_step_path_list

    for node in node_list:
        node_degree_list = search_one_step_path(node)
        length, farthest_node_length = 1, 1
        farthest_path, highest_degree_node_list = node_degree_list, node_degree_list

        while True:
            higher_degree_node_list = search_n_step_path(node_degree_list)
            if higher_degree_node_list:
                highest_degree_node_list = higher_degree_node_list
                length += 1
            else:
                break
            node_degree_list = higher_degree_node_list
        if length > farthest_node_length:
            farthest_node_length = length
            farthest_path = highest_degree_node_list

    return farthest_node_length, farthest_path


if __name__ == '__main__':
    # Enter the adjacent path to get the farthest path
    input_paths = [["a-b", "b-c", "b-d"], ["b-e", "b-c", "c-d", "a-b", "e-f"], ["b-a", "c-e", "b-c", "d-c"]]
    for input_path in input_paths:
        farthest_node_length, farthest_path = find_farthest_nodes(input_path)
        print(f'For {input_path} path the farthest node length: {farthest_node_length} and one of farthest node paths: {farthest_path}')
