def insertion_sort(ls):
    for index in range(1, len(ls)):
        for sub_index in range(0, index):
            if ls[index] < ls[sub_index]:
                ls[index], ls[sub_index] = ls[sub_index], ls[index]
    return ls

if __name__ == "__main__":
    import random
    print(insertion_sort([random.randint(-1000, 1000) for x in range(50)]))