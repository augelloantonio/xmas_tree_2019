# Code Institute Christmas Challenge

This is Code Institute Christmas Challenge.

## The Challenge 
The description of the challenge is as follow:

![The Challenge](https://github.com/gello94/xmas_tree_2019/blob/master/challenge.png)

## My Solution

I use Python to solve this challenge and I wanted to add some 'lights' to the tree (represented as *).

My solution is based on a While Loop. I assigned different variables and made the characters I need to made the tree:

```
left_tree = '/'
right_tree = '\\'
bar = '_'
star = '*'
starting_space = ' '*(max-1) # This is the left side space 
```

To meet my criteria I used a While Loop assigning as range my 'max' variable, this way it is possible to change as well the size of the tree.

### Tree Basement

To made the tree basement I assigned the variables as follow:

```
bar_vertical = '|'
space_star = ((max*2)-1) * '*'
full_line = ((max*2)-1) * '_'
half_line = 10 * '_'
left_side = (max-5) * ' '
```

The basement will always be on the middle of the tree because it follows the size of the max value ('left_side' variable).

## Ho to run my code locally

1. Copy the repo: 
``` $ git clone https://github.com/gello94/xmas_tree_2019```

2. Run the .py file:
``` $ python xmas_tree.py ```

**DO you want to change the size of the tree?**
Just change the 'max' variable value.





