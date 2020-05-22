def bubble_sort(_list):
    swapped = True
    while(swapped):
        swapped = False
        for i in range(0, len(_list)-1):
           if(_list[i] > _list[i+1]):
               _list[i], _list[i+1] = _list[i+1], _list[i]
               swapped = True
    return _list

if __name__ == "__main__":
    import random
    print(bubble_sort([random.randint(-1000,1000) for x in range(500)]))

