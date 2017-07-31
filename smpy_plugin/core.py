file_lines = []
file_iter = None

def _load_file(filename):
    global file_lines
    global file_iter
    with open(filename, 'r+') as file:
        file_lines = file.readlines()
    
    file_iter = iter(file_lines)

def _next_line():
    try:
        next_line = next(file_iter)
    except StopIteration:
        next_line = None
    return next_line

def parse_file(filename):
    _load_file(filename)

    return None

def print_code_tree(filename, code_tree):
    pass