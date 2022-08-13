# The first line contains a number 1 <= n <= 10^5,
# the second contains an array A[1...n] containing natural numbers not exceeding 10^9.
# You need to count the number of pairs of indices 1 <= i < j <= n for which A[i] > A[j].
# (Such a pair of elements is called an array inversion. The number of inversions in an array is, in a sense,
# a measure of its disorder: for example, in a non-decreasing array, there are no inversions at all,
# but in a descending array, every two elements form an inversion.)

# Sample Input:
# 5
# 2 3 9 2 9

# Sample Output:
# 2


def enhance_merge_sort(arr, temp_arr, left, right):
    inversions_count = 0

    if left < right:
        mid = (left + right) // 2
        inversions_count += enhance_merge_sort(arr, temp_arr, left, mid)
        inversions_count += enhance_merge_sort(arr, temp_arr, mid + 1, right)
        inversions_count += enhance_merge(arr, temp_arr, left, mid, right)

    return inversions_count


def enhance_merge(arr, temp_arr, left, mid, right):
    i = left
    j = mid + 1
    k = left
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
            k += 1
        else:
            temp_arr[k] = arr[j]
            j += 1
            k += 1
            inv_count += (mid - i + 1)

    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    for idx in range(left, right + 1):
        arr[idx] = temp_arr[idx]

    return inv_count


def main():
    input()
    arr = list(map(int, input().split()))
    arr_length = len(arr)
    temp_arr = [0] * arr_length
    inversions_count = enhance_merge_sort(arr, temp_arr, 0, arr_length - 1)
    print(inversions_count)


if __name__ == '__main__':
    main()
