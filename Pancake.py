def pancakeSort(arr):
    res = []
    for size in range(len(arr), 1, -1):
        max_num = max(arr[:size])
        max_index = arr.index(max_num)
        if max_index != size - 1:
            if max_index != 0:
                res.append(max_index + 1)
                arr[:max_index + 1] = reversed(arr[:max_index + 1])
            res.append(size)
            arr[:size] = reversed(arr[:size])
    return res
