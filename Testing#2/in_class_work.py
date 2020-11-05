# Swapping values
my_list = [15, 57, 14, 33, 72, 79, 26, 56, 42, 40]

print(my_list)

temp = my_list[0]
my_list[0] = my_list[2]
my_list[2] = temp

my_list[0], my_list[2] = my_list[2], my_list[0]

print(my_list)

# Sorting
# Selection Sort
"""
selects and replaces the next smallest number until all numbers are sorted into whatever way assigned
"""
15, 57, 14, 33, 72, 79, 26, 56, 42, 40
15, 57, 14, 33, 72, 79, 26, 56, 42, 40
15, 57, 14, 33, 72, 79, 26, 56, 42, 40
15, 57, 14, 33, 72, 79, 26, 56, 42, 40
15, 57, 14, 33, 72, 79, 26, 56, 42, 40
15, 57, 14, 33, 72, 79, 26, 56, 42, 40
15, 57, 14, 33, 72, 79, 26, 56, 42, 40

def selection_sort(my_list):
    for cur_pos in range(len(my_list)):
        min_pos = cur_pos
        for scan_pos in range(cur_pos + 1, len(my_list)):
            if my_list[scan_pos] < my_list[min_pos]:
                min_pos = scan_pos

        #swap
        temp = my_list[min_pos]
        my_list[min_pos] = my_list[cur_pos]
        my_list[cur_pos] = temp

my_list = [15, 57, 14, 33, 72, 79, 26, 56, 42, 40]
selection_sort(my_list)
print(my_list)
