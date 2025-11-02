def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1

    i = 0
    for num in range(len(count)):
        while count[num] > 0:
            arr[i] = num
            i += 1
            count[num] -= 1
    return arr
