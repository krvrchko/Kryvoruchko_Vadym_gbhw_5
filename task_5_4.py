src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

lst_range = range(1, len(src))

num_lst = [src[i] for i in lst_range if int(src[i]) > int(src[i-1])]

print(num_lst)