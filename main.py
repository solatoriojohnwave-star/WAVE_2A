def build_unique_letter_array(full_name):
    unique_letters = []
    for ch in full_name.upper():
        if ch.isalpha() and ch not in unique_letters:
            unique_letters.append(ch)
    return unique_letters


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    full_name = "JOHN WAVE SOLATORIO"

    unsorted_array = build_unique_letter_array(full_name)
    sorted_array = bubble_sort(unsorted_array.copy())

    print("Full Name     :", full_name)
    print("Unsorted Array:", unsorted_array)
    print("Sorted Array  :", sorted_array)