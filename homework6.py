from random import randint

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def binary_search(element, sorted_list):
    left = 0
    right = len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == element:
            print(f"Элемент {element} найден на индексе {mid}.")
            return
        elif sorted_list[mid] < element:
            left = mid + 1
        else:
            right = mid - 1
    print(f"Элемент {element} не найден.")

if __name__ == "__main__":
    N = 10
    arr = [randint(1, 99) for _ in range(N)]
    print("Неотсортированный список:", arr)

    sorted_arr = selection_sort(arr)
    print("Отсортированный список:", sorted_arr)

    search_element = int(input("Введите число для поиска: "))
    binary_search(search_element, sorted_arr)

