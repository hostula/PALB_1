#Union of both the arrays 
def find_union(a, b):
    union_set = set(a) | set(b)   # union of two sets
    return list(union_set)

# Example
a = [1, 2, 3, 4, 4]
b = [3, 4, 5, 6]

print(find_union(a, b))