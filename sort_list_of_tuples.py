musicians=[("Kendrick",32),("trio",18),("Ya levis",27),("Davido",33)]

def sort_by_age(musicians):
    return sorted(musicians,key=lambda musician:musician[1])

print(sort_by_age(musicians))