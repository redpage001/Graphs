from collections import deque

def earliest_ancestor(ancestors, starting_node):
    
    tree = dict()
    for pair in ancestors:
        tree[pair[1]] = tree.get(pair[1], []) # Initialize child key with empty list if not in dictionary
        tree[pair[1]].append(pair[0]) # Appending parent to the child key
        tree[pair[0]] = tree.get(pair[0], []) # Initialize parent key with empty list if not in dictionary

    if tree[starting_node] == []: # If starting_node has no parents
        return -1

    s = deque()
    visited = set()
    paths = list()
    s.append([starting_node])

    while len(s) > 0:
        path = s.pop()
        last_node = path[-1]

        if last_node not in visited:
            visited.add(last_node)

            for parent in tree[last_node]:
                copy_path = path.copy()
                copy_path.append(parent)
                s.append(copy_path)
                paths.append(copy_path) # Append each path to list of paths

    print("Paths: ", paths)
    answers = list()

    for path in paths: # Searches all valid paths
        longest = max(paths, key=len) # Finds the value of the longest path in the list
        if len(path) == len(longest): # Checks paths that match with the length of the longest path
            answers.append(path)

    answers.sort(key = lambda e: e[-1]) # Sorts arrays with the same length from smallest to largest by last index in respective arrays
    print(answers)
    return answers[0][-1] # Returns last node in first array