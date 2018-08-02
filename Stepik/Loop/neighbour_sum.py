input_list = [int(i) for i in input().split()]
# dummy case
if len(input_list) == 1:
    print(input_list[0])
# main case
else:
    l_list = input_list[1:] + input_list[:-1]      # shift left
    r_list = input_list[-1:] + input_list[:-1]     # shift right
    def star(t):                                   # unpack
        x, y = t
        return x + y
    for i in map(star, list(zip(l_list, r_list))): # create tuple via zip, unpack and iterate with map
        print(i, end=" ")