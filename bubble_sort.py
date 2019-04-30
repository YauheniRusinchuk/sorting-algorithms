your_list:list = [5,2,3,1,88,33,7,10,17,32,66,101,9,8]

print(your_list)

def bubble_sort(arr:list) -> None:
    for j in range(len(arr)-1):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]


bubble_sort(your_list)
print(your_list)
