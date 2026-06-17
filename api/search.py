def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1
    probes = 0

    while low <= high and target >= arr[low] and target <= arr[high]:
        probes += 1

        # Avoid division by zero
        if arr[high] == arr[low]:
            return probes

        if low == high:
            return probes

        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[pos] == target:
            return probes
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return probes


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    probes = 0

    while low <= high:
        probes += 1
        mid = (low + high) // 2

        if arr[mid] == target:
            return probes
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return probes


def handler(request):
    try:
        target = int(request.args.get("target", 5000))
    except:
        target = 5000

    arr = list(range(1, 10001))

    probes_i = interpolation_search(arr, target)
    probes_b = binary_search(arr, target)

    return {
        "target": target,
        "interpolation_probes": probes_i,
        "binary_probes": probes_b
    }
