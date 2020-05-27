def selection_sort(ls):
    for x in range(len(ls)):
        smallest_index = None
        for y in range(x, len(ls)):
            if smallest_index is None: 
                smallest_index = y
            elif ls[smallest_index] > ls[y]:
                smallest_index = y
        ls[x], ls[smallest_index] = ls[smallest_index], ls[x]    
    return ls

if __name__ == "__main__":
    import random
    print(selection_sort([random.randint(-1000, 1000) for i in range(50)]))