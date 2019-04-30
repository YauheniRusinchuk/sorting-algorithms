your_list:list = [5,2,3,1,88,33,7,10,17,32,66,101,9,8]

print(your_list)

def insert_sort(arr:list) -> None:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

insert_sort(your_list)
print(your_list)
