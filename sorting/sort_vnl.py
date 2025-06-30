import csv

def load_csv(file):
    with open(file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

def insertion_sort(arr, key=lambda x: x):
    for i in range(1, len(arr)):
        current = arr[i]
        current_key = key(current)
        j = i - 1
        while j >= 0 and key(arr[j]) > current_key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
    return arr

if __name__ == "__main__":
    data = load_csv("data/VNL2023.csv")
    
    sorted_data = insertion_sort(data, key=lambda x: int(x["Age"]))
    print("VNL Men 2023 players sorted by age:")
    for player in sorted_data:
        print(f"{player['Player']} ({player['Country']}) - {player['Age']}")

