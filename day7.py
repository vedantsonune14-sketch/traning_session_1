# #1
# arr=[12,312,3,123,123]
# for i in range(10):
#     print(arr,end=" ")
# print(arr) 
# print(*arr)

arr = [3,3,4,2,4,4,2,4,4]
major = 0
count = 0
for num in arr:
    if count == 0:
        major = num
        count = 1
    elif num == major:
        count += 1
    else:
        count -= 1
if arr.count(major) > len(arr)//2:
    print("Majority element ",major)
else:
    print("No Majority Element")