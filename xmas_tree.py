'''
Code Institute Christmas Challenge

Make a Christmas Tree in Python or in Javascript

'''

# Assigning various caracters and variables
i = 0

# Change max value to made a bigger or smaller christmas tree
max = 18
left_tree = '/'
right_tree = '\\'
bar = '_'
star = '*'
starting_space = ' '*(max-1)

# Leave a space in top
print()

# While loop to loop over the size of the tree
while i in range(max):
    starting_space = ' ' * (max - i)
    # If i = 0 print the vertical bar as top of tree
    if i == 0:
        space = (i*'')
        i += 1
        print(starting_space + '|')
    # Get the first bar in the tree and add 'lights'
    if i < 4 and i % 3 == 0:
        space = (((i+i)-3)*'*')
        starting_space = ' '*(max - (i))
        i - 1
        print(starting_space + left_tree +
              bar + space + bar + right_tree)
    # Get all the remaining bar in the tree and add 'lights'
    if i > 3 and i % 3 == 0:
        space = (((i+i)-3)*'*')
        starting_space = ' '*(max - (i))
        i - 1
        print(starting_space + left_tree +
              bar + space + bar + right_tree)
    # Prevent having double space in the second row
    if i == 1:
        space = (((i+i)-1)*'*')
        starting_space = ' '*(max - (i))
        i += 1
        print(starting_space + left_tree + space + right_tree)
    # loop over the rest of the tree
    else:
        space = (((i+i)-1)*' ')
        starting_space = ' '*(max - (i))
        i += 1
        print(starting_space + left_tree + space + right_tree)


# Assign values and caracter for the bottom of the tree
bar_vertical = '|'
space_star = ((max*2)-1) * '*'
full_line = ((max*2)-1) * '_'
half_line = 10 * '_'
left_side = (max-5) * ' '

# Print the bottom of the tree
print(left_tree + space_star + right_tree)
print(bar_vertical + full_line + bar_vertical)
print(left_side+bar_vertical+half_line+bar_vertical)
