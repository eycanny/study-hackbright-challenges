def count_recursively(lst):
    """Return number of items in a list, using recursion."""

    if len(lst) == 0:
        return 0
        
    lst.pop()

    return 1 + count_recursively(lst)