from os import getcwd, listdir
from os.path import isdir

#function that generates a directory tree as a nested list
#if depth is more than 2 directories it doesn't count them
def get_tree(path = getcwd(), depth = 0):
    tree = []
    if depth > 2:
        return tree
    for el in listdir(path):
        if isdir(dir_path := f"{path}\{el}"):
            el = [el, *get_tree(dir_path, depth + 1)]
        tree.append(el)
    return tree

#if started as main script it also realises fuтсtion that represents it
if __name__ == "__main__":
    from sys import argv
    if len(argv) > 2:
        raise Exception("Too much arguments")
    def print_tree(tree, indent = 0):
        for el in tree:
            if isinstance(el, str):
                print(" " * indent + "└ " + el)
            else:
                print(" " * indent + "└ " + el[0])
                print_tree(el[1:], indent + 1)
    print_tree(get_tree(*argv[1:]))
