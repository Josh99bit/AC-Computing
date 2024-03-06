lst1 = [['a', 'b', 'c'], ['d', 'e'], ['f', 'g', 'h', 'i']]
lst2 = [[1, ], [3, 7, 6, 4], [2, 9], [5, 8]]

def find_item (item, array):
    for n in range(len(array)):
        l=array[n]
        if item in l:
            return [n,l.index(item)]
    return "Not found!"
