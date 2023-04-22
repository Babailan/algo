# Array tester
n = [5, 1, 543, 51, 32, 2]


def bubblesort(array):
    for i in range(0, len(n)):
        for j in range(i + 1, len(n)):
            if array[i] > array[j]:
                replacer = array[i]
                array[i] = array[j]
                array[j] = replacer
