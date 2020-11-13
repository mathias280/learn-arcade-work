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

# Lab 4 code
# def get_map_2(map_array):

    # map2_file = open("map2_door.csv")

    # for line in map2_file:
        # line = line.strip()
        # map2_row = line.split(",")

        # for index, item in enumerate(map2_row):
           #  map2_row[index] = int(item)

       #  map_array.append(map2_row)
       #  map2_file.close()

   # return map_array


# def get_map_3(map_array):

   # map3_file = open("map2_background.csv")

   # for line in map3_file:
       # line = line.strip()
       # map3_row = line.split(",")

       # for index, item in enumerate(map3_row):
           # map3_row[index] = int(item)

        # map_array.append(map3_row)
        # map3_file.close()

    # return map_array
