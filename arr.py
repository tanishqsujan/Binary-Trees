tree= [None] * 10  #Initial Size

def ensure_capacity(index):
    """Ensure the tree array has enough capacity."""
    if index >= len(tree):
        #Extend the tree size
        new_size= max(index + 1, len(tree) * 2)
        tree.extend([None] * (new_size - len(tree)))
        
def root(key):
    if tree[0] is not None:
        print("Tree already has a root")
    else:
        tree[0]= key
        
def set_left(key, parent):
    child_index= (parent * 2) + 1
    if parent >= len(tree) or tree[parent] is None:
        print(f"Can't set left child at index {child_index}, no parent found at index {parent}")
    else:
        ensure_capacity(child_index)
        tree[child_index]= key
        
def set_right(key, parent):
    child_index= (parent * 2) + 2
    if parent >= len(tree) or tree[parent] is None:
        print("Can't see right child at index {child_index}, no parent found at index {parent}")