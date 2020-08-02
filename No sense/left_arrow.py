width = int(input("> "))

numbers = list(range(1, width + 1))
for r in range((width - 1) * -1, width):
    r = abs(r) * - 1
    string_numbers = map(str, numbers[:r if r else None])
    margin = ' ' * (width - abs(r))
    print(margin, *string_numbers)

#> 7
#  1
#   1 2
#    1 2 3
#     1 2 3 4
#      1 2 3 4 5
#       1 2 3 4 5 6
#        1 2 3 4 5 6 7
#       1 2 3 4 5 6
#      1 2 3 4 5
#     1 2 3 4
#    1 2 3
#   1 2
#  1
