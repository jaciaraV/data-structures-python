#  Ex insertion sort

def insertion(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
    return arr

if __name__ == "__main__":
    numbers = []

    print("Please enter five numbers:\n")

    while len(numbers) < 5:
        try:
            num = int(input(f"Number {len(numbers)+1}: "))
            numbers.append(num)
        except ValueError:
            print("Please enter a valid number.")

    print("Numbers entered:", numbers)

    sorted_numbers = insertion(numbers.copy())
    print("Numbers sorted:", sorted_numbers)

    