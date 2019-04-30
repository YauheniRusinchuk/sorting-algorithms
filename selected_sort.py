your_list:list = [5,2,3,1,88,33,7,10,17,32,66,101,9,8]


print(your_list)


def selected_sort(arr:list) -> None:
    for i in range(len(arr)):
        mix_idx:int = i
        for j in range(i+1, len(arr)):
            if arr[mix_idx] > arr[j]:
                mix_idx = j

        arr[i], arr[mix_idx] = arr[mix_idx], arr[i]

#selected_sort(your_list)
#print(your_list)



def selected_sort_two(arr:list) -> None:
    for i in range(0, len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]


selected_sort_two(your_list)
print(your_list)
