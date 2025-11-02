def bucket_sort(arr):
    if len(arr) == 0:
        return arr
    bucket_count = 10
    buckets = [[] for _ in range(bucket_count)]
    for num in arr:
        index = int(bucket_count * num)
        buckets[index].append(num)

    for i in range(bucket_count):
        buckets[i].sort()

    return [num for bucket in buckets for num in bucket]
