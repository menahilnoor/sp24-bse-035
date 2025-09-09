
list1 = [int(input("Enter number for list1: "))
         for _ in range(int(input("How many numbers in first list? ")))]
list2 = [int(input("Enter number for list2: "))
         for _ in range(int(input("How many numbers in second list? ")))]

merged_list = sorted(list1 + list2)
print("Merged and Sorted List:", merged_list)

print("Smallest element:", min(merged_list))
print("Largest element:", max(merged_list))
